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
        await self._look(DataDiri.Initial.main_hint)
        await expect(self._find(DataDiri.Initial.main_hint)).to_be_visible()

    async def hints_title_presence(self):
        await self._look(DataDiri.Initial.hint_title)
        await expect(self._find(DataDiri.Initial.hint_title)).to_have_text('Tips Professional')

    async def hints_desc_presence(self):
        await self._look(DataDiri.Initial.hint_desc)
        await expect(self._find(DataDiri.Initial.hint_desc)).to_have_text(
            'Cantumkan informasi yang benar dan terbaru.')

    async def hints_toggle_presence(self):
        await self._look(DataDiri.Initial.hint_btn)
        await expect(self._find(DataDiri.Initial.hint_btn)).to_be_enabled()

    async def first_name_presence(self):
        await self._look(DataDiri.Initial.first_name_label)
        await expect(self._find(DataDiri.Initial.first_name_label)).to_have_text("Nama Depan")

        await self._touch(DataDiri.Initial.first_name_input)
        await expect(self._find(DataDiri.Initial.first_name_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.first_name_input)).to_have_attribute("placeholder", "John")

    async def last_name_presence(self):
        await self._look(DataDiri.Initial.last_name_label)
        await expect(self._find(DataDiri.Initial.last_name_label)).to_have_text("Nama Belakang")

        await self._touch(DataDiri.Initial.last_name_input)
        await expect(self._find(DataDiri.Initial.last_name_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.last_name_input)).to_have_attribute("placeholder", "Doe")

    async def email_presence(self):
        await self._look(DataDiri.Initial.email_label)
        await expect(self._find(DataDiri.Initial.email_label)).to_have_text("Email")

        await self._touch(DataDiri.Initial.email_input)
        await expect(self._find(DataDiri.Initial.email_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.email_input)).to_have_attribute("placeholder", "johndoe@gmail.com")

    async def phone_presence(self):
        await self._look(DataDiri.Initial.phone_label)
        await expect(self._find(DataDiri.Initial.phone_label)).to_have_text("No. Telepon")

        await self._touch(DataDiri.Initial.phone_input)
        await expect(self._find(DataDiri.Initial.phone_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.phone_input)).to_have_attribute("placeholder", "081234567890")

    async def country_presence(self):
        await self._look(DataDiri.Initial.country_label)
        await expect(self._find(DataDiri.Initial.country_label)).to_have_text("Negara")

        await self._touch(DataDiri.Initial.country_input)
        await expect(self._find(DataDiri.Initial.country_content)).to_have_attribute("title", "Indonesia")

    async def province_presence(self):
        await self._look(DataDiri.Initial.province_label)
        await expect(self._find(DataDiri.Initial.province_label)).to_have_text("Provinsi")

        await self._touch(DataDiri.Initial.province_input)
        await expect(self._find(DataDiri.Initial.province_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.province_empty)).to_have_text("Banten")

    async def city_presence(self):
        await self._look(DataDiri.Initial.city_label)
        await expect(self._find(DataDiri.Initial.city_label)).to_have_text("Kota")

        await self._touch(DataDiri.Initial.city_input)
        await expect(self._find(DataDiri.Initial.city_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.city_empty)).to_have_text("Tangerang")

    async def address_presence(self):
        await self._look(DataDiri.Initial.address_label)
        await expect(self._find(DataDiri.Initial.address_label)).to_have_text("Alamat")

        await self._touch(DataDiri.Initial.address_input)
        await expect(self._find(DataDiri.Initial.address_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.address_input)).to_have_attribute('placeholder', 'Gambir, 10150')

    async def linkedin_presence(self):
        await self._look(DataDiri.Initial.linkedin_label)
        await expect(self._find(DataDiri.Initial.linkedin_label)).to_have_text("LinkedIn")

        await self._touch(DataDiri.Initial.linkedin_input)
        await expect(self._find(DataDiri.Initial.linkedin_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.linkedin_input)).to_have_attribute('placeholder',
                                                                                    "https://www.linkedin.com/in/johndoe/")

    async def portfolio_presence(self):
        await self._look(DataDiri.Initial.portfolio_label)
        await expect(self._find(DataDiri.Initial.portfolio_label)).to_have_text("Portofolio")

        await self._touch(DataDiri.Initial.portfolio_input)
        await expect(self._find(DataDiri.Initial.portfolio_input)).to_be_empty()
        await expect(self._find(DataDiri.Initial.portfolio_input)).to_have_attribute('placeholder',
                                                                                     'https://portofoliokamu.com')

    async def save_form_presence(self):
        await self._look(DataDiri.submit_btn)
        await expect(self._find(DataDiri.submit_btn)).to_be_enabled()

    """Personal Information Section Interaction"""
    async def collapse_form(self):
        await self._click(DataDiri.title)
        await self._conceal(DataDiri.Initial.main_hint)
        await expect(self._find(DataDiri.form_state)).to_have_attribute('aria-expanded', 'false')

    async def expand_form(self):
        await self._click(DataDiri.title)
        await self._look(DataDiri.Initial.main_hint)
        await expect(self._find(DataDiri.form_state)).to_have_attribute('aria-expanded', 'true')

    async def hints_click_show(self):
        await self._click(DataDiri.Initial.hint_btn)
        await expect(self._find(DataDiri.Initial.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(DataDiri.Initial.hint_desc)).not_to_be_hidden()

    async def hints_click_hide(self):
        await self._click(DataDiri.Initial.hint_btn)
        await expect(self._find(DataDiri.Initial.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(DataDiri.Initial.hint_desc)).to_be_hidden()

    async def insert_first_name(self, text: str):
        await self._type(DataDiri.Initial.first_name_input, text)
        await expect(self._find(DataDiri.Initial.first_name_input)).to_be_focused()
        await expect(self._find(DataDiri.Initial.first_name_input)).to_have_value(text)

    async def insert_last_name(self, text: str):
        await self._type(DataDiri.Initial.last_name_input, text)
        await expect(self._find(DataDiri.Initial.last_name_input)).to_be_focused()
        await expect(self._find(DataDiri.Initial.last_name_input)).to_have_value(text)

    async def insert_email(self, text: str):
        await self._type(DataDiri.Initial.email_input, text)
        await expect(self._find(DataDiri.Initial.email_input)).to_be_focused()
        await expect(self._find(DataDiri.Initial.email_input)).to_have_value(text)

    async def insert_phone(self, text: str):
        await self._type(DataDiri.Initial.phone_input, text)
        await expect(self._find(DataDiri.Initial.phone_input)).to_be_focused()
        await expect(self._find(DataDiri.Initial.phone_input)).to_have_value(text)

    async def show_country_list(self):
        await self._click(DataDiri.Initial.country_input)
        await expect(self._find(DataDiri.Initial.country_lists)).to_be_visible()

    async def country_select_wni(self):
        await self.show_country_list()
        await self._force(DataDiri.Initial.country_wni)
        await expect(self._find(DataDiri.Initial.country_content)).to_have_attribute('title', 'Indonesia')

    async def country_select_wna(self):
        await self.show_country_list()
        await self._force(DataDiri.Initial.country_wna)
        await expect(self._find(DataDiri.Initial.country_content)).to_have_attribute('title', 'Luar Indonesia')

    async def insert_province(self, text: str):
        await self._type(DataDiri.Initial.province_input, text)
        await expect(self._find(DataDiri.Initial.province_input)).to_have_value(text)
        await expect(self._find(DataDiri.Initial.province_lists)).to_be_attached()

    async def province_click_filled(self):
        await self._click(DataDiri.Initial.province_selected)
        await expect(self._find(DataDiri.Initial.province_input)).to_be_focused()
        await expect(self._find(DataDiri.Initial.province_lists)).to_be_visible()

    async def select_province_option_within(self, text):
        await self.insert_province(text)
        count = await self._find(DataDiri.Initial.province_item).count()

        for x in range(1, count + 1):
            await self._click(f"{DataDiri.Initial.province_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick the input field
            if x != count:
                await self.province_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(DataDiri.Initial.province_lists)).not_to_be_visible()
        await expect(self._find(DataDiri.Initial.city_input)).to_be_enabled()

    async def insert_city(self, text: str):
        await self._type(DataDiri.Initial.city_input, text)
        await expect(self._find(DataDiri.Initial.city_input)).to_have_value(text)
        await expect(self._find(DataDiri.Initial.city_lists)).to_be_attached()

    async def city_click_filled(self):
        await self._click(DataDiri.Initial.city_selected)
        await expect(self._find(DataDiri.Initial.city_input)).to_be_focused()
        await expect(self._find(DataDiri.Initial.city_lists)).to_be_visible()

    async def select_city_option_within(self, text):
        await self.insert_city(text)
        count = await self._find(DataDiri.Initial.city_item).count()
        for x in range(1, count + 1):
            await self._click(f"{DataDiri.Initial.city_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick input field
            if x != count:
                await self.city_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(DataDiri.Initial.city_lists)).not_to_be_visible()

    async def insert_address(self, text: str):
        await self._type(DataDiri.Initial.address_input, text)
        await expect(self._find(DataDiri.Initial.address_input)).to_have_value(text)

    async def insert_linkedin(self, text: str):
        await self._type(DataDiri.Initial.linkedin_input, text)
        await expect(self._find(DataDiri.Initial.linkedin_input)).to_have_value(text)

    async def insert_portfolio(self, text: str):
        await self._type(DataDiri.Initial.portfolio_input, text)
        await expect(self._find(DataDiri.Initial.portfolio_input)).to_have_value(text)

    async def click_simpan_button(self):
        await self._click(DataDiri.submit_btn)

    """Personal Information Saved input Validation"""
    async def hints_absence(self):
        await self._conceal(DataDiri.Initial.main_hint)
        await expect(self._find(DataDiri.Initial.main_hint)).not_to_be_visible()

    async def first_name_absence(self):
        await self._conceal(DataDiri.Initial.first_name_label)
        await expect(self._find(DataDiri.Initial.first_name_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.first_name_input)
        await expect(self._find(DataDiri.Initial.first_name_input)).not_to_be_visible()

    async def last_name_absence(self):
        await self._conceal(DataDiri.Initial.last_name_label)
        await expect(self._find(DataDiri.Initial.last_name_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.last_name_input)
        await expect(self._find(DataDiri.Initial.last_name_input)).not_to_be_visible()

    async def email_absence(self):
        await self._conceal(DataDiri.Initial.email_label)
        await expect(self._find(DataDiri.Initial.email_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.email_input)
        await expect(self._find(DataDiri.Initial.email_input)).not_to_be_visible()

    async def phone_absence(self):
        await self._conceal(DataDiri.Initial.phone_label)
        await expect(self._find(DataDiri.Initial.phone_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.phone_input)
        await expect(self._find(DataDiri.Initial.phone_input)).not_to_be_visible()

    async def country_absence(self):
        await self._conceal(DataDiri.Initial.country_label)
        await expect(self._find(DataDiri.Initial.country_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.country_input)
        await expect(self._find(DataDiri.Initial.country_content)).not_to_be_visible()

    async def province_absence(self):
        await self._conceal(DataDiri.Initial.province_label)
        await expect(self._find(DataDiri.Initial.province_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.province_input)
        await expect(self._find(DataDiri.Initial.province_input)).not_to_be_visible()

    async def city_absence(self):
        await self._conceal(DataDiri.Initial.city_label)
        await expect(self._find(DataDiri.Initial.city_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.city_input)
        await expect(self._find(DataDiri.Initial.city_input)).not_to_be_visible()

    async def address_absence(self):
        await self._conceal(DataDiri.Initial.address_label)
        await expect(self._find(DataDiri.Initial.address_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.address_input)
        await expect(self._find(DataDiri.Initial.address_input)).not_to_be_visible()

    async def linkedin_absence(self):
        await self._conceal(DataDiri.Initial.linkedin_label)
        await expect(self._find(DataDiri.Initial.linkedin_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.linkedin_input)
        await expect(self._find(DataDiri.Initial.linkedin_input)).not_to_be_visible()

    async def portfolio_absence(self):
        await self._conceal(DataDiri.Initial.portfolio_label)
        await expect(self._find(DataDiri.Initial.portfolio_label)).not_to_be_visible()

        await self._conceal(DataDiri.Initial.portfolio_input)
        await expect(self._find(DataDiri.Initial.portfolio_input)).not_to_be_visible()

    async def saved_first_name_presence(self):
        await self._look(DataDiri.Filled.first_name)
        await expect(self._find(DataDiri.Filled.first_name)).not_to_have_text("")

    async def saved_last_name_presence(self):
        await self._look(DataDiri.Filled.first_name)
        await expect(self._find(DataDiri.Filled.first_name)).not_to_have_text("")

    async def saved_email_presence(self):
        await self._look(DataDiri.Filled.email)
        await expect(self._find(DataDiri.Filled.email)).to_contain_text("@")

    async def saved_phone_presence(self):
        await self._look(DataDiri.Filled.phone)
        await expect(self._find(DataDiri.Filled.phone)).not_to_have_text("")

    async def saved_province_presence(self):
        await self._look(DataDiri.Filled.province)
        await expect(self._find(DataDiri.Filled.province)).not_to_have_text("")

    async def saved_city_presence(self):
        await self._look(DataDiri.Filled.city)
        await expect(self._find(DataDiri.Filled.city)).not_to_have_text("")

    async def saved_address_presence(self):
        await self._look(DataDiri.Filled.address)
        await expect(self._find(DataDiri.Filled.address)).not_to_have_text("")

    async def saved_linkedin_presence(self):
        await self._look(DataDiri.Filled.linkedin)
        await expect(self._find(DataDiri.Filled.linkedin)).to_contain_text("https://www.linkedin.com/")

        await self._look(DataDiri.Filled.linkedin_checkbox)
        await expect(self._find(DataDiri.Filled.linkedin_checkbox)).to_be_checked()

    async def saved_portfolio_presence(self):
        await self._look(DataDiri.Filled.portfolio)
        await expect(self._find(DataDiri.Filled.portfolio)).to_contain_text("https://")

        await self._look(DataDiri.Filled.portfolio_checkbox)
        await expect(self._find(DataDiri.Filled.portfolio_checkbox)).to_be_checked()

    async def saved_button_save_presence(self):
        await expect(self._find(DataDiri.Filled.save)).to_be_attached()

        await self._find(DataDiri.Filled.wrapper).hover()
        await expect(self._find(DataDiri.Filled.save)).to_be_visible()

    async def saved_button_edit_presence(self):
        await expect(self._find(DataDiri.Filled.edit)).to_be_attached()

        await self._find(DataDiri.Filled.wrapper).hover()
        await expect(self._find(DataDiri.Filled.edit)).to_be_visible()

    async def saved_button_delete_presence(self):
        await expect(self._find(DataDiri.Filled.delete)).to_be_attached()

        await self._find(DataDiri.Filled.wrapper).hover()
        await expect(self._find(DataDiri.Filled.delete)).to_be_visible()

    """Data Diri Resume Preview Validation"""
    async def preview_main_form_presence(self):
        await self._look(Preview.main)
        await expect(self._find(Preview.main)).not_to_be_empty()

    async def preview_section_title_presence(self):
        await self._look(Preview.section_title)
        await expect(self._find(Preview.section_title)).to_have_text("Pratinjau Resume")

    async def preview_section_info_presence(self):
        await self._look(Preview.completeness)
        await expect(self._find(Preview.completeness)).to_have_text("Kelengkapan Resume")
        await expect(self._find(Preview.complete_tag)).to_be_visible()

    async def preview_first_name_presence(self):
        await self._look(DataDiri.Preview.name)

        stored_first_name = await self._find(DataDiri.Filled.first_name).text_content()
        await expect(self._find(DataDiri.Preview.first_name)).to_be_visible()
        await expect(self._find(DataDiri.Preview.first_name)).to_have_text(stored_first_name)

    async def preview_last_name_presence(self):
        await self._look(DataDiri.Preview.name)

        stored_name = await self._find(DataDiri.Filled.last_name).text_content()
        await expect(self._find(DataDiri.Preview.last_name)).to_be_visible()
        await expect(self._find(DataDiri.Preview.last_name)).to_have_text(stored_name)
    
    async def preview_phone_presence(self):
        await self._look(DataDiri.Preview.phone)

        stored_name = await self._find(DataDiri.Filled.phone).text_content()
        await expect(self._find(DataDiri.Preview.phone)).to_be_visible()
        await expect(self._find(DataDiri.Preview.phone)).to_have_text(stored_name)
        
    async def preview_province_presence(self):
        await self._look(DataDiri.Preview.province)

        stored_name = await self._find(DataDiri.Filled.province).text_content()
        await expect(self._find(DataDiri.Preview.province)).to_be_visible()
        await expect(self._find(DataDiri.Preview.province)).to_have_text(stored_name)
        
    async def preview_email_presence(self):
        await self._look(DataDiri.Preview.email)

        stored_name = await self._find(DataDiri.Filled.email).text_content()
        await expect(self._find(DataDiri.Preview.email)).to_be_visible()
        await expect(self._find(DataDiri.Preview.email)).to_have_text(stored_name)
        
    async def preview_city_presence(self):
        await self._look(DataDiri.Preview.city)

        stored_name = await self._find(DataDiri.Filled.city).text_content()
        await expect(self._find(DataDiri.Preview.city)).to_be_visible()
        await expect(self._find(DataDiri.Preview.city)).to_have_text(stored_name.title())
        
    async def preview_portfolio_presence(self):
        await self._look(DataDiri.Preview.portfolio)
        await expect(self._find(DataDiri.Preview.portfolio)).to_be_visible()

        stored_name = await self._find(DataDiri.Preview.portfolio).text_content()
        await expect(self._find(DataDiri.Filled.portfolio)).to_contain_text(stored_name)
        
    async def preview_linkedin_presence(self):
        await self._look(DataDiri.Preview.linkedin)
        await expect(self._find(DataDiri.Preview.linkedin)).to_be_visible()
        
        stored_name = await self._find(DataDiri.Preview.linkedin).text_content()
        await expect(self._find(DataDiri.Filled.linkedin)).to_contain_text(stored_name)
    
    async def preview_address_presence(self):
        await self._look(DataDiri.Preview.address)

        stored_name = await self._find(DataDiri.Filled.address).text_content()
        await expect(self._find(DataDiri.Preview.address)).to_be_visible()
        await expect(self._find(DataDiri.Preview.address)).to_have_text(stored_name)

