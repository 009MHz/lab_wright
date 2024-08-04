from playwright.async_api import async_playwright, Playwright
import pytest
import logging
from datetime import datetime
import os
import allure
import re

# Set up logging
logging.basicConfig(level=logging.DEBUG)
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
async def browser(playwright: Playwright):
    browser_type = os.getenv("BROWSER", "chromium")
    mode = os.getenv("mode")
    headless = os.getenv("headless") == "True"

    launch_args = {
        "headless": headless,
        "args": ["--start-maximized"]
    }

    logger.info(f"Launching browser in {mode} mode")
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
    video_option = os.getenv("video", "retain-on-failure")

    context_options = {
        "viewport": {"width": 1920, "height": 1080} if headless else None,
        "no_viewport": not headless
    }

    if video_option != "off":
        context_options["record_video_dir"] = "reports/videos"

    context = await browser.new_context(**context_options)
    yield context
    await context.close()


@pytest.fixture()
async def page(context):
    screenshot_option = os.getenv("screenshot", "only-on-failure")
    full_page_screenshot = os.getenv("full_page_screenshot", "off") == "on"

    page = await context.new_page()
    yield page

    # if screenshot_option != "off":
    #     screenshot_path = f"reports/screenshots/{await _file_naming(page)}_screenshot.png"
    #     await page.screenshot(path=screenshot_path, full_page=full_page_screenshot)
    #
    # video_option = os.getenv("video", "retain-on-failure")
    # if video_option == "retain-on-failure" and hasattr(page, "video"):
    #     video_path = f"reports/videos/{await _file_naming(page)}_test_failed_video.webm"
    #     await page.video.save_as(video_path)

    await page.close()


# async def _file_naming(page):
#     title = await page.title()
#     title = re.sub(r'[^\w\s-]', '', title)
#     title = re.sub(r'[-\s]+', '-', title).strip('-')
#     timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
#     return f"{title}_{timestamp}"


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         if "page" in item.funcargs:
#             page = item.funcargs["page"]
#             module_name = item.module.__name__.split('.')[-1]

