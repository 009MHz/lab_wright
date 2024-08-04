from pages.__base import BasePage
from elements.__login import LogInLoc as LogIn
from playwright.async_api import Page, expect, async_playwright


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def open_login_page(self):
        await self.page.goto(LogIn.url)

    """First Login State - Email """
    async def main_title_presence(self):
        await self._look(LogIn.main_title)
        await expect(self._find(LogIn.main_title)).to_be_visible()
        await expect(self._find(LogIn.main_title)).to_have_text("Masuk ke KarirLab")

    async def email_field_presence(self):
        await self._look(LogIn.email_label)
        await expect(self._find(LogIn.email_label)).to_have_text("Email")
        await self._touch(LogIn.email_input)
        await expect(self._find(LogIn.email_input)).to_have_attribute("placeholder", "Masukkan Email")

    async def email_insert(self, user_email):
        await self._touch(LogIn.email_input)
        await self._type(LogIn.email_input, user_email)
        await expect(self._find(LogIn.email_input)).not_to_be_empty()

    async def next_button_presence(self):
        await self._look(LogIn.button_submit)
        await expect(self._find(LogIn.button_submit)).to_be_enabled()
        await expect(self._find(LogIn.button_submit)).to_have_text("Berikutnya")

    async def next_button_click(self):
        await self._force(LogIn.button_submit)
        await expect(self._find(LogIn.button_submit)).to_be_focused()

    async def google_button_presence(self):
        await self._look(LogIn.btn_google_sso)
        await expect(self._find(LogIn.btn_google_sso)).to_be_enabled()
        await expect(self._find(LogIn.btn_google_sso)).to_have_text("Google")

    """Second Login State - Password"""
    async def pass_field_presence(self):
        await self._look(LogIn.pass_label)
        await expect(self._find(LogIn.pass_label)).to_have_text("Kata Sandi")
        await self._touch(LogIn.pass_input)
        await expect(self._find(LogIn.pass_input)).to_have_attribute("placeholder", "Masukkan Kata Sandi")

    async def pass_insert(self, user_pass):
        await self._touch(LogIn.pass_input)
        await self._type(LogIn.pass_input, user_pass)
        await expect(self._find(LogIn.pass_input)).not_to_be_empty()

    async def pass_reveal_presence(self):
        await self._touch(LogIn.pass_eye_icon)
        await expect(self._find(LogIn.pass_eye_icon)).to_have_attribute("aria-label", "eye-invisible")

    async def forgot_pass_presence(self):
        await self._look(LogIn.forget_pass)
        await expect(self._find(LogIn.forget_pass)).to_have_attribute("href", "/forgot-password")
        await expect(self._find(LogIn.forget_pass)).to_have_text("Lupa Kata Sandi?")

    async def enter_button_presence(self):
        await self._look(LogIn.button_submit)
        await expect(self._find(LogIn.button_submit)).to_be_enabled()
        await expect(self._find(LogIn.button_submit)).to_have_text("Masuk")

    async def enter_button_click(self):
        await self._look(LogIn.button_submit)
        await self._click(LogIn.button_submit)
        await expect(self._find(LogIn.button_submit)).to_be_focused()

    async def sign_up_info_presence(self):
        await self._look(LogIn.new_account_message)
        await expect(self._find(LogIn.new_account_message)).to_contain_text("Belum punya akun?")
        await expect(self._find(LogIn.new_account_cta)).to_have_text("Daftar disini")
        await expect(self._find(LogIn.new_account_cta)).to_have_attribute("href", "/sign-up")

    async def success_attempt(self):
        print(await self.page.title())
        await expect(self.page).not_to_have_url("login")
        await self._look(LogIn.side_dashboard)


# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context()
#         page = await context.new_page()
#
#         login_page = LoginPage(page)
#         await login_page.open_login_page()
#         await login_page.main_title_presence()
#
#         await browser.close()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
