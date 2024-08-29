from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class PersonalInformation(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Personal Information Section Validation"""
    async def section_title_presence(self):
        await self._look(DataDiri.title)
        await expect(self._find(DataDiri.title)).to_have_text("Data Diri")

    async def main_form_presence(self):
        await self._look(DataDiri.main_form)
        await expect(self._find(DataDiri.main_form)).to_be_visible()

    async def hints_presence(self):
        await self._look(DataDiri.main_hint)
        await expect(self._find(DataDiri.main_hint)).to_be_visible()

    async def hints_title_presence(self):
        await self._look(DataDiri.hint_title)
        await expect(self._find(DataDiri.hint_title)).to_have_text('Tips Professional')

    async def hints_desc_presence(self):
        await self._look(DataDiri.hint_desc)
        await expect(self._find(DataDiri.hint_desc)).to_have_text(
            'Cantumkan informasi yang benar dan terbaru.')

    async def hints_toggle_presence(self):
        await self._look(DataDiri.hint_btn)
        await expect(self._find(DataDiri.hint_btn)).to_be_enabled()

    async def first_name_presence(self):
        await self._look(DataDiri.first_name_label)
        await expect(self._find(DataDiri.first_name_label)).to_have_text("Nama Depan")

        await self._touch(DataDiri.first_name_input)
        await expect(self._find(DataDiri.first_name_input)).to_be_empty()
        await expect(self._find(DataDiri.first_name_input)).to_have_attribute("placeholder", "John")

    async def last_name_presence(self):
        await self._look(DataDiri.last_name_label)
        await expect(self._find(DataDiri.last_name_label)).to_have_text("Nama Belakang")

        await self._touch(DataDiri.last_name_input)
        await expect(self._find(DataDiri.last_name_input)).to_be_empty()
        await expect(self._find(DataDiri.last_name_input)).to_have_attribute("placeholder", "Doe")

    async def email_presence(self):
        await self._look(DataDiri.email_label)
        await expect(self._find(DataDiri.email_label)).to_have_text("Email")

        await self._touch(DataDiri.email_input)
        await expect(self._find(DataDiri.email_input)).to_be_empty()
        await expect(self._find(DataDiri.email_input)).to_have_attribute("placeholder", "johndoe@gmail.com")

    async def phone_presence(self):
        await self._look(DataDiri.phone_label)
        await expect(self._find(DataDiri.phone_label)).to_have_text("No. Telepon")

        await self._touch(DataDiri.phone_input)
        await expect(self._find(DataDiri.phone_input)).to_be_empty()
        await expect(self._find(DataDiri.phone_input)).to_have_attribute("placeholder", "081234567890")

    async def country_presence(self):
        await self._look(DataDiri.country_label)
        await expect(self._find(DataDiri.country_label)).to_have_text("Negara")

        await self._touch(DataDiri.country_input)
        await expect(self._find(DataDiri.country_content)).to_have_attribute("title", "Indonesia")

    async def province_presence(self):
        await self._look(DataDiri.province_label)
        await expect(self._find(DataDiri.province_label)).to_have_text("Provinsi")

        await self._touch(DataDiri.province_input)
        await expect(self._find(DataDiri.province_input)).to_be_empty()
        await expect(self._find(DataDiri.province_empty)).to_have_text("Banten")

    async def city_presence(self):
        await self._look(DataDiri.city_label)
        await expect(self._find(DataDiri.city_label)).to_have_text("Kota")

        await self._touch(DataDiri.city_input)
        await expect(self._find(DataDiri.city_input)).to_be_empty()
        await expect(self._find(DataDiri.city_empty)).to_have_text("Tangerang")

    async def address_presence(self):
        await self._look(DataDiri.address_label)
        await expect(self._find(DataDiri.address_label)).to_have_text("Alamat")

        await self._touch(DataDiri.address_input)
        await expect(self._find(DataDiri.address_input)).to_be_empty()
        await expect(self._find(DataDiri.address_input)).to_have_attribute('placeholder', 'Gambir, 10150')

    async def linkedin_presence(self):
        await self._look(DataDiri.linkedin_label)
        await expect(self._find(DataDiri.linkedin_label)).to_have_text("LinkedIn")

        await self._touch(DataDiri.linkedin_input)
        await expect(self._find(DataDiri.linkedin_input)).to_be_empty()
        await expect(self._find(DataDiri.linkedin_input)).to_have_attribute('placeholder',
                                                                            "https://www.linkedin.com/in/johndoe/")

    async def portfolio_presence(self):
        await self._look(DataDiri.portfolio_label)
        await expect(self._find(DataDiri.portfolio_label)).to_have_text("Portofolio")

        await self._touch(DataDiri.portfolio_input)
        await expect(self._find(DataDiri.portfolio_input)).to_be_empty()
        await expect(self._find(DataDiri.portfolio_input)).to_have_attribute('placeholder',
                                                                             'https://portofoliokamu.com')

    async def save_form_presence(self):
        await self._look(DataDiri.submit_btn)
        await expect(self._find(DataDiri.submit_btn)).to_be_enabled()

    """Personal Information Section Interaction"""
    async def collapse_form(self):
        await self._click(DataDiri.title)
        await self._conceal(DataDiri.main_hint)
        await expect(self._find(DataDiri.form_state)).to_have_attribute('aria-expanded', 'false')

    async def expand_form(self):
        await self._click(DataDiri.title)
        await self._look(DataDiri.main_hint)
        await expect(self._find(DataDiri.form_state)).to_have_attribute('aria-expanded', 'true')

    async def hints_click_show(self):
        await self._click(DataDiri.hint_btn)
        await expect(self._find(DataDiri.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(DataDiri.hint_desc)).not_to_be_hidden()

    async def hints_click_hide(self):
        await self._click(DataDiri.hint_btn)
        await expect(self._find(DataDiri.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(DataDiri.hint_desc)).to_be_hidden()

    async def insert_first_name(self, text: str):
        await self._type(DataDiri.first_name_input, text)
        await expect(self._find(DataDiri.first_name_input)).to_be_focused()
        await expect(self._find(DataDiri.first_name_input)).to_have_value(text)

    async def insert_last_name(self, text: str):
        await self._type(DataDiri.last_name_input, text)
        await expect(self._find(DataDiri.last_name_input)).to_be_focused()
        await expect(self._find(DataDiri.last_name_input)).to_have_value(text)

    async def insert_email(self, text: str):
        await self._type(DataDiri.email_input, text)
        await expect(self._find(DataDiri.email_input)).to_be_focused()
        await expect(self._find(DataDiri.email_input)).to_have_value(text)

    async def insert_phone(self, text: str):
        await self._type(DataDiri.phone_input, text)
        await expect(self._find(DataDiri.phone_input)).to_be_focused()
        await expect(self._find(DataDiri.phone_input)).to_have_value(text)

    async def show_country_list(self):
        await self._click(DataDiri.country_input)
        await expect(self._find(DataDiri.country_lists)).to_be_visible()

    async def country_select_wni(self):
        await self.show_country_list()
        await self._force(DataDiri.country_wni)
        await expect(self._find(DataDiri.country_content)).to_have_attribute('title', 'Indonesia')

    async def country_select_wna(self):
        await self.show_country_list()
        await self._force(DataDiri.country_wna)
        await expect(self._find(DataDiri.country_content)).to_have_attribute('title', 'Luar Indonesia')

    async def insert_province(self, text: str):
        await self._type(DataDiri.province_input, text)
        await expect(self._find(DataDiri.province_input)).to_have_value(text)
        await expect(self._find(DataDiri.province_lists)).to_be_attached()

    async def province_click_filled(self):
        await self._click(DataDiri.province_selected)
        await expect(self._find(DataDiri.province_input)).to_be_focused()
        await expect(self._find(DataDiri.province_lists)).to_be_visible()

    async def select_province_option_within(self, text):
        await self.insert_province(text)
        count = await self._find(DataDiri.province_item).count()

        for x in range(1, count + 1):
            await self._click(f"{DataDiri.province_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick the input field
            if x != count:
                await self.province_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(DataDiri.province_lists)).not_to_be_visible()
        await expect(self._find(DataDiri.city_input)).to_be_enabled()

    async def insert_city(self, text: str):
        await self._type(DataDiri.city_input, text)
        await expect(self._find(DataDiri.city_input)).to_have_value(text)
        await expect(self._find(DataDiri.city_lists)).to_be_attached()

    async def city_click_filled(self):
        await self._click(DataDiri.city_selected)
        await expect(self._find(DataDiri.city_input)).to_be_focused()
        await expect(self._find(DataDiri.city_lists)).to_be_visible()

    async def select_city_option_within(self, text):
        await self.insert_city(text)
        count = await self._find(DataDiri.city_item).count()
        for x in range(1, count + 1):
            await self._click(f"{DataDiri.city_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick input field
            if x != count:
                await self.city_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(DataDiri.city_lists)).not_to_be_visible()

    async def insert_address(self, text: str):
        await self._type(DataDiri.address_input, text)
        await expect(self._find(DataDiri.address_input)).to_have_value(text)

    async def insert_linkedin(self, text: str):
        await self._type(DataDiri.linkedin_input, text)
        await expect(self._find(DataDiri.linkedin_input)).to_have_value(text)

    async def insert_portfolio(self, text: str):
        await self._type(DataDiri.portfolio_input, text)
        await expect(self._find(DataDiri.portfolio_input)).to_have_value(text)

    async def click_simpan_button(self):
        await self._click(DataDiri.submit_btn)
