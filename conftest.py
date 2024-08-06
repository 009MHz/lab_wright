import pytest
import logging
import os
import json
import time
import allure
import asyncio
from pages.login_page import LoginPage
from playwright.async_api import async_playwright

SESSION_FILE = "data/.auth/session.json"
SESSION_DIR = os.path.dirname(SESSION_FILE)


def pytest_addoption(parser):
    """
    pytest --option variables from shell
    --env:
        dev: Run tests in dev environment (with dev data)
        test: Run tests in test environment (with test data)
        stage: Run tests in stage environment (with stage data)
    --mode:
        local: Run tests in your local machine.
        grid: Run tests with remote playwright server.
        pipeline: Run tests in CI pipeline.
    """
    parser.addoption('--env', action='store', default='test', help='')
    parser.addoption('--mode', help='', default='local')
    parser.addoption('--headless', action='store_true', default=False, help='Run tests in headless mode')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["mode"] = config.getoption('mode') or 'local'
    os.environ["headless"] = str(config.getoption('headless'))


@pytest.fixture()
async def playwright():
    async with async_playwright() as playwright:
        yield playwright


@pytest.fixture()
async def browser(playwright):
    browser_type = os.getenv("BROWSER", "chromium")
    mode = os.getenv("mode")
    headless = os.getenv("headless") == "True"

    launch_args = {
        "headless": headless,
        "args": ["--start-maximized"]
    }

    if mode == 'pipeline':
        browser = await playwright[browser_type].launch(**launch_args)
    elif mode == 'local':
        browser = await playwright[browser_type].launch(**launch_args)
    elif mode == 'grid':
        server_url = "http://remote-playwright-server:4444"
        browser = await playwright[browser_type].connect(server_url)
    else:
        raise ValueError(f"Unsupported execution type: {mode}")

    yield browser
    await browser.close()


@pytest.fixture()
async def context(browser):
    headless = os.getenv("headless") == "True"
    context_options = {
        "viewport": {"width": 1920, "height": 1080} if headless else None,
        "no_viewport": not headless,
    }

    context = await browser.new_context(**context_options)
    yield context
    await context.close()


@pytest.fixture()
async def auth_context(browser):
    if not os.path.exists(SESSION_DIR):
        os.makedirs(SESSION_DIR)

    if not os.path.exists(SESSION_FILE) or session_checker(SESSION_FILE):
        context_options = {
            "viewport": {"width": 1920, "height": 1080} if os.getenv("headless") == "True" else None,
            "no_viewport": os.getenv("headless") != "True",
        }
        context = await browser.new_context(**context_options)
        page = await context.new_page()
        sess = LoginPage(page)
        await sess.create_session(
            'simbah.test01@gmail.com',
            'germa069')
        logging.info("Login Success, Creating the file . . .")
        await context.storage_state(path=SESSION_FILE)
        await context.close()

    headless = os.getenv("headless") == "True"
    context_options = {
        "viewport": {"width": 1920, "height": 1080} if headless else None,
        "no_viewport": not headless,
        "storage_state": SESSION_FILE,
    }
    context = await browser.new_context(**context_options)
    yield context
    await context.close()


@pytest.fixture()
async def auth_page(auth_context):
    screenshot_option = os.getenv("screenshot")
    page = await auth_context.new_page()
    yield page
    if screenshot_option != "off":
        screenshot_path = f"reports/screenshots/{await page.title()}.png"
        await page.screenshot(path=screenshot_path, full_page=True)
    await page.close()


@pytest.fixture()
async def page(context):
    screenshot_option = os.getenv("screenshot")
    page = await context.new_page()
    yield page
    if screenshot_option != "off":
        screenshot_path = f"reports/screenshots/{await page.title()}.png"
        await page.screenshot(path=screenshot_path, full_page=True)
    await page.close()


def session_checker(session_file):
    """Check if the session file contains expired cookies."""
    if not os.path.exists(session_file):
        return True

    with open(session_file, "r") as file:
        session_data = json.load(file)

    current_time = time.time()
    for cookie in session_data.get("cookies", []):
        if cookie.get("expires", 0) <= current_time:
            return True

    return False


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call": #  if rep.when == "call" and rep.failed: # config on fail only
        screenshot_path = os.path.join("reports/screenshots", f"{item.name}.png")
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

        try:
            page = item.funcargs.get('page') or item.funcargs.get('auth')
            if page:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(page.screenshot(path=screenshot_path, full_page=True))
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
        except Exception as e:
            print(f"Failed to take screenshot: {e}")
