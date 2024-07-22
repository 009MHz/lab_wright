from pages.__base import BasePage
from elements.__job import JobLoc
from playwright.sync_api import Page, expect


class JobPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_job_page(self):
        self.page.goto(JobLoc.url)

    def sort_control_check(self):
        self._view(JobLoc.sort_control)
        return self._find(JobLoc.sort_control).is_visible()

    def sort_control_click(self):
        self._click(JobLoc.sort_control)

    def sort_item_check(self):
        for item in JobLoc.sort_options:
            self._view(JobLoc.sort_control_expanded)
            self._view(JobLoc.sort_options[item])
            if not self._find(JobLoc.sort_options[item]).is_visible():
                return False
            self._click(JobLoc.sort_options[item])
            self.sort_control_click()
        return True

    def click_easy_apply(self):
        self._click(JobLoc.btn_easy_apply)

    def easy_apply_selected(self):
        self._interacted(JobLoc.btn_easy_apply)

    def click_msib(self):
        self._click(JobLoc.btn_MSIB)

    def msib_selected(self):
        self._interacted(JobLoc.btn_MSIB)
