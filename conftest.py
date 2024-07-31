import json
import time
import os
import pytest
from playwright.async_api import async_playwright
import allure
from datetime import datetime
import re
import logging
from data.__login_auth import AuthManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
async def playwright_instance():
    logger.info("Initializing Playwright instance")
    async with async_playwright() as playwright:
        yield playwright


@pytest.fixture(scope='class')
async def browser(playwright_instance):
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

    logger.info(f"Launching browser in {mode} mode")
    if mode == 'pipeline':
        browser = await playwright_instance[browser_type].launch(**launch_args)
    elif mode == 'local':
        browser = await playwright_instance[browser_type].launch(**launch_args)
    elif mode == 'grid':
        server_url = "http://remote-playwright-server:4444"
        browser = await playwright_instance[browser_type].connect(server_url)
    else:
        raise ValueError(f"Unsupported execution type: {mode}")

    yield browser
    logger.info("Closing browser")
    await browser.close()


@pytest.fixture(scope='function')
async def page(browser):
    video_option = os.getenv("video", "retain-on-failure")
    screenshot_option = os.getenv("screenshot", "only-on-failure")
    full_page_screenshot = os.getenv("full_page_screenshot", "off") == "on"
    headless = os.getenv("headless") == "True"

    logger.info("Creating browser context")
    context = await browser.new_context(
        viewport={"width": 1920, "height": 1080} if headless else None,
        record_video_dir="reports/videos" if video_option != "off" else None
    )

    page = await context.new_page()
    yield page

    logger.info("Taking screenshots and saving videos if necessary")
    if screenshot_option != "off":
        screenshot_path = f"reports/screenshots/{await _file_naming(page)}_screenshot.png"
        await page.screenshot(path=screenshot_path, full_page=full_page_screenshot)

    if video_option == "retain-on-failure" and hasattr(page, "video"):
        video_path = f"reports/videos/{await _file_naming(page)}_test_failed_video.webm"
        await page.video.save_as(video_path)

    await context.close()


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
async def auth_page(page):
    auth_manager = AuthManager(browser_type="chromium")

    if not os.path.exists(SESSION_FILE) or not ses_checker(SESSION_FILE):
        logger.info("Creating new session")
        await auth_manager.create_session(
            username='simbah.test01@gmail.com',
            password='germa069',
            state_path=SESSION_FILE
        )

    await page.context.storage_state(path=SESSION_FILE)
    yield page


async def _file_naming(page):
    title = re.sub(r'[^a-zA-Z0-9_\-]', '_', await page.title())
    if not title:
        title = "Untitled"
    timestamp = datetime.now().strftime("%d%m%y_%H%M%S")
    return f"{title}-{timestamp}"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "page" in item.funcargs:
            page = item.funcargs["page"]
            module_name = item.module.__name__.split('.')[-1]
            timestamp = datetime.now().strftime("%d%m%y_%H%M%S")

            screenshot_path = f"reports/screenshots/{module_name}-{timestamp}.png"
            page.loop.run_until_complete(page.screenshot(path=screenshot_path, full_page=True))
            allure.attach.file(screenshot_path, name=f"{module_name}-{timestamp}",
                               attachment_type=allure.attachment_type.PNG)

            if os.getenv("video") != "off" and hasattr(page, "video"):
                video_path = page.loop.run_until_complete(page.video.path())
                allure.attach.file(video_path, name=f"{module_name}-{timestamp}",
                                   attachment_type=allure.attachment_type.WEBM)
