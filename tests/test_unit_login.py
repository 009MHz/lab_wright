import pytest
from pages.login_page import LoginPage
import allure

@pytest.fixture(scope='function')
async def login(page):
    login = LoginPage(page)
    await login.open_login_page()
    return login

@allure.epic("Login Page")
@allure.story("Login Page Smoke Test")
class TestSmokeLoginPage:
    @pytest.mark.asyncio
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("First State Login Page Validation")
    @allure.feature("Login", "Email", "Google")
    async def test_login_init(self, login):
        with allure.step("1. Verify the login init page components"):
            await login.main_title_presence()
            await login.email_field_presence()
            await login.next_button_presence()
            await login.google_button_presence()

    @pytest.mark.asyncio
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Second State Login Page Validation")
    @allure.feature("Login", "Email", "Password")
    async def test_password_init(self, login):
        with allure.step("1. Insert a valid email account"):
            await login.email_insert("simbah.test01@gmail.com")
        with allure.step("2. Click on the 'Berikutnya' button"):
            await login.next_button_click()
        with allure.step("3. Verify the password component"):
            await login.pass_field_presence()
            await login.pass_reveal_presence()
            await login.forgot_pass_presence()
            await login.enter_button_presence()
            await login.sign_up_info_presence()
            await login.google_button_presence()

    @pytest.mark.asyncio
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Valid email login validation")
    @allure.feature("Login", "Email", "Password")
    async def test_login_with_email(self, login):
        with allure.step("1. Insert a valid email account"):
            await login.email_insert("simbah.test01@gmail.com")
        with allure.step("2. Click on the 'Berikutnya' button"):
            await login.next_button_click()
        with allure.step("3. Insert a valid email password"):
            await login.pass_insert("germa069")
        with allure.step("4. Click on the 'Masuk' button"):
            await login.enter_button_click()
            await login.success_attempt()
