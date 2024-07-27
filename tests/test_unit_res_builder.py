import pytest
from pages.res_builder_page import Builder
import allure


@pytest.fixture(scope='function')
def builder(page):
    builder = Builder(page)
    return builder


@allure.epic("Resume Builder Page")
@allure.story("Resume Builder Header Component")
class TestSmokeLoginPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("")
    @allure.feature("Login", "Email", "Google")
    def test_main_header_info(self):
        pass
