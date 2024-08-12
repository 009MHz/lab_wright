from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Builder(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def load_page(self):
        await self.page.goto(PageInfo.url)

    """Resume Information Section Existence"""
    async def page_title_presence(self):
        await self._look(PageInfo.title)
        await expect(self._find(PageInfo.title)).to_have_text("Buat Resume Terbaikmu")

    async def info_section_title_presence(self):
        await self._look(ResumeInfo.title)
        await expect(self._find(ResumeInfo.title)).to_have_text("Informasi Resume")

    async def info_resume_name_title_presence(self):
        await self._look(ResumeInfo.name_label)
        await expect(self._find(ResumeInfo.name_label)).to_have_text("Nama Resume")

    async def info_resume_name_input_presence(self):
        await self._touch(ResumeInfo.name_input)
        await expect(self._find(ResumeInfo.name_input)).to_have_attribute("placeholder","Yoga 2 Januari 2023")

    async def info_resume_lang_title_presence(self):
        await self._touch(ResumeInfo.lang_label)
        await expect(self._find(ResumeInfo.lang_label)).to_have_text("Bahasa Resume")

    async def info_resume_lang_input_presence(self):
        await self._touch(ResumeInfo.lang_input)
        await expect(self._find(ResumeInfo.lang_input)).to_have_text("Bahasa Indonesia")

    async def info_resume_goal_title_presence(self):
        await self._touch(ResumeInfo.goal_label)
        await expect(self._find(ResumeInfo.goal_label)).to_have_text('Tujuan Pekerjaan')

    async def info_resume_goal_desc_presence(self):
        await self._touch(ResumeInfo.goal_desc)
        await expect(self._find(ResumeInfo.goal_desc)).to_contain_text('memberikan rekomendasi')

    async def info_resume_goal_input_presence(self):
        await self._touch(ResumeInfo.goal_input)
        await expect(self._find(ResumeInfo.goal_content_empty)).to_have_text('Pilih kategori pekerjaan')

    async def info_resume_import_data_presence(self):
        await self._touch(ResumeInfo.import_btn)
        await expect(self._find(ResumeInfo.import_btn)).to_have_text(" Impor Data")

    async def import_data_modal_presence(self):
        await self._look(ResumeInfo.import_modal)
        await expect(self._find(ResumeInfo.import_modal)).to_be_visible()

    """Resume Information Section Interaction"""

    async def info_resume_name_insert(self, text):
        await self._touch(ResumeInfo.name_input)
        await self._type(ResumeInfo.name_input, text)
        await expect(self._find(ResumeInfo.name_input)).to_have_value(text)

    async def info_resume_lang_click(self):
        await self._touch(ResumeInfo.lang_input)
        await self._force(ResumeInfo.lang_input)
        await expect(self._find(ResumeInfo.lang_id)).to_be_attached()
        await expect(self._find(ResumeInfo.lang_en)).to_be_attached()

    async def info_resume_select_bahasa(self):
        await self._click(ResumeInfo.lang_id)
        await expect(self._find(ResumeInfo.lang_input)).to_contain_text("Bahasa Indonesia")

    async def info_resume_select_language(self):
        await self._click(ResumeInfo.lang_en)
        await expect(self._find(ResumeInfo.lang_input)).to_contain_text("Bahasa Inggris")

    async def info_resume_goal_click(self):
        await self._force(ResumeInfo.goal_input)
        await expect(self._find(ResumeInfo.goal_lists)).to_be_attached()

    async def info_resume_goal_items_interact(self):
        total_goals = await self._find(ResumeInfo.goal_items).count()
        for index in range(1, total_goals + 1):
            option = f"{ResumeInfo.goal_items}[{index}]"
            opt_label = await self._find(option).get_attribute('title')
            print(f"Selecting: {opt_label}")
            await self._click(option)
            await expect(self._find(ResumeInfo.goal_content_selected)).to_have_attribute('title',
                                                                                                  opt_label)
            await self.info_resume_goal_click()

    async def info_resume_import_data_click(self):
        await self._click(ResumeInfo.import_btn)
        await expect(self._find(ResumeInfo.import_btn)).to_be_focused()

    """Personal Information Section Existence"""

    async def self_info_title_presence(self):
        await self._look(DataDiri.title)
        await expect(self._find(DataDiri.title)).to_have_text("Data Diri")

    async def self_info_main_form_presence(self):
        await self._look(DataDiri.main_form)
        await expect(self._find(DataDiri.main_form)).to_be_visible()

    async def self_info_main_hints_presence(self):
        await self._look(DataDiri.main_hint)
        await expect(self._find(DataDiri.main_hint)).to_be_visible()

    async def self_info_hints_title_presence(self):
        await self._look(DataDiri.hint_title)
        await expect(self._find(DataDiri.hint_title)).to_have_text('Tips Professional')

    async def self_info_hints_desc_presence(self):
        await self._look(DataDiri.hint_desc)
        await expect(self._find(DataDiri.hint_desc)).to_have_text(
            'Cantumkan informasi yang benar dan terbaru.')

    async def self_info_hints_toggle_presence(self):
        await self._look(DataDiri.hint_btn)
        await expect(self._find(DataDiri.hint_btn)).to_be_enabled()

    async def self_info_first_name_presence(self):
        await self._look(DataDiri.first_name_label)
        await expect(self._find(DataDiri.first_name_label)).to_have_text("Nama Depan")

        await self._touch(DataDiri.first_name_input)
        await expect(self._find(DataDiri.first_name_input)).to_be_empty()
        await expect(self._find(DataDiri.first_name_input)).to_have_attribute("placeholder", "John")

    async def self_info_last_name_presence(self):
        await self._look(DataDiri.last_name_label)
        await expect(self._find(DataDiri.last_name_label)).to_have_text("Nama Belakang")

        await self._touch(DataDiri.last_name_input)
        await expect(self._find(DataDiri.last_name_input)).to_be_empty()
        await expect(self._find(DataDiri.last_name_input)).to_have_attribute("placeholder", "Doe")

    async def self_info_email_presence(self):
        await self._look(DataDiri.email_label)
        await expect(self._find(DataDiri.email_label)).to_have_text("Email")

        await self._touch(DataDiri.email_input)
        await expect(self._find(DataDiri.email_input)).to_be_empty()
        await expect(self._find(DataDiri.email_input)).to_have_attribute("placeholder",
                                                                                             "johndoe@gmail.com")

    async def self_info_phone_presence(self):
        await self._look(DataDiri.phone_label)
        await expect(self._find(DataDiri.phone_label)).to_have_text("No. Telepon")

        await self._touch(DataDiri.phone_input)
        await expect(self._find(DataDiri.phone_input)).to_be_empty()
        await expect(self._find(DataDiri.phone_input)).to_have_attribute("placeholder",
                                                                                             "081234567890")

    async def self_info_country_presence(self):
        await self._look(DataDiri.country_label)
        await expect(self._find(DataDiri.country_label)).to_have_text("Negara")

        await self._touch(DataDiri.country_input)
        await expect(self._find(DataDiri.country_content)).to_have_attribute("title", "Indonesia")

    async def self_info_prov_presence(self):
        await self._look(DataDiri.province_label)
        await expect(self._find(DataDiri.province_label)).to_have_text("Provinsi")

        await self._touch(DataDiri.province_input)
        await expect(self._find(DataDiri.province_input)).to_be_empty()
        await expect(self._find(DataDiri.province_empty)).to_have_text("Banten")

    async def self_info_city_presence(self):
        await self._look(DataDiri.city_label)
        await expect(self._find(DataDiri.city_label)).to_have_text("Kota")

        await self._touch(DataDiri.city_input)
        await expect(self._find(DataDiri.city_input)).to_be_empty()
        await expect(self._find(DataDiri.city_empty)).to_have_text("Tangerang")

    async def self_info_address_presence(self):
        await self._look(DataDiri.address_label)
        await expect(self._find(DataDiri.address_label)).to_have_text("Alamat")

        await self._touch(DataDiri.address_input)
        await expect(self._find(DataDiri.address_input)).to_be_empty()
        await expect(self._find(DataDiri.address_input)).to_have_attribute('placeholder',
                                                                                               'Gambir, 10150')

    async def self_info_linkedin_presence(self):
        await self._look(DataDiri.linkedin_label)
        await expect(self._find(DataDiri.linkedin_label)).to_have_text("LinkedIn")

        await self._touch(DataDiri.linkedin_input)
        await expect(self._find(DataDiri.linkedin_input)).to_be_empty()
        await expect(self._find(DataDiri.linkedin_input)).to_have_attribute('placeholder',
                                                                                                "https://www.linkedin.com/in/johndoe/")

    async def self_info_portfolio_presence(self):
        await self._look(DataDiri.portfolio_label)
        await expect(self._find(DataDiri.portfolio_label)).to_have_text("Portofolio")

        await self._touch(DataDiri.portfolio_input)
        await expect(self._find(DataDiri.portfolio_input)).to_be_empty()
        await expect(self._find(DataDiri.portfolio_input)).to_have_attribute('placeholder',
                                                                                                 'https://portofoliokamu.com')

    async def self_info_simpan_btn_presence(self):
        await self._look(DataDiri.submit_btn)
        await expect(self._find(DataDiri.submit_btn)).to_be_enabled()

    """Personal Information Section Interaction"""

    async def self_info_collapse_form(self):
        await self._click(DataDiri.title)
        await self._conceal(DataDiri.main_hint)
        await expect(self._find(DataDiri.form_state)).to_have_attribute('aria-expanded', 'false')

    async def self_info_expand_form(self):
        await self._click(DataDiri.title)
        await self._look(DataDiri.main_hint)
        await expect(self._find(DataDiri.form_state)).to_have_attribute('aria-expanded', 'true')

    async def self_info_hints_click_show(self):
        await self._click(DataDiri.hint_btn)
        await expect(self._find(DataDiri.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(DataDiri.hint_desc)).not_to_be_hidden()

    async def self_info_hints_click_hide(self):
        await self._click(DataDiri.hint_btn)
        await expect(self._find(DataDiri.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(DataDiri.hint_desc)).to_be_hidden()

    async def self_info_first_name_insert(self, text: str):
        await self._type(DataDiri.first_name_input, text)
        await expect(self._find(DataDiri.first_name_input)).to_be_focused()
        await expect(self._find(DataDiri.first_name_input)).to_have_value(text)

    async def self_info_last_name_insert(self, text: str):
        await self._type(DataDiri.last_name_input, text)
        await expect(self._find(DataDiri.last_name_input)).to_be_focused()
        await expect(self._find(DataDiri.last_name_input)).to_have_value(text)

    async def self_info_email_insert(self, text: str):
        await self._type(DataDiri.email_input, text)
        await expect(self._find(DataDiri.email_input)).to_be_focused()
        await expect(self._find(DataDiri.email_input)).to_have_value(text)

    async def self_info_phone_insert(self, text: str):
        await self._type(DataDiri.phone_input, text)
        await expect(self._find(DataDiri.phone_input)).to_be_focused()
        await expect(self._find(DataDiri.phone_input)).to_have_value(text)

    async def self_info_click_country(self):
        await self._click(DataDiri.country_input)
        await expect(self._find(DataDiri.country_lists)).to_be_visible()

    async def self_info_select_wni(self):
        await self._force(DataDiri.country_wni)
        await expect(self._find(DataDiri.country_content)).to_have_attribute('title', 'Indonesia')

    async def self_info_select_wna(self):
        await self._force(DataDiri.country_wna)
        await expect(self._find(DataDiri.country_content)).to_have_attribute('title',
                                                                                                 'Luar Indonesia')

    async def self_info_prov_insert(self, text: str):
        await self._type(DataDiri.province_input, text)
        await expect(self._find(DataDiri.province_input)).to_have_value(text)
        await expect(self._find(DataDiri.province_lists)).to_be_visible()

    async def self_info_prov_click_all_prov(self):
        pass
        await self._look(DataDiri.province_lists)
        # choices = await self._find(PersonalInformation.province_item).get_attribute('title')
        # print(f"Collected Province Item: {choices}")

    async def self_info_city_insert(self, text: str):
        await self._type(DataDiri.city_input, text)
        await expect(self._find(DataDiri.city_input)).to_have_value(text)
        await expect(self._find(DataDiri.city_lists)).to_be_visible()

    async def self_info_city_click_all_city(self):
        pass
        await self._look(DataDiri.city_lists)
        # choices = await self._find(PersonalInformation.city_item).get_attribute('title')
        # print(f"Collected city Item: {choices}")

    async def self_info_address_insert(self, text: str):
        await self._type(DataDiri.address_input, text)
        await expect(self._find(DataDiri.address_input)).to_have_value(text)

    async def self_info_linkedin_insert(self, text: str):
        await self._type(DataDiri.linkedin_input, text)
        await expect(self._find(DataDiri.linkedin_input)).to_have_value(text)

    async def self_info_portfolio_insert(self, text: str):
        await self._type(DataDiri.portfolio_input, text)
        await expect(self._find(DataDiri.portfolio_input)).to_have_value(text)

    async def self_info_click_simpan(self):
        await self._click(DataDiri.submit_btn)
        await expect(self._find(DataDiri.submit_btn)).to_be_focused()

    """Education History Existence"""
    # Header Existence Validation
    async def edu_title_presence(self):
        await self._look(EduHistory.title)
        await expect(self._find(EduHistory.title)).to_have_text("Riwayat Pendidikan")

    """Education History Interaction"""
    async def edu_title_click_collapse(self):
        await self._touch(EduHistory.title)
        await self._force(EduHistory.title)
        await expect(self._find(ResumeInfo.lang_id)).to_be_attached()
        await expect(self._find(ResumeInfo.lang_en)).to_be_attached()
    # Todo 3c: Main Form Content validation after add new form
    # Todo 3d: Validate Main content state & existence
    # Todo 3e: Validate Hints Existence & Interaction
    # Todo 3f: Validate Hints Existence
    # Todo 3g: Validate Degree Existence
    # Todo 3g.a: Degree Show Option
    # Todo 3g.b: Degree Select Options
    # Todo 3h: Validate Institution Name Existence
    # Todo 3h.a: Institution Name Insert Keyword & validate option lists
    # Todo 3h.b: Institution Name Select option based on keyword
    # Todo 3i: Validate Faculty Existence
    # Todo 3i.a: Faculty Insert Keyword & validate option lists
    # Todo 3i.b: Faculty Select option based on keyword
    # Todo 3j: Validate Final Score Existence
    # Todo 3j.a: Final Score Insert Value action
    # Todo 3j.b: Final Score Warning validation
    # Todo 3k: Validate Max Final Score Existence
    # Todo 3k.a: Max Final Score Insert Value action
    # Todo 3k.b: Max Final Score Warning validation
    # Todo 3l: Validate Institution Country
    # Todo 3l.a: Institution Country interaction
    # Todo 3m: Validate Institution Province Existence
    # Todo 3m.a: Institution Province Insert Keyword & validate option lists
    # Todo 3m.b: Institution Province Select option based on keyword
    # Todo 3n: Validate Institution City Existence
    # Todo 3n.a: Institution City Insert Keyword & validate option lists
    # Todo 3n.b: Institution City Select option based on keyword
    # Todo 3o: Validate Start Date existence
    # Todo 3o.a: Validate Start Date datepicker
    # Todo 3o.b: Start Date select date action
    # Todo 3o.c: Start Date clear date selection
    # Todo 3o.d: Start Date pass manual date value
    # Todo 3p: Validate Graduation Date existence
    # Todo 3p.a: Validate Graduation Date datepicker
    # Todo 3p.b: Graduation Date select date action
    # Todo 3p.c: Graduation Date clear date selection
    # Todo 3p.d: Graduation Date pass manual date value
    # Todo 3q: Validate Education History Main button existence
    # Todo 3q.a: Validate Education History Main button action

    # Todo 4: Occupation History Section
    # Todo 5: Proficiencies
    # Todo 6: Achievements
    # Todo 7: Achievements
    # Todo 8: Hobbies
    # Todo 9: Preview
    # Todo 10: Toast Result Action
