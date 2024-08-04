import pytest
from playwright.async_api import async_playwright
import logging
import os

# Set up logging
# logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

SESSION_FILE = "data/.auth/session.json"


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

    # logger.info(f"Launching browser in {mode} mode")
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
        "no_viewport": not headless
    }

    context = await browser.new_context(**context_options)
    yield context
    await context.close()


@pytest.fixture()
async def page(context):
    page = await context.new_page()
    yield page
    await page.close()
