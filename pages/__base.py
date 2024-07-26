from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _find(self, locator: str):
        return self.page.locator(locator)

    def _look(self, locator: str, timeout: int = 10000):
        self.page.wait_for_selector(locator, state='visible', timeout=timeout)

    def _conceal(self, locator: str, timeout: int = 7000):
        self.page.wait_for_selector(locator, state='hidden', timeout=timeout)

    def _touch(self, locator: str, timeout: int = 10000):
        self._look(locator)
        self._find(locator).is_enabled(timeout=timeout)

    def _type(self, locator: str, text: str, timeout: int = 10000):
        self._look(locator, timeout)
        self._find(locator).fill(text)

    def _click(self, locator: str, timeout: int = 10000):
        self._touch(locator, timeout=timeout)
        self._find(locator).click()

    def _double_click(self, locator: str, timeout: int = 10000):
        self._touch(locator, timeout=timeout)
        self._find(locator).dblclick()

    def _force(self, locator: str, timeout: int = 10000):
        self._look(locator, timeout)
        self._find(locator).click(force=True, delay=500)

