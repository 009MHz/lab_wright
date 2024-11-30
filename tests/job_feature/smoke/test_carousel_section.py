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
@allure.feature("Job/ Carousel")
@pytest.mark.job_card
class TestSmokeJobPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.sort_control
    @allure.title("Sorting Control Test Validation")
    @allure.feature("Job/ Carousel/ Sort")
    @allure.severity(severity.NORMAL)
    async def test_sort_control(self, job_page):
        with allure.step("1. Interact & validate the sort control"):
            await job_page.sort_control_presence()
            await job_page.sort_control_click()
            await job_page.sort_item_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.feature("Job/ Carousel/ Job Card")
    @allure.title("Main Job Card Validation")
    @allure.severity(severity.NORMAL)
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
    @pytest.mark.pagination
    @pytest.mark.skip
    @allure.feature("Job/ Carousel/ Pagination")
    @allure.title("Pagination Section Validation")
    @allure.severity(severity.NORMAL)
    async def test_pagination(self, job_page):
        with allure.step("1. The Pagination Component should be exist"):
            await job_page.next_chevron_presence()
            await job_page.prev_chevron_presence()
            await job_page.page_number_presence()
        with allure.step("2. Click on Pagination Chevron"):
            await job_page.next_chevron_click()
            await job_page.prev_chevron_click()
