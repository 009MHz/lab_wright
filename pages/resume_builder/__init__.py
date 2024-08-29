import allure
from playwright.async_api import Page, expect
from elements.__res_builder import PageInfo, ResumeInfo
from pages.__base import BasePage


class PreCond(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def load_page(self):
        with allure.step("▸ Navigate to resume builder page"):
            await self.page.goto(PageInfo.url)
            await self._look(PageInfo.title)
            await expect(self._find(PageInfo.title)).to_have_text("Buat Resume Terbaikmu")

    async def import_data_modal(self):
        with allure.step("▸ Navigate to resume builder page"):
            await self.page.goto(PageInfo.url)
            await self._look(PageInfo.title)
            await expect(self._find(PageInfo.title)).to_have_text("Buat Resume Terbaikmu")

        with allure.step("▸ Click on the Import Data button"):
            await self._click(ResumeInfo.import_btn)
            await expect(self._find(ResumeInfo.import_btn)).to_be_focused()

            await self._look(ResumeInfo.import_modal)
            await expect(self._find(ResumeInfo.import_modal)).to_be_visible()
