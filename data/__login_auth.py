from playwright.sync_api import sync_playwright


class AuthStateManager:
    def __init__(self, browser_type="chromium", headless=True):
        self.browser_type = browser_type
        self.headless = headless
        self.browser = None
        self.context = None
        self.page = None

    def _launch_browser(self):
        playwright = sync_playwright().start()
        self.browser = getattr(playwright, self.browser_type).launch(headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def _close_browser(self):
        self.browser.close()

    def login_and_save_state(self, login_url, username, password, state_path):
        self._launch_browser()
        self.page.goto(login_url)

        # Perform login
        self.page.get_by_label("Username or email address").fill(username)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

        # Save authenticated state
        self.context.storage_state(path=state_path)

        self._close_browser()


if __name__ == "__main__":
    auth_manager = AuthStateManager(headless=False)
    auth_manager.login_and_save_state(
        login_url='https://github.com/login',
        username='your_username',
        password='your_password',
        state_path='playwright/.auth/state.json'
    )
