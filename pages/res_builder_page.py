from pages.__base import BasePage
from elements.__res_builder import BuildLoc
from playwright.async_api import Page, expect


class Builder(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def load_page(self):
        await self.page.goto(BuildLoc.url)

    """Informasi Resume Section Existence"""
    async def page_title_presence(self):
        await self._look(BuildLoc.page_info_title)
        await expect(self._find(BuildLoc.page_info_title)).to_have_text("Buat Resume Terbaikmu")

    async def info_section_title_presence(self):
        await self._look(BuildLoc.main_info_title)
        await expect(self._find(BuildLoc.main_info_title)).to_have_text("Informasi Resume")

    async def info_resume_name_title_presence(self):
        await self._look(BuildLoc.info_name_label)
        await expect(self._find(BuildLoc.info_name_label)).to_have_text("Nama Resume")

    async def info_resume_name_input_presence(self):
        await self._touch(BuildLoc.info_name_input)
        await expect(self._find(BuildLoc.info_name_input)).to_have_attribute("placeholder", "Yoga 2 Januari 2023")

    async def info_resume_lang_title_presence(self):
        await self._touch(BuildLoc.info_lang_label)
        await expect(self._find(BuildLoc.info_lang_label)).to_have_text("Bahasa Resume")

    async def info_resume_lang_input_presence(self):
        await self._touch(BuildLoc.info_lang_input)
        await expect(self._find(BuildLoc.info_lang_input)).to_have_text("Bahasa Indonesia")

    async def info_resume_goal_title_presence(self):
        await self._touch(BuildLoc.info_goal_label)
        await expect(self._find(BuildLoc.info_goal_label)).to_have_text('Tujuan Pekerjaan')

    async def info_resume_goal_desc_presence(self):
        await self._touch(BuildLoc.info_goal_desc)
        await expect(self._find(BuildLoc.info_goal_desc)).to_contain_text('memberikan rekomendasi')

    async def info_resume_goal_input_presence(self):
        await self._touch(BuildLoc.info_goal_input)
        await expect(self._find(BuildLoc.info_goal_content_empty)).to_have_text('Pilih kategori pekerjaan')

    async def info_resume_import_data_presence(self):
        await self._touch(BuildLoc.info_import_btn)
        await expect(self._find(BuildLoc.info_import_btn)).to_have_text(" Impor Data")

    async def import_data_modal_presence(self):
        await self._look(BuildLoc.info_import_modal)
        await expect(self._find(BuildLoc.info_import_modal)).to_be_visible()

    """Informasi Resume Section Interaction"""
    async def info_resume_name_insert(self, text):
        await self._touch(BuildLoc.info_name_input)
        await self._type(BuildLoc.info_name_input, text)
        await expect(self._find(BuildLoc.info_name_input)).to_have_value(text)

    async def info_resume_lang_click(self):
        await self._touch(BuildLoc.info_lang_input)
        await self._force(BuildLoc.info_lang_input)
        await expect(self._find(BuildLoc.info_lang_ID)).to_be_attached()
        await expect(self._find(BuildLoc.info_lang_EN)).to_be_attached()

    async def info_resume_select_bahasa(self):
        await self._click(BuildLoc.info_lang_ID)
        await expect(self._find(BuildLoc.info_lang_input)).to_contain_text("Bahasa Indonesia")

    async def info_resume_select_language(self):
        await self._click(BuildLoc.info_lang_EN)
        await expect(self._find(BuildLoc.info_lang_input)).to_contain_text("Bahasa Inggris")

    async def info_resume_goal_click(self):
        await self._force(BuildLoc.info_goal_input)
        await expect(self._find(BuildLoc.info_goal_lists)).to_be_attached()

    async def info_resume_goal_items_interact(self):
        total_goals = await self._find(BuildLoc.info_goal_items).count()
        for index in range(1, total_goals + 1):
            option = f"{BuildLoc.info_goal_items}[{index}]"
            opt_label = await self._find(option).get_attribute('title')
            print(f"Selecting: {opt_label}")
            await self._click(option)
            await expect(self._find(BuildLoc.info_goal_content_selected)).to_have_attribute('title', opt_label)
            await self.info_resume_goal_click()

    async def info_resume_import_data_click(self):
        await self._click(BuildLoc.info_import_btn)
        await expect(self._find(BuildLoc.info_import_btn)).to_be_focused()

    """Data Diri Section Existence"""
    async def self_info_title_presence(self):
        await self._look(BuildLoc.self_info_title)
        await expect(self._find(BuildLoc.self_info_title)).to_have_text("Data Diri")

    async def self_info_main_form_presence(self):
        await self._look(BuildLoc.self_info_main_form)
        await expect(self._find(BuildLoc.self_info_main_form)).to_be_visible()

    async def self_info_main_hints_presence(self):
        await self._look(BuildLoc.self_info_main_hint)
        await expect(self._find(BuildLoc.self_info_main_hint)).to_be_visible()

    async def self_info_hints_title_presence(self):
        await self._look(BuildLoc.self_info_hint_title)
        await expect(self._find(BuildLoc.self_info_hint_title)).to_have_text('Tips Professional')

    async def self_info_hints_desc_presence(self):
        await self._look(BuildLoc.self_info_hint_desc)
        await expect(self._find(BuildLoc.self_info_hint_desc)).to_have_text('Cantumkan informasi yang benar dan terbaru.')

    async def self_info_hints_toggle_presence(self):
        await self._look(BuildLoc.self_info_hint_btn)
        await expect(self._find(BuildLoc.self_info_hint_btn)).to_be_enabled()

    async def self_info_first_name_presence(self):
        await self._look(BuildLoc.self_info_first_name_label)
        await expect(self._find(BuildLoc.self_info_first_name_label)).to_have_text("Nama Depan")

        await self._touch(BuildLoc.self_info_first_name_input)
        await expect(self._find(BuildLoc.self_info_first_name_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_first_name_input)).to_have_attribute("placeholder", "John")
        
    async def self_info_last_name_presence(self):
        await self._look(BuildLoc.self_info_last_name_label)
        await expect(self._find(BuildLoc.self_info_last_name_label)).to_have_text("Nama Belakang")

        await self._touch(BuildLoc.self_info_last_name_input)
        await expect(self._find(BuildLoc.self_info_last_name_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_last_name_input)).to_have_attribute("placeholder", "Doe")
        
    async def self_info_email_presence(self):
        await self._look(BuildLoc.self_info_email_label)
        await expect(self._find(BuildLoc.self_info_email_label)).to_have_text("Email")

        await self._touch(BuildLoc.self_info_email_input)
        await expect(self._find(BuildLoc.self_info_email_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_email_input)).to_have_attribute("placeholder", "johndoe@gmail.com")
        
    async def self_info_phone_presence(self):
        await self._look(BuildLoc.self_info_phone_label)
        await expect(self._find(BuildLoc.self_info_phone_label)).to_have_text("No. Telepon")

        await self._touch(BuildLoc.self_info_phone_input)
        await expect(self._find(BuildLoc.self_info_phone_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_phone_input)).to_have_attribute("placeholder", "081234567890")

    async def self_info_country_presence(self):
        await self._look(BuildLoc.self_info_country_label)
        await expect(self._find(BuildLoc.self_info_country_label)).to_have_text("Negara")

        await self._touch(BuildLoc.self_info_country_input)
        await expect(self._find(BuildLoc.self_info_country_content)).to_have_attribute("title", "Indonesia")

    async def self_info_prov_presence(self):
        await self._look(BuildLoc.self_info_province_label)
        await expect(self._find(BuildLoc.self_info_province_label)).to_have_text("Provinsi")

        await self._touch(BuildLoc.self_info_province_input)
        await expect(self._find(BuildLoc.self_info_province_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_province_empty)).to_have_text("Banten")
        
    async def self_info_city_presence(self):
        await self._look(BuildLoc.self_info_city_label)
        await expect(self._find(BuildLoc.self_info_city_label)).to_have_text("Kota")

        await self._touch(BuildLoc.self_info_city_input)
        await expect(self._find(BuildLoc.self_info_city_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_city_empty)).to_have_text("Tangerang")
        
    async def self_info_address_presence(self):
        await self._look(BuildLoc.self_info_address_label)
        await expect(self._find(BuildLoc.self_info_address_label)).to_have_text("Alamat")

        await self._touch(BuildLoc.self_info_address_input)
        await expect(self._find(BuildLoc.self_info_address_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_address_input)).to_have_attribute('placeholder', 'Gambir, 10150')
        
    async def self_info_linkedin_presence(self):
        await self._look(BuildLoc.self_info_linkedin_label)
        await expect(self._find(BuildLoc.self_info_linkedin_label)).to_have_text("LinkedIn")

        await self._touch(BuildLoc.self_info_linkedin_input)
        await expect(self._find(BuildLoc.self_info_linkedin_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_linkedin_input)).to_have_attribute('placeholder', "https://www.linkedin.com/in/johndoe/")
        
    async def self_info_portfolio_presence(self):
        await self._look(BuildLoc.self_info_portfolio_label)
        await expect(self._find(BuildLoc.self_info_portfolio_label)).to_have_text("Portofolio")

        await self._touch(BuildLoc.self_info_portfolio_input)
        await expect(self._find(BuildLoc.self_info_portfolio_input)).to_be_empty()
        await expect(self._find(BuildLoc.self_info_portfolio_input)).to_have_attribute('placeholder', 'https://portofoliokamu.com')

    async def self_info_simpan_btn_presence(self):
        await self._look(BuildLoc.self_info_submit_btn)
        await expect(self._find(BuildLoc.self_info_submit_btn)).to_be_enabled()

    """Data Diri Section Interaction"""
    async def self_info_collapse_form(self):
        await self._click(BuildLoc.self_info_title)
        await self._conceal(BuildLoc.self_info_main_hint)
        await expect(self._find(BuildLoc.self_info_form_state)).to_have_attribute('aria-expanded', 'false')

    async def self_info_expand_form(self):
        await self._click(BuildLoc.self_info_title)
        await self._look(BuildLoc.self_info_main_hint)
        await expect(self._find(BuildLoc.self_info_form_state)).to_have_attribute('aria-expanded', 'true')

    async def self_info_hints_click_show(self):
        await self._click(BuildLoc.self_info_hint_btn)
        await expect(self._find(BuildLoc.self_info_hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(BuildLoc.self_info_hint_desc)).not_to_be_hidden()

    async def self_info_hints_click_hide(self):
        await self._click(BuildLoc.self_info_hint_btn)
        await expect(self._find(BuildLoc.self_info_hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(BuildLoc.self_info_hint_desc)).to_be_hidden()


    # Todo 3: Riwayat Pendidikan Section
    # Todo 4: Riwayat Pekerjaan Section
    # Todo 5: Keahlian
    # Todo 6: Prestasi & Penghargaan
    # Todo 7: Prestasi & Penghargaan
    # Todo 8: Minat
    # Todo 9: Preview
    # Todo 10: Toast Result Action

