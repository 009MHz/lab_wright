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
            job_page.sort_control_presence()
            job_page.sort_control_click()
            job_page.sort_item_presence()

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
            job_page.job_cards_logo_presence()
            job_page.job_cards_company_presence()
            job_page.job_cards_title_presence()
            job_page.job_cards_location_presence()
            job_page.job_cards_industry_presence()
            job_page.job_cards_type_presence()
            job_page.check_job_cards_daycount()
            job_page.job_cards_easyapply_presence()
            job_page.job_cards_msib_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Input Field Search Validation")
    def test_input_search(self, page):
        with allure.step("1. Navigate to the Job page"):
            job_page = JobPage(page)
            job_page.open_job_page()
        with allure.step("2. Check each input field availability"):
            job_page.position_input_presence()
            job_page.company_input_presence()
            job_page.industri_input_presence()
            job_page.lokasi_input_presence()
            job_page.skill_input_presence()
        with allure.step("3. Insert text on the each input field"):
            job_page.position_input_type("Written from playwright, on Posisi field")
            job_page.company_input_type("Written from playwright, on Company field")
            job_page.industri_input_type("Written from playwright, on Industri field")
            job_page.lokasi_input_type("Written from playwright, on Lokasi field")
            job_page.skill_input_type("Written from playwright, on Kemampuan field")
        with allure.step("3. Clear the text from each input field"):
            job_page.position_input_clear()
            job_page.company_input_clear()
            job_page.industri_input_clear()
            job_page.lokasi_input_clear()
            job_page.skill_input_clear()
