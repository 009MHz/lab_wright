import pytest
from pages.job_page import JobPage
import allure

@allure.feature("Job Page")
@allure.story("Job Page Smoke Test")
class TestJobPageSmoke:
    @pytest.mark.ui
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Sorting Control Test Validation")
    def test_sort_control(self, page):
        with allure.step("1. Navigate to the Job page"):
            job_page = JobPage(page)
            job_page.open_job_page()
        with allure.step("2. Interact & validate the sort control"):
            assert job_page.sort_control_check(), "Sort Control Doesn't Exist"
            assert job_page.sort_item_check(), "One or more Sort Options were not visible"
