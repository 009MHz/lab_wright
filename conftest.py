import os
import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    """ pytest --option variables from shell
    --browser:
        chromium= Run tests with Chromium.
        firefox= Run tests with Firefox.
        webkit = Run tests with WebKit.
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
    parser.addoption('--browser', help='', default='chromium')
    parser.addoption('--mode', help='', default='local')
    parser.addoption('--headless', action='store_true', default=False, help='Run tests in headless mode')


def pytest_configure(config):
    os.environ["env"] = config.getoption('env')
    os.environ["browser"] = config.getoption('browser')
    os.environ["mode"] = config.getoption('mode') or 'local'
    os.environ["headless"] = str(config.getoption('headless'))


@pytest.fixture(scope='session')
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope='class')
def browser(playwright_instance):
    browser_type = os.getenv("browser")
    execution_type = os.getenv("execution_type")
    headless = os.getenv("headless") == "True"

    if execution_type == 'grid' or execution_type == 'pipeline':
        # Configure remote browser options if needed
        server_url = "http://remote-playwright-server:4444"
        browser = playwright_instance[browser_type].connect(server_url, headless=headless)
    elif execution_type == 'local':
        browser = playwright_instance[browser_type].launch(headless=headless)
    else:
        raise ValueError(f"Unsupported execution type: {execution_type}")

    yield browser
    browser.close()


@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()