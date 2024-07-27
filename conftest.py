import json
import time
import os
import pytest
from playwright.sync_api import sync_playwright
import allure
from datetime import datetime
import re
from data.__login_auth import AuthManager


SESSION_FILE = "data/.auth/session.json"


def pytest_addoption(parser):
    """ pytest --option variables from shell
    --env:
        dev: Run tests in dev environment (with dev data)
        test: Run tests in test environment (with test data)
        stage: Run tests in stage environment (with stage data)
    --execution_type:
        local: Run tests in your local machine.
        grid: Run tests with remote playwright server.
        pipeline: Run tests in CI pipeline.
    """
    parser.addoption('--env', action='store', default='test', help='')
    parser.addoption('--mode', help='', default='local')
    parser.addoption('--headless', action='store_true', default="--headed", help='Run tests in headless mode')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["mode"] = config.getoption('mode') or 'local'
    os.environ["headless"] = str(config.getoption('headless'))


@pytest.fixture(scope='session')
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope='class')
def browser(playwright_instance):
    browser_type = os.getenv("BROWSER", "chromium")
    mode = os.getenv("mode")
    headless = os.getenv("headless") == "True"

    video_dir = "reports/videos"
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)

    launch_args = {
        "headless": headless,
        "args": ["--start-maximized"]
    }

    if mode == 'pipeline':
        browser = playwright_instance[browser_type].launch(**launch_args)
    elif mode == 'local':
        browser = playwright_instance[browser_type].launch(**launch_args)
    elif mode == 'grid':
        server_url = "http://remote-playwright-server:4444"
        browser = playwright_instance[browser_type].connect(server_url)
    else:
        raise ValueError(f"Unsupported execution type: {mode}")

    yield browser
    browser.close()


@pytest.fixture(scope='function')
def page(browser):
    video_option = os.getenv("video", "retain-on-failure")
    screenshot_option = os.getenv("screenshot", "only-on-failure")
    full_page_screenshot = os.getenv("full_page_screenshot", "off") == "on"
    headless = os.getenv("headless") == "True"

    if headless:
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir="reports/videos" if video_option != "off" else None
        )
    else:
        context = browser.new_context(
            no_viewport=True,
            record_video_dir="reports/videos" if video_option != "off" else None
        )

    page = context.new_page()
    yield page

    if screenshot_option != "off":
        screenshot_path = f"reports/screenshots/{_file_naming(page)}_screenshot.png"
        page.screenshot(path=screenshot_path, full_page=full_page_screenshot)

    if video_option == "retain-on-failure" and hasattr(page, "video"):
        video_path = f"reports/videos/{_file_naming(page)}_test_failed_video.webm"
        page.close()
        page.video.save_as(video_path)

    context.close()


def ses_checker(session_file):
    """Check if the session data contains non-expired cookies."""
    try:
        with open(session_file, 'r') as source:
            data = json.load(source)
        cookies = data.get("cookies", [])
        current_time = time.time()
        for cookie in cookies:
            if cookie.get("expires", 0) < current_time:
                return False
        return True
    except (json.JSONDecodeError, FileNotFoundError):
        return False


@pytest.fixture(scope='function')
def auth_page(page):
    auth_manager = AuthManager(browser_type="chromium")

    if not os.path.exists(SESSION_FILE) or not ses_checker(SESSION_FILE):
        auth_manager.create_session(
            username='simbah.test01@gmail.com',
            password='germa069',
            state_path=SESSION_FILE
        )

    page.context.storage_state(path=SESSION_FILE)

    yield page


def _file_naming(page):
    title = re.sub(r'[^a-zA-Z0-9_\-]', '_', page.title())
    if not title:
        title = "Untitled"  # Fallback if title is empty after sanitization
    timestamp = datetime.now().strftime("%d%m%y_%H%M%S")
    return f"{title}-{timestamp}"


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            module_name = item.module.__name__.split('.')[-1]
            timestamp = datetime.now().strftime("%d%m%y_%H%M%S")

            screenshot_path = f"reports/screenshots/{module_name}-{timestamp}.png"
            page.screenshot(path=screenshot_path, full_page=True)
            allure.attach.file(screenshot_path, name=f"{module_name}-{timestamp}",
                               attachment_type=allure.attachment_type.PNG)

            if os.getenv("video") != "off" and hasattr(page, "video"):
                video_path = page.video.path()
                allure.attach.file(video_path, name=f"{module_name}-{timestamp}",
                                   attachment_type=allure.attachment_type.WEBM)
