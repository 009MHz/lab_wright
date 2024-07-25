from pages.__base import BasePage
from elements.__job import JobLoc
from playwright.sync_api import Page, expect


class JobPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_page(self):
        self.page.goto(JobLoc.url)

    """Job List Sorting Control"""
    def sort_control_presence(self):
        self._look(JobLoc.sort_control)
        expect(self._find(JobLoc.sort_control)).to_be_visible()

    def sort_control_click(self):
        self._click(JobLoc.sort_control)

    def sort_item_presence(self):
        for item in JobLoc.sort_options:
            self._look(JobLoc.sort_control_expanded)
            expect(self._find(JobLoc.sort_control_expanded)).to_be_visible()

            self._look(JobLoc.sort_options[item])
            expect(self._find(JobLoc.sort_options[item])).to_be_visible()
            self._click(JobLoc.sort_options[item])
            self.sort_control_click()

    """Job List Main Button Filter"""
    def click_easy_apply(self):
        self._click(JobLoc.btn_easy_apply)
        expect(self._find(JobLoc.btn_easy_apply)).to_be_focused()

    def click_msib(self):
        self._click(JobLoc.btn_MSIB)
        expect(self._find(JobLoc.btn_MSIB)).to_be_focused()

    def click_clear(self):
        self._click(JobLoc.btn_clear)
        expect(self._find(JobLoc.btn_clear)).to_be_focused()

    def click_apply(self):
        self._click(JobLoc.btn_apply)
        expect(self._find(JobLoc.btn_apply)).to_be_focused()

    """Job List Carousel"""
    def _card_component(self, locator, component_name, index):
        locator = f"({locator})[{index}]"
        self.page.wait_for_selector(locator, state='visible')
        expect(self._find(locator)).to_be_visible(timeout=3000), f"{component_name} is not visible for card {index}"

    def job_cards_logo_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_logo, 'logo', index)

    def job_cards_company_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_company_name, 'company', index)

    def job_cards_title_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_title, 'title', index)

    def job_cards_location_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_location, 'location', index)

    def job_cards_description_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_description, 'description', index)

    def job_cards_industry_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_industry, 'industry', index)

    def job_cards_type_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_type, 'type', index)

    def check_job_cards_daycount(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_daycount, 'daycount', index)

    def job_cards_easyapply_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            if not self._find(f"({JobLoc.body_job_easy_apply})[{index}]").is_visible():
                print(f"easyapply button doesn't apply for card {index}")
                continue
            self._card_component(JobLoc.body_job_easy_apply, 'easyapply', index)

    def job_cards_msib_presence(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            if not self._find(f"({JobLoc.body_job_msib})[{index}]").is_visible():
                print(f"msib button doesn't apply for card {index}")
                continue
            self._card_component(JobLoc.body_job_msib, 'msib', index)

    def position_input_presence(self):
        self._touch(JobLoc.box_position_input)
        expect(self._find(JobLoc.box_position_input)).to_be_visible()

        self._click(JobLoc.box_position_input)
        expect(self._find(JobLoc.box_position_input)).to_be_focused()

    """Filter Input Field Search"""
    def position_input_type(self, text: str):
        self._type(JobLoc.box_position_input, text)
        expect(self._find(JobLoc.box_position_input)).not_to_be_empty()

    def position_input_clear(self):
        self._look(JobLoc.box_position_clear)
        self._click(JobLoc.box_position_clear)
        expect(self._find(JobLoc.box_position_input)).to_be_empty()

    def company_input_presence(self):
        self._touch(JobLoc.box_company_input)
        expect(self._find(JobLoc.box_company_input)).to_be_visible()

        self._click(JobLoc.box_company_input)
        expect(self._find(JobLoc.box_company_input)).to_be_focused()

    def company_input_type(self, text: str):
        self._type(JobLoc.box_company_input, text)
        expect(self._find(JobLoc.box_company_input)).not_to_be_empty()

    def company_input_clear(self):
        self._look(JobLoc.box_company_clear)
        self._click(JobLoc.box_company_clear)
        expect(self._find(JobLoc.box_company_input)).to_be_empty()

    def industri_input_presence(self):
        self._touch(JobLoc.box_industri_input)
        expect(self._find(JobLoc.box_industri_input)).to_be_visible()

        self._click(JobLoc.box_industri_input)
        expect(self._find(JobLoc.box_industri_input)).to_be_focused()

    def industri_input_type(self, text: str):
        self._type(JobLoc.box_industri_input, text)
        expect(self._find(JobLoc.box_industri_input)).not_to_be_empty()

    def industri_input_clear(self):
        self._force(JobLoc.box_industri_clear)
        self._click(JobLoc.box_industri_clear)
        expect(self._find(JobLoc.box_industri_input)).to_be_empty()

    def lokasi_input_presence(self):
        self._touch(JobLoc.box_lokasi_input)
        expect(self._find(JobLoc.box_lokasi_input)).to_be_visible()

        self._click(JobLoc.box_lokasi_input)
        expect(self._find(JobLoc.box_lokasi_input)).to_be_focused()

    def lokasi_input_type(self, text: str):
        self._type(JobLoc.box_lokasi_input, text)
        expect(self._find(JobLoc.box_lokasi_input)).not_to_be_empty()

    def lokasi_input_clear(self):
        self._force(JobLoc.box_lokasi_clear)
        self._click(JobLoc.box_lokasi_clear)
        expect(self._find(JobLoc.box_lokasi_input)).to_be_empty()

    def skill_input_presence(self):
        self._touch(JobLoc.box_skill_input)
        expect(self._find(JobLoc.box_skill_input)).to_be_visible()

        self._click(JobLoc.box_skill_input)
        expect(self._find(JobLoc.box_skill_input)).to_be_focused()

    def skill_input_type(self, text: str):
        self._type(JobLoc.box_skill_input, text)
        expect(self._find(JobLoc.box_skill_input)).not_to_be_empty()

    def skill_input_clear(self):
        self._force(JobLoc.box_skill_clear)
        self._click(JobLoc.box_skill_clear)
        expect(self._find(JobLoc.box_skill_input)).to_be_empty()

    """Tipe Pekerjaan Checkboxes Section"""
    def full_time_presence(self):
        self._look(JobLoc.checkbox_full)
        expect(self._find(JobLoc.checkbox_full)).to_be_visible()

    def full_time_check(self):
        self._touch(JobLoc.checkbox_full)
        self._find(JobLoc.checkbox_full).check()
        expect(self._find(JobLoc.checkbox_full)).to_be_checked()

    def full_time_uncheck(self):
        self._touch(JobLoc.checkbox_full)
        self._click(JobLoc.checkbox_full)
        expect(self._find(JobLoc.checkbox_full)).not_to_be_checked()

    def part_time_presence(self):
        self._look(JobLoc.checkbox_part)
        expect(self._find(JobLoc.checkbox_part)).to_be_visible()

    def part_time_check(self):
        self._touch(JobLoc.checkbox_part)
        self._find(JobLoc.checkbox_part).check()
        expect(self._find(JobLoc.checkbox_part)).to_be_checked()

    def part_time_uncheck(self):
        self._touch(JobLoc.checkbox_part)
        self._click(JobLoc.checkbox_part)
        expect(self._find(JobLoc.checkbox_part)).not_to_be_checked()

    def intern_presence(self):
        self._look(JobLoc.checkbox_intern)
        expect(self._find(JobLoc.checkbox_intern)).to_be_visible()

    def intern_check(self):
        self._touch(JobLoc.checkbox_intern)
        self._find(JobLoc.checkbox_intern).check()
        expect(self._find(JobLoc.checkbox_intern)).to_be_checked()

    def intern_uncheck(self):
        self._touch(JobLoc.checkbox_intern)
        self._click(JobLoc.checkbox_intern)
        expect(self._find(JobLoc.checkbox_intern)).not_to_be_checked()

    def volunteer_presence(self):
        self._look(JobLoc.checkbox_volunteer)
        expect(self._find(JobLoc.checkbox_volunteer)).to_be_visible()

    def volunteer_check(self):
        self._touch(JobLoc.checkbox_volunteer)
        self._find(JobLoc.checkbox_volunteer).check()
        expect(self._find(JobLoc.checkbox_volunteer)).to_be_checked()

    def volunteer_uncheck(self):
        self._touch(JobLoc.checkbox_volunteer)
        self._click(JobLoc.checkbox_volunteer)
        expect(self._find(JobLoc.checkbox_volunteer)).not_to_be_checked()

    def contract_presence(self):
        self._look(JobLoc.checkbox_contract)
        expect(self._find(JobLoc.checkbox_contract)).to_be_visible()

    def contract_check(self):
        self._touch(JobLoc.checkbox_contract)
        self._find(JobLoc.checkbox_contract).check()
        expect(self._find(JobLoc.checkbox_contract)).to_be_checked()

    def contract_uncheck(self):
        self._touch(JobLoc.checkbox_contract)
        self._click(JobLoc.checkbox_contract)
        expect(self._find(JobLoc.checkbox_contract)).not_to_be_checked()

    def scholar_presence(self):
        self._look(JobLoc.checkbox_scholar)
        expect(self._find(JobLoc.checkbox_scholar)).to_be_visible()

    def scholar_check(self):
        self._touch(JobLoc.checkbox_scholar)
        self._find(JobLoc.checkbox_scholar).check()
        expect(self._find(JobLoc.checkbox_scholar)).to_be_checked()

    def scholar_uncheck(self):
        self._touch(JobLoc.checkbox_scholar)
        self._click(JobLoc.checkbox_scholar)
        expect(self._find(JobLoc.checkbox_scholar)).not_to_be_checked()

    def partner_presence(self):
        self._look(JobLoc.checkbox_partner)
        expect(self._find(JobLoc.checkbox_partner)).to_be_visible()

    def partner_check(self):
        self._touch(JobLoc.checkbox_partner)
        self._find(JobLoc.checkbox_partner).check()
        expect(self._find(JobLoc.checkbox_partner)).to_be_checked()

    def partner_uncheck(self):
        self._touch(JobLoc.checkbox_partner)
        self._click(JobLoc.checkbox_partner)
        expect(self._find(JobLoc.checkbox_partner)).not_to_be_checked()

    """Tipe Pengaturan Kerja Section"""
    def hybrid_presence(self):
        self._look(JobLoc.checkbox_hybrid)
        expect(self._find(JobLoc.checkbox_hybrid)).to_be_visible()

    def hybrid_check(self):
        self._touch(JobLoc.checkbox_hybrid)
        self._find(JobLoc.checkbox_hybrid).check()
        expect(self._find(JobLoc.checkbox_hybrid)).to_be_checked()

    def hybrid_uncheck(self):
        self._touch(JobLoc.checkbox_hybrid)
        self._click(JobLoc.checkbox_hybrid)
        expect(self._find(JobLoc.checkbox_hybrid)).not_to_be_checked()
        
    def on_site_presence(self):
        self._look(JobLoc.checkbox_on_site)
        expect(self._find(JobLoc.checkbox_on_site)).to_be_visible()

    def on_site_check(self):
        self._touch(JobLoc.checkbox_on_site)
        self._find(JobLoc.checkbox_on_site).check()
        expect(self._find(JobLoc.checkbox_on_site)).to_be_checked()

    def on_site_uncheck(self):
        self._touch(JobLoc.checkbox_on_site)
        self._click(JobLoc.checkbox_on_site)
        expect(self._find(JobLoc.checkbox_on_site)).not_to_be_checked()
        
    def remote_presence(self):
        self._look(JobLoc.checkbox_remote)
        expect(self._find(JobLoc.checkbox_remote)).to_be_visible()

    def remote_check(self):
        self._touch(JobLoc.checkbox_remote)
        self._find(JobLoc.checkbox_remote).check()
        expect(self._find(JobLoc.checkbox_remote)).to_be_checked()

    def remote_uncheck(self):
        self._touch(JobLoc.checkbox_remote)
        self._click(JobLoc.checkbox_remote)
        expect(self._find(JobLoc.checkbox_remote)).not_to_be_checked()

    """Pengalaman Kerja Section"""
    def no_exp_presence(self):
        self._look(JobLoc.checkbox_no_exp)
        expect(self._find(JobLoc.checkbox_no_exp)).to_be_visible()

    def no_exp_check(self):
        self._touch(JobLoc.checkbox_no_exp)
        self._find(JobLoc.checkbox_no_exp).check()
        expect(self._find(JobLoc.checkbox_no_exp)).to_be_checked()

    def no_exp_uncheck(self):
        self._touch(JobLoc.checkbox_no_exp)
        self._click(JobLoc.checkbox_no_exp)
        expect(self._find(JobLoc.checkbox_no_exp)).not_to_be_checked()

    def year_01_presence(self):
        self._look(JobLoc.checkbox_01_yr)
        expect(self._find(JobLoc.checkbox_01_yr)).to_be_visible()

    def year_01_check(self):
        self._touch(JobLoc.checkbox_01_yr)
        self._find(JobLoc.checkbox_01_yr).check()
        expect(self._find(JobLoc.checkbox_01_yr)).to_be_checked()

    def year_01_uncheck(self):
        self._touch(JobLoc.checkbox_01_yr)
        self._click(JobLoc.checkbox_01_yr)
        expect(self._find(JobLoc.checkbox_01_yr)).not_to_be_checked()

    def year_02_presence(self):
        self._look(JobLoc.checkbox_02_yr)
        expect(self._find(JobLoc.checkbox_02_yr)).to_be_visible()

    def year_02_check(self):
        self._touch(JobLoc.checkbox_02_yr)
        self._find(JobLoc.checkbox_02_yr).check()
        expect(self._find(JobLoc.checkbox_02_yr)).to_be_checked()

    def year_02_uncheck(self):
        self._touch(JobLoc.checkbox_02_yr)
        self._click(JobLoc.checkbox_02_yr)
        expect(self._find(JobLoc.checkbox_02_yr)).not_to_be_checked()

    def year_03_presence(self):
        self._look(JobLoc.checkbox_03_yr)
        expect(self._find(JobLoc.checkbox_03_yr)).to_be_visible()

    def year_03_check(self):
        self._touch(JobLoc.checkbox_03_yr)
        self._find(JobLoc.checkbox_03_yr).check()
        expect(self._find(JobLoc.checkbox_03_yr)).to_be_checked()

    def year_03_uncheck(self):
        self._touch(JobLoc.checkbox_03_yr)
        self._click(JobLoc.checkbox_03_yr)
        expect(self._find(JobLoc.checkbox_03_yr)).not_to_be_checked()

    def year_04_presence(self):
        self._look(JobLoc.checkbox_04_yr)
        expect(self._find(JobLoc.checkbox_04_yr)).to_be_visible()

    def year_04_check(self):
        self._touch(JobLoc.checkbox_04_yr)
        self._find(JobLoc.checkbox_04_yr).check()
        expect(self._find(JobLoc.checkbox_04_yr)).to_be_checked()

    def year_04_uncheck(self):
        self._touch(JobLoc.checkbox_04_yr)
        self._click(JobLoc.checkbox_04_yr)
        expect(self._find(JobLoc.checkbox_04_yr)).not_to_be_checked()

