import pytest
from pages.job_page import JobPage
import allure


@allure.feature("Job Page")
@allure.story("Job Page Smoke Test")
class TestJobPageSmoke:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Sorting Control Test Validation")
    def test_sort_control(self, page):
        with allure.step("1. Navigate to the Job page"):
            job_page = JobPage(page)
            job_page.open_job_page()
        with allure.step("2. Interact & validate the sort control"):
            job_page.sort_control_check()
            job_page.sort_control_click()
            job_page.sort_item_check()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Main Filter button Validation")
    def test_main_filter(self, page):
        with allure.step("1. Navigate to the Job page"):
            job_page = JobPage(page)
            job_page.open_job_page()
        with allure.step("2. Interact with Main Filter"):
            job_page.click_easy_apply()
            job_page.click_msib()
            job_page.click_clear()
            job_page.click_apply()

