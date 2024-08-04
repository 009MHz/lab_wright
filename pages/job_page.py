from pages.__base import BasePage
from elements.__job import JobLoc
from playwright.async_api import Page, expect


class JobPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def open_page(self):
        await self.page.goto(JobLoc.url)

    """Job List Sorting Control"""
    async def sort_control_presence(self):
        await self._look(JobLoc.sort_control)
        await expect(self._find(JobLoc.sort_control)).to_be_visible()

    async def sort_control_click(self):
        await self._click(JobLoc.sort_control)

    async def sort_item_presence(self):
        for item in JobLoc.sort_options:
            await self._look(JobLoc.sort_control_expanded)
            await expect(self._find(JobLoc.sort_control_expanded)).to_be_visible()

            await self._look(JobLoc.sort_options[item])
            await expect(self._find(JobLoc.sort_options[item])).to_be_visible()
            await self._click(JobLoc.sort_options[item])
            await self.sort_control_click()

    """Job List Main Button Filter"""
    async def click_easy_apply(self):
        await self._click(JobLoc.btn_easy_apply)
        await expect(self._find(JobLoc.btn_easy_apply)).to_be_focused()

    async def click_msib(self):
        await self._click(JobLoc.btn_MSIB)
        await expect(self._find(JobLoc.btn_MSIB)).to_be_focused()

    async def click_clear(self):
        await self._click(JobLoc.btn_clear)
        await expect(self._find(JobLoc.btn_clear)).to_be_focused()

    async def click_apply(self):
        await self._click(JobLoc.btn_apply)
        await expect(self._find(JobLoc.btn_apply)).to_be_focused()

    """Job List Carousel"""
    async def _card_component(self, locator, component_name, index):
        locator = f"({locator})[{index}]"
        await self._look(locator)
        await expect(self._find(locator)).to_be_visible(timeout=3000), f"{component_name} is not visible for card {index}"

    async def job_cards_logo_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_logo, 'logo', index)

    async def job_cards_company_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_company_name, 'company', index)

    async def job_cards_title_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_job_title, 'title', index)

    async def job_cards_location_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_job_location, 'location', index)

    async def job_cards_description_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_job_description, 'description', index)

    async def job_cards_industry_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_job_industry, 'industry', index)

    async def job_cards_type_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_job_type, 'type', index)

    async def check_job_cards_daycount(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.body_job_daycount, 'daycount', index)

    async def job_cards_easyapply_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            if not await self._find(f"({JobLoc.body_job_easy_apply})[{index}]").is_visible():
                print(f"easyapply button doesn't apply for card {index}")
                continue
            await self._card_component(JobLoc.body_job_easy_apply, 'easyapply', index)

    async def job_cards_msib_presence(self):
        await self._look(JobLoc.body_cards)
        total_cards = await self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            if not await self._find(f"({JobLoc.body_job_msib})[{index}]").is_visible():
                print(f"msib button doesn't apply for card {index}")
                continue
            await self._card_component(JobLoc.body_job_msib, 'msib', index)

    async def position_input_presence(self):
        await self._touch(JobLoc.box_position_input)
        await expect(self._find(JobLoc.box_position_input)).to_be_visible()

        await self._click(JobLoc.box_position_input)
        await expect(self._find(JobLoc.box_position_input)).to_be_focused()

    """Filter Input Field Search"""
    async def position_input_type(self, text: str):
        await self._type(JobLoc.box_position_input, text)
        await expect(self._find(JobLoc.box_position_input)).not_to_be_empty()

    async def position_input_clear(self):
        await self._look(JobLoc.box_position_clear)
        await self._click(JobLoc.box_position_clear)
        await expect(self._find(JobLoc.box_position_input)).to_be_empty()

    async def company_input_presence(self):
        await self._touch(JobLoc.box_company_input)
        await expect(self._find(JobLoc.box_company_input)).to_be_visible()

        await self._click(JobLoc.box_company_input)
        await expect(self._find(JobLoc.box_company_input)).to_be_focused()

    async def company_input_type(self, text: str):
        await self._type(JobLoc.box_company_input, text)
        await expect(self._find(JobLoc.box_company_input)).not_to_be_empty()

    async def company_input_clear(self):
        await self._look(JobLoc.box_company_clear)
        await self._click(JobLoc.box_company_clear)
        await expect(self._find(JobLoc.box_company_input)).to_be_empty()

    async def industri_input_presence(self):
        await self._touch(JobLoc.box_industri_input)
        await expect(self._find(JobLoc.box_industri_input)).to_be_visible()

        await self._click(JobLoc.box_industri_input)
        await expect(self._find(JobLoc.box_industri_input)).to_be_focused()

    async def industri_input_type(self, text: str):
        await self._type(JobLoc.box_industri_input, text)
        await expect(self._find(JobLoc.box_industri_input)).not_to_be_empty()

    async def industri_input_clear(self):
        await self._force(JobLoc.box_industri_clear)
        await self._click(JobLoc.box_industri_clear)
        await expect(self._find(JobLoc.box_industri_input)).to_be_empty()

    async def lokasi_input_presence(self):
        await self._touch(JobLoc.box_lokasi_input)
        await expect(self._find(JobLoc.box_lokasi_input)).to_be_visible()

        await self._click(JobLoc.box_lokasi_input)
        await expect(self._find(JobLoc.box_lokasi_input)).to_be_focused()

    async def lokasi_input_type(self, text: str):
        await self._type(JobLoc.box_lokasi_input, text)
        await expect(self._find(JobLoc.box_lokasi_input)).not_to_be_empty()

    async def lokasi_input_clear(self):
        await self._force(JobLoc.box_lokasi_clear)
        await self._click(JobLoc.box_lokasi_clear)
        await expect(self._find(JobLoc.box_lokasi_input)).to_be_empty()

    async def skill_input_presence(self):
        await self._touch(JobLoc.box_skill_input)
        await expect(self._find(JobLoc.box_skill_input)).to_be_visible()

        await self._click(JobLoc.box_skill_input)
        await expect(self._find(JobLoc.box_skill_input)).to_be_focused()

    async def skill_input_type(self, text: str):
        await self._type(JobLoc.box_skill_input, text)
        await expect(self._find(JobLoc.box_skill_input)).not_to_be_empty()

    async def skill_input_clear(self):
        await self._force(JobLoc.box_skill_clear)
        await self._click(JobLoc.box_skill_clear)
        await expect(self._find(JobLoc.box_skill_input)).to_be_empty()

    """Tipe Pekerjaan Checkboxes Section"""
    async def full_time_presence(self):
        await self._look(JobLoc.checkbox_full)
        await expect(self._find(JobLoc.checkbox_full)).to_be_visible()

    async def full_time_check(self):
        await self._touch(JobLoc.checkbox_full)
        await self._find(JobLoc.checkbox_full).check()
        await expect(self._find(JobLoc.checkbox_full)).to_be_checked()

    async def full_time_uncheck(self):
        await self._click(JobLoc.checkbox_full)
        await expect(self._find(JobLoc.checkbox_full)).not_to_be_checked()

    async def part_time_presence(self):
        await self._look(JobLoc.checkbox_part)
        await expect(self._find(JobLoc.checkbox_part)).to_be_visible()

    async def part_time_check(self):
        await self._touch(JobLoc.checkbox_part)
        await self._find(JobLoc.checkbox_part).check()
        await expect(self._find(JobLoc.checkbox_part)).to_be_checked()

    async def part_time_uncheck(self):
        await self._click(JobLoc.checkbox_part)
        await expect(self._find(JobLoc.checkbox_part)).not_to_be_checked()

    async def intern_presence(self):
        await self._look(JobLoc.checkbox_intern)
        await expect(self._find(JobLoc.checkbox_intern)).to_be_visible()

    async def intern_check(self):
        await self._touch(JobLoc.checkbox_intern)
        await self._find(JobLoc.checkbox_intern).check()
        await expect(self._find(JobLoc.checkbox_intern)).to_be_checked()

    async def intern_uncheck(self):
        await self._click(JobLoc.checkbox_intern)
        await expect(self._find(JobLoc.checkbox_intern)).not_to_be_checked()

    async def volunteer_presence(self):
        await self._look(JobLoc.checkbox_volunteer)
        await expect(self._find(JobLoc.checkbox_volunteer)).to_be_visible()

    async def volunteer_check(self):
        await self._touch(JobLoc.checkbox_volunteer)
        await self._find(JobLoc.checkbox_volunteer).check()
        await expect(self._find(JobLoc.checkbox_volunteer)).to_be_checked()

    async def volunteer_uncheck(self):
        await self._click(JobLoc.checkbox_volunteer)
        await expect(self._find(JobLoc.checkbox_volunteer)).not_to_be_checked()

    async def contract_presence(self):
        await self._look(JobLoc.checkbox_contract)
        await expect(self._find(JobLoc.checkbox_contract)).to_be_visible()

    async def contract_check(self):
        await self._touch(JobLoc.checkbox_contract)
        await self._find(JobLoc.checkbox_contract).check()
        await expect(self._find(JobLoc.checkbox_contract)).to_be_checked()

    async def contract_uncheck(self):
        await self._click(JobLoc.checkbox_contract)
        await expect(self._find(JobLoc.checkbox_contract)).not_to_be_checked()

    async def scholar_presence(self):
        await self._look(JobLoc.checkbox_scholar)
        await expect(self._find(JobLoc.checkbox_scholar)).to_be_visible()

    async def scholar_check(self):
        await self._touch(JobLoc.checkbox_scholar)
        await self._find(JobLoc.checkbox_scholar).check()
        await expect(self._find(JobLoc.checkbox_scholar)).to_be_checked()

    async def scholar_uncheck(self):
        await self._click(JobLoc.checkbox_scholar)
        await expect(self._find(JobLoc.checkbox_scholar)).not_to_be_checked()

    async def partner_presence(self):
        await self._look(JobLoc.checkbox_partner)
        await expect(self._find(JobLoc.checkbox_partner)).to_be_visible()

    async def partner_check(self):
        await self._touch(JobLoc.checkbox_partner)
        await self._find(JobLoc.checkbox_partner).check()
        await expect(self._find(JobLoc.checkbox_partner)).to_be_checked()

    async def partner_uncheck(self):
        await self._click(JobLoc.checkbox_partner)
        await expect(self._find(JobLoc.checkbox_partner)).not_to_be_checked()

    """Tipe Pengaturan Kerja Section"""
    async def hybrid_presence(self):
        await self._look(JobLoc.checkbox_hybrid)
        await expect(self._find(JobLoc.checkbox_hybrid)).to_be_visible()

    async def hybrid_check(self):
        await self._touch(JobLoc.checkbox_hybrid)
        await self._find(JobLoc.checkbox_hybrid).check()
        await expect(self._find(JobLoc.checkbox_hybrid)).to_be_checked()

    async def hybrid_uncheck(self):
        await self._click(JobLoc.checkbox_hybrid)
        await expect(self._find(JobLoc.checkbox_hybrid)).not_to_be_checked()
        
    async def on_site_presence(self):
        await self._look(JobLoc.checkbox_on_site)
        await expect(self._find(JobLoc.checkbox_on_site)).to_be_visible()

    async def on_site_check(self):
        await self._touch(JobLoc.checkbox_on_site)
        await self._find(JobLoc.checkbox_on_site).check()
        await expect(self._find(JobLoc.checkbox_on_site)).to_be_checked()

    async def on_site_uncheck(self):
        await self._click(JobLoc.checkbox_on_site)
        await expect(self._find(JobLoc.checkbox_on_site)).not_to_be_checked()
        
    async def remote_presence(self):
        await self._look(JobLoc.checkbox_remote)
        await expect(self._find(JobLoc.checkbox_remote)).to_be_visible()

    async def remote_check(self):
        await self._touch(JobLoc.checkbox_remote)
        await self._find(JobLoc.checkbox_remote).check()
        await expect(self._find(JobLoc.checkbox_remote)).to_be_checked()

    async def remote_uncheck(self):
        await self._click(JobLoc.checkbox_remote)
        await expect(self._find(JobLoc.checkbox_remote)).not_to_be_checked()

    """Pengalaman Kerja Section"""
    async def no_exp_presence(self):
        await self._look(JobLoc.checkbox_no_exp)
        await expect(self._find(JobLoc.checkbox_no_exp)).to_be_visible()

    async def no_exp_check(self):
        await self._touch(JobLoc.checkbox_no_exp)
        await self._find(JobLoc.checkbox_no_exp).check()
        await expect(self._find(JobLoc.checkbox_no_exp)).to_be_checked()

    async def no_exp_uncheck(self):
        await self._click(JobLoc.checkbox_no_exp)
        await expect(self._find(JobLoc.checkbox_no_exp)).not_to_be_checked()

    async def year_01_presence(self):
        await self._look(JobLoc.checkbox_01_yr)
        await expect(self._find(JobLoc.checkbox_01_yr)).to_be_visible()

    async def year_01_check(self):
        await self._touch(JobLoc.checkbox_01_yr)
        await self._find(JobLoc.checkbox_01_yr).check()
        await expect(self._find(JobLoc.checkbox_01_yr)).to_be_checked()

    async def year_01_uncheck(self):
        await self._click(JobLoc.checkbox_01_yr)
        await expect(self._find(JobLoc.checkbox_01_yr)).not_to_be_checked()

    async def year_02_presence(self):
        await self._look(JobLoc.checkbox_02_yr)
        await expect(self._find(JobLoc.checkbox_02_yr)).to_be_visible()

    async def year_02_check(self):
        await self._touch(JobLoc.checkbox_02_yr)
        await self._find(JobLoc.checkbox_02_yr).check()
        await expect(self._find(JobLoc.checkbox_02_yr)).to_be_checked()

    async def year_02_uncheck(self):
        await self._click(JobLoc.checkbox_02_yr)
        await expect(self._find(JobLoc.checkbox_02_yr)).not_to_be_checked()

    async def year_03_presence(self):
        await self._look(JobLoc.checkbox_03_yr)
        await expect(self._find(JobLoc.checkbox_03_yr)).to_be_visible()

    async def year_03_check(self):
        await self._touch(JobLoc.checkbox_03_yr)
        await self._find(JobLoc.checkbox_03_yr).check()
        await expect(self._find(JobLoc.checkbox_03_yr)).to_be_checked()

    async def year_03_uncheck(self):
        await self._click(JobLoc.checkbox_03_yr)
        await expect(self._find(JobLoc.checkbox_03_yr)).not_to_be_checked()

    async def year_04_presence(self):
        await self._look(JobLoc.checkbox_04_yr)
        await expect(self._find(JobLoc.checkbox_04_yr)).to_be_visible()

    async def year_04_check(self):
        await self._touch(JobLoc.checkbox_04_yr)
        await self._find(JobLoc.checkbox_04_yr).check()
        await expect(self._find(JobLoc.checkbox_04_yr)).to_be_checked()

    async def year_04_uncheck(self):
        await self._click(JobLoc.checkbox_04_yr)
        await expect(self._find(JobLoc.checkbox_04_yr)).not_to_be_checked()

    """Pagination Section"""

    async def prev_chevron_presence(self):
        await self._look(JobLoc.page_previous)
        await expect(self._find(JobLoc.page_previous)).to_be_visible()

    async def prev_chevron_click(self):
        await self._click(JobLoc.page_previous)
        await expect(self._find(JobLoc.page_previous)).to_be_focused()

    async def next_chevron_presence(self):
        await self._look(JobLoc.page_next)
        await expect(self._find(JobLoc.page_next)).to_be_visible()

    async def next_chevron_click(self):
        await self._click(JobLoc.page_next)
        await expect(self._find(JobLoc.page_next)).to_be_focused()

    async def page_number_count(self):
        print(f"Total Pages: {self._find(JobLoc.page_container).count()}")

    async def page_number_presence(self):
        await self._look(JobLoc.page_container)
        await expect(self._find(JobLoc.page_container)).to_be_visible()

