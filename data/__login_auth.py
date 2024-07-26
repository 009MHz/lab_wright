import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


class AuthManager:
    def __init__(self, browser_type="chromium"):
        self.browser_type = browser_type
        self.browser = None
        self.context = None
        self.page = None

    def _launch_browser(self):
        playwright = sync_playwright().start()
        self.browser = getattr(playwright, self.browser_type).launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def _close_browser(self):
        self.browser.close()

    def create_session(self, username, password, state_path):
        self._launch_browser()
        login = LoginPage(self.page)
        print("Initiating create session . . .\n")

        # Open login page and perform login
        login.open_login_page(), print("Opening Login Page")
        login.email_insert(username), print("Providing Valid Credentials")
        login.next_button_click()
        login.pass_insert(password)
        login.next_button_click()
        login.success_attempt(), print("Login Success, Creating the file . . .")

        # Ensure the directory exists
        os.makedirs(os.path.dirname(state_path), exist_ok=True)

        # Save authenticated state
        self.context.storage_state(path=state_path)

        self._close_browser()


if __name__ == "__main__":
    auth_manager = AuthManager()
    auth_manager.create_session(
        username='simbah.test01@gmail.com',
        password='germa069',
        state_path='../data/.auth/session.json'
    )
