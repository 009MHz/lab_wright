from pages.__base import BasePage
from elements.__job import JobLoc
from playwright.sync_api import Page, expect
import json


class JobPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_job_page(self):
        self.page.goto(JobLoc.url)

    def sort_control_check(self):
        self._look(JobLoc.sort_control)
        expect(self._find(JobLoc.sort_control)).to_be_visible()

    def sort_control_click(self):
        self._click(JobLoc.sort_control)

    def sort_item_check(self):
        for item in JobLoc.sort_options:
            self._look(JobLoc.sort_control_expanded)
            expect(self._find(JobLoc.sort_control_expanded)).to_be_visible()

            self._look(JobLoc.sort_options[item])
            expect(self._find(JobLoc.sort_options[item])).to_be_visible()
            self._click(JobLoc.sort_options[item])
            self.sort_control_click()

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

    def _card_component(self, locator, component_name, index):
        locator = f"({locator})[{index}]"
        self.page.wait_for_selector(locator, state='visible')
        expect(self._find(locator)).to_be_visible(timeout=3000), f"{component_name} is not visible for card {index}"

    def check_job_cards_logo(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_logo, 'logo', index)

    def check_job_cards_company(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_company_name, 'company', index)

    def check_job_cards_title(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_title, 'title', index)

    def check_job_cards_location(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_location, 'location', index)

    def check_job_cards_description(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_description, 'description', index)

    def check_job_cards_industry(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_industry, 'industry', index)

    def check_job_cards_type(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_type, 'type', index)

    def check_job_cards_daycount(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            self._card_component(JobLoc.body_job_daycount, 'daycount', index)

    def check_job_cards_easyapply(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            if not self._find(f"({JobLoc.body_job_easy_apply})[{index}]").is_visible():
                print(f"easyapply button doesn't apply for card {index}")
                continue
            self._card_component(JobLoc.body_job_easy_apply, 'easyapply', index)

    def check_job_cards_msib(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()
        for index in range(1, total_cards + 1):
            if not self._find(f"({JobLoc.body_job_msib})[{index}]").is_visible():
                print(f"msib button doesn't apply for card {index}")
                continue
            self._card_component(JobLoc.body_job_msib, 'msib', index)