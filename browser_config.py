import os
import json
import time
import logging
from pages.login_page import LoginPage

SESSION_FILE = "data/.auth/session.json"
SESSION_DIR = os.path.dirname(SESSION_FILE)

logging.getLogger('asyncio').setLevel(logging.WARNING)


class Config:
    def __init__(self):
        self.browser = None
        self.page = None

    def is_headless(self):
        return os.getenv("headless") == "True"

    async def setup_browser(self, playwright):
        browser_type = os.getenv("BROWSER", "chromium")
        mode = os.getenv("mode")
        headless = self.is_headless()

        launch_args = {
            "headless": headless,
            "args": ["--start-maximized"]
        }

        if mode == 'pipeline':
            self.browser = await playwright[browser_type].launch(**launch_args)
        elif mode == 'local':
            self.browser = await playwright[browser_type].launch(**launch_args)
        elif mode == 'grid':
            server_url = "http://remote-playwright-server:4444"
            self.browser = await playwright[browser_type].connect(server_url)
        else:
            raise ValueError(f"Unsupported execution type: {mode}")

    async def context_init(self, storage_state=None):
        headless = self.is_headless()
        context_options = {
            "viewport": {"width": 1920, "height": 1080} if headless else None,
            "no_viewport": not headless,
        }

        if storage_state:
            if not os.path.exists(SESSION_DIR):
                os.makedirs(SESSION_DIR)

            if not os.path.exists(SESSION_FILE) or self.session_checker(SESSION_FILE):
                context = await self.browser.new_context(**context_options)
                page = await context.new_page()
                sess = LoginPage(page)
                await sess.create_session('simbah.test03@gmail.com', 'germa069')
                logging.info("Login Success, Creating the file . . .")
                await context.storage_state(path=SESSION_FILE)
                await context.close()

            context_options["storage_state"] = SESSION_FILE

        return await self.browser.new_context(**context_options)

    async def setup_page(self):
        context = await self.context_init()
        self.page = await context.new_page()
        return self.page

    async def setup_auth_page(self):
        context = await self.context_init(storage_state=SESSION_FILE)
        self.page = await context.new_page()
        return self.page

    async def capture_handler(self):
        screenshot_option = os.getenv("screenshot")
        if screenshot_option != "off" and self.page:
            screenshot_path = f"reports/screenshots/{await self.page.title()}.png"
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            await self.page.screenshot(path=screenshot_path, full_page=True)

    def session_checker(self, session_file):
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
