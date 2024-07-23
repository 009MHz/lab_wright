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

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Main Job Card Validation")
    def test_job_cards(self, page):
        with allure.step("1. Navigate to the Job page"):
            job_page = JobPage(page)
            job_page.open_job_page()
        with allure.step("2. Check the each job cards element availability"):
            job_page.check_job_cards_logo()
            job_page.check_job_cards_company()
            job_page.check_job_cards_title()
            job_page.check_job_cards_location()
            job_page.check_job_cards_industry()
            job_page.check_job_cards_type()
            job_page.check_job_cards_daycount()
            job_page.check_job_cards_easyapply()
            job_page.check_job_cards_msib()

