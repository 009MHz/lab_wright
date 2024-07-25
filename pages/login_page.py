from pages.__base import BasePage
from elements.__login import LogInLoc as LogIn
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_login_page(self):
        self.page.goto(LogIn.url)

    def main_title_presence(self):
        self._look(LogIn.main_title)
        expect(self._find(LogIn.main_title)).to_be_visible()
        expect(self._find(LogIn.main_title)).to_have_text("Masuk ke KarirLab")

    def email_field_presence(self):
        self._look(LogIn.email_label)
        expect(self._find(LogIn.email_label)).to_have_text("Email")
        self._touch(LogIn.email_input)
        expect(self._find(LogIn.email_input)).to_have_attribute(["[placeholder= 'Masukkan Email']"])

    def next_button_presence(self):
        self._look(LogIn.btn_next)
        expect(self._find(LogIn.btn_next)).to_be_enabled()

    def google_button_presence(self):
        self._look(LogIn.btn_google_sso)
        expect(self._find(LogIn.btn_google_sso)).to_be_enabled()
