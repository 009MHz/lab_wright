from pages.__base import BasePage
from elements.__login import LogInLoc as LogIn
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_login_page(self):
        self.page.goto(LogIn.url)

    """First Login State - Email """
    def main_title_presence(self):
        self._look(LogIn.main_title)
        expect(self._find(LogIn.main_title)).to_be_visible()
        expect(self._find(LogIn.main_title)).to_have_text("Masuk ke KarirLab")

    def email_field_presence(self):
        self._look(LogIn.email_label)
        expect(self._find(LogIn.email_label)).to_have_text("Email")
        self._touch(LogIn.email_input)
        expect(self._find(LogIn.email_input)).to_have_attribute("placeholder", "Masukkan Email")

    def email_insert(self, user_email):
        self._touch(LogIn.email_input)
        self._type(LogIn.email_input, user_email)
        expect(self._find(LogIn.email_input)).not_to_be_empty()

    def next_button_presence(self):
        self._look(LogIn.button_submit)
        expect(self._find(LogIn.button_submit)).to_be_enabled()
        expect(self._find(LogIn.button_submit)).to_have_text("Berikutnya")

    def next_button_click(self):
        self._look(LogIn.button_submit)
        self._click(LogIn.button_submit)
        expect(self._find(LogIn.button_submit)).to_be_focused()

    def google_button_presence(self):
        self._look(LogIn.btn_google_sso)
        expect(self._find(LogIn.btn_google_sso)).to_be_enabled()
        expect(self._find(LogIn.btn_google_sso)).to_have_text("Google")

    """Second Login State - Password"""
    def pass_field_presence(self):
        self._look(LogIn.pass_label)
        expect(self._find(LogIn.pass_label)).to_have_text("Kata Sandi")
        self._touch(LogIn.pass_input)
        expect(self._find(LogIn.pass_input)).to_have_attribute("placeholder", "Masukkan Kata Sandi")

    def pass_insert(self, user_pass):
        self._touch(LogIn.pass_input)
        self._type(LogIn.pass_input, user_pass)
        expect(self._find(LogIn.pass_input)).not_to_be_empty()

    def pass_reveal_presence(self):
        self._touch(LogIn.pass_eye_icon)
        expect(self._find(LogIn.pass_eye_icon)).to_have_attribute("aria-label", "eye-invisible")

    def forgot_pass_presence(self):
        self._look(LogIn.forget_pass)
        expect(self._find(LogIn.forget_pass)).to_have_attribute("href", "/forgot-password")
        expect(self._find(LogIn.forget_pass)).to_have_text("Lupa Kata Sandi?")

    def enter_button_presence(self):
        self._look(LogIn.button_submit)
        expect(self._find(LogIn.button_submit)).to_be_enabled()
        expect(self._find(LogIn.button_submit)).to_have_text("Masuk")

    def enter_button_click(self):
        self._look(LogIn.button_submit)
        self._click(LogIn.button_submit)
        expect(self._find(LogIn.button_submit)).to_be_focused()

    def sign_up_info_presence(self):
        self._look(LogIn.new_account_message)
        expect(self._find(LogIn.new_account_message)).to_contain_text("Belum punya akun?")
        expect(self._find(LogIn.new_account_cta)).to_have_text("Daftar disini")
        expect(self._find(LogIn.new_account_cta)).to_have_attribute("href", "/sign-up")

    def success_attempt(self):
        print(self.page.title())
        expect(self.page).not_to_have_url("login")