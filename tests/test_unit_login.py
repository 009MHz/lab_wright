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
    @allure.title("First State Login Page Validation")
    @allure.feature("Login", "Email", "Google")
    def test_login_init(self, login):
        with allure.step("1. Verify the login init page components"):
            login.main_title_presence()
            login.email_field_presence()
            login.next_button_presence()
            login.google_button_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Second State Login Page Validation")
    @allure.feature("Login", "Email", "Password")
    def test_password_init(self, login):
        with allure.step("1. Insert a valid email account"):
            login.email_insert("simbah.test01@gmail.com")
        with allure.step("2. Click on the 'Berikutnya' button"):
            login.next_button_click()
        with allure.step("3. Verify the password component"):
            login.pass_field_presence()
            login.pass_reveal_presence()
            login.forgot_pass_presence()
            login.enter_button_presence()
            login.sign_up_info_presence()
            login.google_button_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Valid email login validation")
    @allure.feature("Login", "Email", "Password")
    def test_login_with_email(self, login):
        with allure.step("1. Insert a valid email account"):
            login.email_insert("simbah.test01@gmail.com")
        with allure.step("2. Click on the 'Berikutnya' button"):
            login.next_button_click()
        with allure.step("3. Insert a valid email password"):
            login.pass_insert("germa069")
        with allure.step("4. Click on the 'Masuk' button"):
            login.next_button_click()
            login.success_attempt()
