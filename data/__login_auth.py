import os
import asyncio
from playwright.async_api import async_playwright
from pages.login_page import LoginPage


class AuthManager:
    def __init__(self, browser_type="chromium"):
        self.browser_type = browser_type
        self.browser = None
        self.context = None
        self.page = None

    async def _launch_browser(self):
        self.playwright = await async_playwright().start()
        self.browser = await getattr(self.playwright, self.browser_type).launch(headless=True)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

    async def _close_browser(self):
        await self.browser.close()
        await self.playwright.stop()

    async def create_session(self, username, password, state_path):
        await self._launch_browser()
        login = LoginPage(self.page)
        print("Initiating create session . . .\n")

        # Open login page and perform login
        await login.open_login_page()
        print("Opening Login Page")
        await login.email_insert(username)
        print("Providing Valid Credentials")
        await login.next_button_click()
        await login.pass_insert(password)
        await login.next_button_click()
        await login.success_attempt()
        print("Login Success, Creating the file . . .")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(state_path), exist_ok=True)

        # Save authenticated state
        await self.context.storage_state(path=state_path)

        await self._close_browser()


if __name__ == "__main__":
    auth_manager = AuthManager()
    asyncio.run(auth_manager.create_session(
        username='simbah.test01@gmail.com',
        password='germa069',
        state_path='../data/.auth/session.json'
    ))
