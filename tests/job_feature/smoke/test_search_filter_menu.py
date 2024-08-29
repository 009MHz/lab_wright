import pytest
from pages.job.job_page import JobPage
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def job_page(page):
    job_page = JobPage(page)
    await job_page.open_page()
    return job_page


@allure.epic("Job")
@allure.story("Smoke Testing: Job Page")
@allure.feature("Job/ Filter")
@pytest.mark.job_filter
class TestSmokeJobPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.tag("Direct Filter")
    @allure.feature("Job/ Filter/ Easy Apply", "Job/ Filter/ MSIB")
    @allure.title("Main Filter button Validation")
    @allure.severity(severity.CRITICAL)
    async def test_main_filter(self, job_page):
        with allure.step("1. Interact with Main Filter"):
            await job_page.click_easy_apply()
            await job_page.click_msib()
            await job_page.click_clear()
            await job_page.click_apply()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.auto_complete
    @pytest.mark.input_field
    @allure.feature("Job/ Filter/ Posisi", "Job/ Filter/ Nama Perusahaan", "Job/ Filter/ Industri", 
                    "Job/ Filter/ Lokasi", "Job/ Filter/ Kemampuan")
    @allure.title("Input Field Search Validation")
    @allure.severity(severity.CRITICAL)
    async def test_input_search(self, job_page):
        with allure.step("1. Check each input field availability"):
            await job_page.position_input_presence()
            await job_page.company_input_presence()
            await job_page.industry_input_presence()
            await job_page.location_input_presence()
            await job_page.skill_input_presence()
        with allure.step("2. Insert text on each input field"):
            await job_page.position_input_type("Written from playwright, on Posisi field")
            await job_page.company_input_type("Written from playwright, on Company field")
            await job_page.industry_input_type("Written from playwright, on Industri field")
            await job_page.location_input_type("Written from playwright, on Lokasi field")
            await job_page.skill_input_type("Written from playwright, on Kemampuan field")
        with allure.step("3. Clear the text from each input field"):
            await job_page.position_input_clear()
            await job_page.company_input_clear()
            await job_page.industry_input_clear()
            await job_page.location_input_clear()
            await job_page.skill_input_clear()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.checkbox
    @allure.feature("Job/ Filter/ Tipe Pekerjaan")
    @allure.title("'Tipe Pekerjaan' Check Validation")
    @allure.severity(severity.CRITICAL)
    async def test_job_type_checkboxes(self, job_page):
        with allure.step("1. Check each Tipe Pekerjaan Checkbox availability"):
            await job_page.full_time_presence()
            await job_page.part_time_presence()
            await job_page.internship_presence()
            await job_page.volunteer_presence()
            await job_page.contract_presence()
            await job_page.scholarship_presence()
            await job_page.partnership_presence()
        with allure.step("2. Click on each checkboxes"):
            await job_page.full_time_check()
            await job_page.part_time_check()
            await job_page.internship_check()
            await job_page.volunteer_check()
            await job_page.contract_check()
            await job_page.scholarship_check()
            await job_page.partnership_check()
        with allure.step("3. Uncheck all checkboxes"):
            await job_page.full_time_uncheck()
            await job_page.part_time_uncheck()
            await job_page.internship_uncheck()
            await job_page.volunteer_uncheck()
            await job_page.contract_uncheck()
            await job_page.scholarship_uncheck()
            await job_page.partnership_uncheck()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.checkbox
    @allure.feature("Job/ Filter/ Tipe Pengaturan Kerja")
    @allure.title("'Tipe Pengaturan Kerja' Check Validation")
    @allure.severity(severity.CRITICAL)
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
    @pytest.mark.checkbox
    @allure.feature("Job/ Filter/ Pengalaman Kerja")
    @allure.title("'Pengalaman Kerja' Check Validation")
    @allure.severity(severity.CRITICAL)
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
