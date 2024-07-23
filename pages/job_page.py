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

    def check_job_cards(self):
        self._look(JobLoc.body_cards)
        total_cards = self._find(JobLoc.body_cards).count()

        for index in range(1, total_cards + 1):
            locators = {
                "logo": f"({JobLoc.body_logo})[{index}]",
                "company": f"({JobLoc.body_company_name})[{index}]",
                "title": f"({JobLoc.body_job_title})[{index}]",
                "location": f"({JobLoc.body_job_location})[{index}]",
                "description": f"({JobLoc.body_job_description})[{index}]",
                "industry": f"({JobLoc.body_job_industry})[{index}]",
                "type": f"({JobLoc.body_job_type})[{index}]",
                "daycount": f"({JobLoc.body_job_daycount})[{index}]",
                "easyapply": f"({JobLoc.body_job_easy_apply})[{index}]",
                "msib": f"({JobLoc.body_job_msib})[{index}]",
            }

            for key, locator in locators.items():
                if key in ["easyapply", "msib"]:
                    if not self.page.locator(locator).is_visible():
                        print(f"{key} button doesn't applied for card {index}")
                        continue

                self.page.wait_for_selector(locator, state='visible')
                assert self.page.locator(locator).is_visible(), f"{key} is not visible for card {index}"
