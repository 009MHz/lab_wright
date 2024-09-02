import allure
from playwright.async_api import Page, expect
from elements.__res_builder import PageInfo, ResumeInfo
from pages.resume_builder.data_diri import PersonalInformation
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

    async def self_data_filling(self, page):
        handler = PersonalInformation(page)
        with allure.step("▸ Navigate to resume builder page"):
            await self.page.goto(PageInfo.url)
            await self._look(PageInfo.title)
            await expect(self._find(PageInfo.title)).to_have_text("Buat Resume Terbaikmu")

        with allure.step("▸ Insert the necessary data on the Data Diri input field"):
            await handler.insert_first_name('Play')
            await handler.insert_last_name('Wright')
            await handler.insert_email('halo@karirlab.co')
            await handler.insert_phone('085311111010')
            await handler.select_province_option_within("Jakarta")
            await handler.select_city_option_within("Jakarta Pusat")
            await handler.insert_address("Jl. Belawan No.16, RT.18/RW.1, Cideng, Kecamatan Gambir, "
                                           "Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10150")
            await handler.insert_linkedin("https://www.linkedin.com/company/karirlab/")
            await handler.insert_portfolio("https://github.com/microsoft/playwright")
            await handler.click_simpan_button()
