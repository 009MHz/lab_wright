import pytest
from pages.job_page import JobPage
import allure


@allure.epic("Job Page")
@allure.story("Job Page Smoke Test")
class TestJobPageSmoke:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Sorting Control Test Validation")
    @allure.feature("Sort")
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
    @allure.feature("Filter", "Main", "Easy Apply", "MSIB")
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
    @allure.feature("Carousel", "Job Card")
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
    @allure.feature("Filter", "Auto Complete", "Input")
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

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Filter", "Checkbox")
    @allure.title("'Tipe Pekerjaan' Check Validation")
    def test_tipe_pekerjaan_checkboxes(self, page):
        with allure.step("1. Navigate to the Job page"):
            job_page = JobPage(page)
            job_page.open_job_page()
        with allure.step("2. Check each Tipe Pekerjaan Checkbox availability"):
            job_page.full_time_presence()
            job_page.part_time_presence()
            job_page.intern_presence()
            job_page.volunteer_presence()
            job_page.contract_presence()
            job_page.scholar_presence()
            job_page.partner_presence()
        with allure.step("3. Click on each checkboxes"):
            job_page.full_time_check()
            job_page.part_time_check()
            job_page.intern_check()
            job_page.volunteer_check()
            job_page.contract_check()
            job_page.scholar_check()
            job_page.partner_check()
        with allure.step("4. Uncheck all checkboxes"):
            job_page.full_time_uncheck()
            job_page.part_time_uncheck()
            job_page.intern_uncheck()
            job_page.volunteer_uncheck()
            job_page.contract_uncheck()
            job_page.scholar_uncheck()
            job_page.partner_uncheck()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Filter", "Checkbox")
    @allure.title("'Tipe Pengaturan Kerja' Check Validation")
    def test_arrangement_checkboxes(self, page):
        with allure.step("1. Navigate to the Job page"):
            job_page = JobPage(page)
            job_page.open_job_page()
        with allure.step("2. Check each Tipe Pengaturan KErja Checkbox availability"):
            job_page.hybrid_presence()
            job_page.on_site_presence()
            job_page.remote_presence()
        with allure.step("3. Click on each checkboxes"):
            job_page.hybrid_check()
            job_page.on_site_check()
            job_page.remote_check()
        with allure.step("4. Uncheck all checkboxes"):
            job_page.hybrid_uncheck()
            job_page.on_site_uncheck()
            job_page.remote_uncheck()
