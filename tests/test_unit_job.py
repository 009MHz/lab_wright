import pytest
from pages.job_page import JobPage
import allure


@pytest.fixture(scope='function')
async def job_page(page):
    job_page = JobPage(page)
    await job_page.open_page()
    return job_page


@allure.epic("Job Page")
@allure.story("Job Page Smoke Test")
class TestSmokeJobPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Sorting Control Test Validation")
    @allure.feature("Sort")
    async def test_sort_control(self, job_page):
        with allure.step("1. Interact & validate the sort control"):
            await job_page.sort_control_presence()
            await job_page.sort_control_click()
            await job_page.sort_item_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Filter", "Main", "Easy Apply", "MSIB")
    @allure.title("Main Filter button Validation")
    async def test_main_filter(self, job_page):
        with allure.step("1. Interact with Main Filter"):
            await job_page.click_easy_apply()
            await job_page.click_msib()
            await job_page.click_clear()
            await job_page.click_apply()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Carousel", "Job Card")
    @allure.title("Main Job Card Validation")
    async def test_job_cards(self, job_page):
        with allure.step("1. Check each job cards element availability"):
            await job_page.job_cards_logo_presence()
            await job_page.job_cards_company_presence()
            await job_page.job_cards_title_presence()
            await job_page.job_cards_location_presence()
            await job_page.job_cards_industry_presence()
            await job_page.job_cards_type_presence()
            await job_page.check_job_cards_daycount()
            await job_page.job_cards_easyapply_presence()
            await job_page.job_cards_msib_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Filter", "Auto Complete", "Input")
    @allure.title("Input Field Search Validation")
    async def test_input_search(self, job_page):
        with allure.step("1. Check each input field availability"):
            await job_page.position_input_presence()
            await job_page.company_input_presence()
            await job_page.industri_input_presence()
            await job_page.lokasi_input_presence()
            await job_page.skill_input_presence()
        with allure.step("2. Insert text on each input field"):
            await job_page.position_input_type("Written from playwright, on Posisi field")
            await job_page.company_input_type("Written from playwright, on Company field")
            await job_page.industri_input_type("Written from playwright, on Industri field")
            await job_page.lokasi_input_type("Written from playwright, on Lokasi field")
            await job_page.skill_input_type("Written from playwright, on Kemampuan field")
        with allure.step("3. Clear the text from each input field"):
            await job_page.position_input_clear()
            await job_page.company_input_clear()
            await job_page.industri_input_clear()
            await job_page.lokasi_input_clear()
            await job_page.skill_input_clear()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Filter", "Checkbox")
    @allure.title("'Tipe Pekerjaan' Check Validation")
    async def test_job_type_checkboxes(self, job_page):
        with allure.step("1. Check each Tipe Pekerjaan Checkbox availability"):
            await job_page.full_time_presence()
            await job_page.part_time_presence()
            await job_page.intern_presence()
            await job_page.volunteer_presence()
            await job_page.contract_presence()
            await job_page.scholar_presence()
            await job_page.partner_presence()
        with allure.step("2. Click on each checkboxes"):
            await job_page.full_time_check()
            await job_page.part_time_check()
            await job_page.intern_check()
            await job_page.volunteer_check()
            await job_page.contract_check()
            await job_page.scholar_check()
            await job_page.partner_check()
        with allure.step("3. Uncheck all checkboxes"):
            await job_page.full_time_uncheck()
            await job_page.part_time_uncheck()
            await job_page.intern_uncheck()
            await job_page.volunteer_uncheck()
            await job_page.contract_uncheck()
            await job_page.scholar_uncheck()
            await job_page.partner_uncheck()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Filter", "Checkbox")
    @allure.title("'Tipe Pengaturan Kerja' Check Validation")
    async def test_arrangement_checkboxes(self, job_page):
        with allure.step("1. Check each Tipe Pengaturan Kerja Checkbox availability"):
            await job_page.hybrid_presence()
            await job_page.on_site_presence()
            await job_page.remote_presence()
        with allure.step("2. Click on each checkboxes"):
            await job_page.hybrid_check()
            await job_page.on_site_check()
            await job_page.remote_check()
        with allure.step("3. Uncheck all checkboxes"):
            await job_page.hybrid_uncheck()
            await job_page.on_site_uncheck()
            await job_page.remote_uncheck()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Filter", "Checkbox")
    @allure.title("'Pengalaman Kerja' Check Validation")
    async def test_experience_checkboxes(self, job_page):
        with allure.step("1. Check each Pengalaman Kerja Checkbox availability"):
            await job_page.no_exp_presence()
            await job_page.year_01_presence()
            await job_page.year_02_presence()
            await job_page.year_03_presence()
            await job_page.year_04_presence()
        with allure.step("2. Click on each checkboxes"):
            await job_page.no_exp_check()
            await job_page.year_01_check()
            await job_page.year_02_check()
            await job_page.year_03_check()
            await job_page.year_04_check()
        with allure.step("3. Uncheck all checkboxes"):
            await job_page.no_exp_uncheck()
            await job_page.year_01_uncheck()
            await job_page.year_02_uncheck()
            await job_page.year_03_uncheck()
            await job_page.year_04_uncheck()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Pagination")
    @allure.title("Pagination Section Validation")
    async def test_pagination(self, job_page):
        with allure.step("1. The Pagination Component should be exist"):
            await job_page.next_chevron_presence()
            await job_page.prev_chevron_presence()
            await job_page.page_number_presence()
        with allure.step("2. Click on Pagination Chevron"):
            await job_page.next_chevron_click()
            await job_page.next_chevron_click()
            await job_page.prev_chevron_click()
