import pytest
from playwright.async_api import async_playwright
import logging
import os
import json
import time
from pages.login_page import LoginPage


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
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
async def page(context):
    page = await context.new_page()
    yield page
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
        logger.info("Login Success, Creating the file . . .")
        await context.storage_state(path=SESSION_FILE)
        await context.close()

    # Create a context with the session file
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
async def auth(auth_context):
    page = await auth_context.new_page()
    yield page
    await page.close()
