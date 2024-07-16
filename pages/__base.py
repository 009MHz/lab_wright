import json
import time as tm
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _find(self, locator: str):
        return self.page.locator(locator)

    def _view(self, locator: str, timeout: int = 10000):
        self.page.wait_for_selector(locator, timeout=timeout)

    def _unseen(self, locator: str, timeout: int = 10000):
        self.page.wait_for_selector(locator, state="hidden", timeout=timeout)

    def _type(self, locator: str, text: str, timeout: int = 10000):
        self._view(locator, timeout)
        self.page.fill(locator, text)

    def _touch(self, locator: str, timeout: int = 15000):
        self.page.wait_for_selector(locator, state="visible", timeout=timeout)

    def _click(self, locator: str):
        self._touch(locator)
        self.page.click(locator)

    def _collect(self, locator: str):
        return self.page.locator(locator).all_text_contents()

    def _url_check(self, url: str, timeout: int = 15000):
        self.page.wait_for_url(url, timeout=timeout)

    def _save_session(self, file_name: str):
        cookies = self.page.context.cookies()
        with open(file_name, 'w') as file:
            json.dump(cookies, file)

    def _load_session(self, file_name: str):
        with open(file_name, 'r') as file:
            cookies = json.load(file)
        self.page.context.add_cookies(cookies)

    def _retry(self, action: str, retry: int, interval: int, *args, **kwargs):
        """Retry action to hit flaky action
        example: self._retry("click", 3, 2, locator="xpath=//button")"""

        attempts = 0
        while attempts < retry:
            try:
                action_method = getattr(self, f"_{action}")
                action_method(*args, **kwargs)
                break  # Exit the loop if action succeeds
            except Exception as e:
                attempts += 1
                print(f"Retry attempt {attempts} failed for {action}: {e}")
                tm.sleep(interval)  # Wait for a moment before retrying
        else:
            raise Exception(f"Failed to perform action {action} after {retry} attempts")
