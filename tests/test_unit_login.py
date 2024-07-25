import pytest
from pages.login_page import LoginPage
import allure


@pytest.fixture(scope='function')
def login(page):
    login = LoginPage(page)
    login.open_login_page()
    return login


@allure.epic("Login Page")
@allure.story("Login Page Smoke Test")
class TestSmokeLoginPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Main Login Page Validation")
    @allure.feature("Login, Email, Google")
    def test_login_init(self, login):
        with allure.step("1. Verify the login init page components"):
            login.main_title_presence()
            login.email_field_presence()
            login.next_button_presence()
            login.google_button_presence()

