from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Builder(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def load_page(self):
        await self.page.goto(PageInfo.url)

    """Resume Information Section Validation"""
    async def page_title_presence(self):
        await self._look(PageInfo.title)
        await expect(self._find(PageInfo.title)).to_have_text("Buat Resume Terbaikmu")

    async def info_section_title_presence(self):
        await self._look(ResumeInfo.title)
        await expect(self._find(ResumeInfo.title)).to_have_text("Informasi Resume")

    async def info_resume_name_presence(self):
        await self._look(ResumeInfo.name_label)
        await expect(self._find(ResumeInfo.name_label)).to_have_text("Nama Resume")

        await self._touch(ResumeInfo.name_input)
        await expect(self._find(ResumeInfo.name_input)).to_have_attribute("placeholder", "Yoga 2 Januari 2023")

    async def info_resume_language_presence(self):
        await self._touch(ResumeInfo.lang_label)
        await expect(self._find(ResumeInfo.lang_label)).to_have_text("Bahasa Resume")

        await self._touch(ResumeInfo.lang_input)
        await expect(self._find(ResumeInfo.lang_input)).to_have_text("Bahasa Indonesia")

    async def info_resume_goal_title_presence(self):
        await self._touch(ResumeInfo.goal_label)
        await expect(self._find(ResumeInfo.goal_label)).to_have_text('Tujuan Pekerjaan')

    async def info_resume_tujuan_presence(self):
        await self._touch(ResumeInfo.goal_desc)
        await expect(self._find(ResumeInfo.goal_desc)).to_contain_text('memberikan rekomendasi')

        await self._touch(ResumeInfo.goal_input)
        await expect(self._find(ResumeInfo.goal_content_empty)).to_have_text('Pilih kategori pekerjaan')

    async def info_resume_import_data_presence(self):
        await self._touch(ResumeInfo.import_btn)
        await expect(self._find(ResumeInfo.import_btn)).to_have_text(" Impor Data")

    async def import_data_modal_presence(self):
        await self._look(ResumeInfo.import_modal)
        await expect(self._find(ResumeInfo.import_modal)).to_be_visible()

    """ Resume Information - Import Data Validation"""
    async def import_data_modal_title_presence(self):
        await self._look(ResumeInfo.ImportModal.title)
        await expect(self._find(ResumeInfo.ImportModal.title)).to_have_text('Impor Data')

    async def import_data_modal_info_presence(self):
        await self._look(ResumeInfo.ImportModal.desc)
        await expect(self._find(ResumeInfo.ImportModal.desc)).to_have_text('Pilih sumber data untuk di impor :')

    async def import_data_modal_close_presence(self):
        await self._look(ResumeInfo.ImportModal.close)
        await expect(self._find(ResumeInfo.ImportModal.close)).to_be_enabled()

    async def import_data_myProfile_carousel_presence(self):
        await self._touch(ResumeInfo.ImportModal.my_profile)
        await expect(self._find(ResumeInfo.ImportModal.my_profile)).to_have_text('Impor dari profil saya')

    async def import_data_myResume_carousel_presence(self):
        await self._touch(ResumeInfo.ImportModal.my_resume)
        await expect(self._find(ResumeInfo.ImportModal.my_resume)).to_have_text('Impor dari resume saya')

    """ Resume Information - Import Data Interaction"""
    async def import_data_modal_click_close(self):
        await self._click(ResumeInfo.ImportModal.close)
        await expect(self._find(ResumeInfo.import_modal)).not_to_be_visible()

    async def import_data_modal_click_my_profile(self):
        await self._click(ResumeInfo.ImportModal.my_profile)
        await expect(self._find(ResumeInfo.ImportModal.my_profile)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).to_be_visible()

    async def import_data_modal_click_my_resume(self):
        await self._click(ResumeInfo.ImportModal.my_resume)
        await expect(self._find(ResumeInfo.ImportModal.main_form)).to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.my_resume)).not_to_be_visible()

    """ Resume Information - Import Data - Import Via Profile Validation"""
    async def import_profile_modal_title_presence(self):
        await self._look(ResumeInfo.ImportModal.Profile.title)
        await expect(self._find(ResumeInfo.ImportModal.Profile.title)).to_have_text('Impor Profile')

    async def import_profile_modal_info_presence(self):
        await self._look(ResumeInfo.ImportModal.Profile.desc)
        await expect(self._find(ResumeInfo.ImportModal.Profile.desc)).to_contain_text('resume dari profil saya')

    async def import_profile_modal_back_arrow_presence(self):
        await self._look(ResumeInfo.ImportModal.Profile.back_chevron)

        await expect(self._find(ResumeInfo.ImportModal.Profile.back_chevron)).to_be_enabled()
        await expect(self._find(ResumeInfo.ImportModal.Profile.back_chevron)).to_have_text(
            "Kembali ke pilih sumber data")

    async def import_profile_modal_form_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_main)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).to_be_visible()

    async def import_profile_self_data_form_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_main)

        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_title)).to_have_text("Data Diri")

    async def import_profile_self_data_check_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_check)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).to_be_enabled()
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).to_be_checked()

    async def import_profile_self_data_name_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_name)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_name)).not_to_have_text("")

    async def import_profile_self_data_email_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_email)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_email)).not_to_have_text("")

    async def import_profile_self_data_phone_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_phone)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_phone)).not_to_have_text("")

    async def import_profile_self_data_province_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_prov)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_prov)).not_to_have_text("")

    async def import_profile_self_data_city_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_city)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_city)).not_to_have_text("")

    """ Resume Information - Import Data - Import Via Resume Validation"""
    async def import_resume_modal_title_presence(self):
        await self._look(ResumeInfo.ImportModal.Resume.title)
        await expect(self._find(ResumeInfo.ImportModal.Resume.title)).to_have_text('Impor Resume')

    async def import_resume_modal_info_presence(self):
        await self._look(ResumeInfo.ImportModal.Resume.desc)
        await expect(self._find(ResumeInfo.ImportModal.Resume.desc)).to_contain_text('dari resume yang telah kamu buat')

    async def import_resume_modal_back_arrow_presence(self):
        await self._look(ResumeInfo.ImportModal.Resume.back_chevron)

        await expect(self._find(ResumeInfo.ImportModal.Resume.back_chevron)).to_be_enabled()
        await expect(self._find(ResumeInfo.ImportModal.Resume.back_chevron)).to_have_text(
            "Kembali ke pilih sumber data")

    async def import_resume_input_name_presence(self):
        await self._look(ResumeInfo.ImportModal.Resume.input_wrapper)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_wrapper)).to_be_enabled()
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_empty)).to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_empty)).to_have_text('Search by resume name')

    async def import_resume_cancel_button_presence(self):
        await self._look(ResumeInfo.ImportModal.Resume.cancel)
        await expect(self._find(ResumeInfo.ImportModal.Resume.cancel)).to_be_enabled()
        await expect(self._find(ResumeInfo.ImportModal.Resume.cancel)).to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.Resume.cancel)).to_have_text('Batal')

    async def import_resume_save_button_presence(self):
        await self._look(ResumeInfo.ImportModal.Resume.save)
        await expect(self._find(ResumeInfo.ImportModal.Resume.save)).to_be_disabled()
        await expect(self._find(ResumeInfo.ImportModal.Resume.save)).to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.Resume.save)).to_have_text('Simpan')

    """ Resume Information - Import Data - Import Via Profile Interaction"""
    async def import_profile_modal_click_back_arrow(self):
        await self._click(ResumeInfo.ImportModal.Profile.back_chevron)
        await expect(self._find(ResumeInfo.ImportModal.Profile.back_chevron)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).not_to_be_visible()

    async def import_profile_collapse_self_data(self):
        await self._click(ResumeInfo.ImportModal.DataForm.info_toggle)
        await self._conceal(ResumeInfo.ImportModal.DataForm.info_name)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_toggle)).to_have_attribute('aria-expanded', 'false')

    async def import_profile_expand_self_data(self):
        await self._click(ResumeInfo.ImportModal.DataForm.info_toggle)
        await self._look(ResumeInfo.ImportModal.DataForm.info_name)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_toggle)).to_have_attribute('aria-expanded', 'true')

    async def import_profile_modal_click_cancel(self):
        await self._click(ResumeInfo.ImportModal.Profile.cancel)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    async def import_profile_modal_click_save(self):
        await self._click(ResumeInfo.ImportModal.Profile.save)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    async def import_profile_modal_click_close(self):
        await self._click(ResumeInfo.ImportModal.close)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    """ Resume Information - Import Data - Import Via Resume Interaction"""
    async def import_resume_modal_click_back_arrow(self):
        await self._click(ResumeInfo.ImportModal.Resume.back_chevron)
        await expect(self._find(ResumeInfo.ImportModal.Resume.back_chevron)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.Resume.title)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_wrapper)).not_to_be_visible()
    #
    # async def import_resume_collapse_self_data(self):
    #     await self._click(ResumeInfo.ImportModal.Resume.info_toggle)
    #     await self._conceal(ResumeInfo.ImportModal.Resume.info_name)
    #     await expect(self._find(ResumeInfo.ImportModal.Resume.info_toggle)).to_have_attribute('aria-expanded', 'false')
    #
    # async def import_resume_expand_self_data(self):
    #     await self._click(ResumeInfo.ImportModal.Resume.info_toggle)
    #     await self._look(ResumeInfo.ImportModal.Resume.info_name)
    #     await expect(self._find(ResumeInfo.ImportModal.Resume.info_toggle)).to_have_attribute('aria-expanded', 'true')

    async def _import_resume_item_count(self):
        await self._look(ResumeInfo.ImportModal.Resume.input_lists)
        return await self._find(ResumeInfo.ImportModal.Resume.input_item).count()

    async def import_resume_modal_click_input(self):
        await self._click(ResumeInfo.ImportModal.Resume.input_wrapper)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_lists)).to_be_visible(timeout=10000)
        item_collect = await self._import_resume_item_count()
        print(f"Retrieved resume: {item_collect} items")

    async def import_resume_modal_click_cancel(self):
        await self._click(ResumeInfo.ImportModal.Resume.cancel)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_wrapper)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    async def import_resume_modal_click_save(self):
        await self._click(ResumeInfo.ImportModal.Resume.save)
        await expect(self._find(ResumeInfo.ImportModal.Resume.info_main)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    async def import_resume_modal_click_close(self):
        await self._click(ResumeInfo.ImportModal.close)
        await expect(self._find(ResumeInfo.ImportModal.Resume.title)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()
    
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
            await expect(self._find(ResumeInfo.goal_content_selected)).to_have_attribute('title', opt_label)
            await self.info_resume_goal_click()

    async def info_resume_import_data_click(self):
        await self._click(ResumeInfo.import_btn)
        await expect(self._find(ResumeInfo.import_btn)).to_be_focused()

    """Personal Information Section Validation"""
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
        await expect(self._find(DataDiri.email_input)).to_have_attribute("placeholder", "johndoe@gmail.com")

    async def self_info_phone_presence(self):
        await self._look(DataDiri.phone_label)
        await expect(self._find(DataDiri.phone_label)).to_have_text("No. Telepon")

        await self._touch(DataDiri.phone_input)
        await expect(self._find(DataDiri.phone_input)).to_be_empty()
        await expect(self._find(DataDiri.phone_input)).to_have_attribute("placeholder", "081234567890")

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
        await expect(self._find(DataDiri.address_input)).to_have_attribute('placeholder', 'Gambir, 10150')

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
        await self.self_info_click_country()
        await self._force(DataDiri.country_wni)
        await expect(self._find(DataDiri.country_content)).to_have_attribute('title', 'Indonesia')

    async def self_info_select_wna(self):
        await self.self_info_click_country()
        await self._force(DataDiri.country_wna)
        await expect(self._find(DataDiri.country_content)).to_have_attribute('title', 'Luar Indonesia')

    async def self_info_prov_insert(self, text: str):
        await self._type(DataDiri.province_input, text)
        await expect(self._find(DataDiri.province_input)).to_have_value(text)
        await expect(self._find(DataDiri.province_lists)).to_be_attached()

    async def self_info_prov_click_filled(self):
        await self._click(DataDiri.province_selected)
        await expect(self._find(DataDiri.province_input)).to_be_focused()
        await expect(self._find(DataDiri.province_lists)).to_be_visible()

    async def self_info_prov_select_option_within(self, text):
        await self.self_info_prov_insert(text)
        count = await self._find(DataDiri.province_item).count()

        for x in range(1, count + 1):
            await self._click(f"{DataDiri.province_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick the input field
            if x != count:
                await self.self_info_prov_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(DataDiri.province_lists)).not_to_be_visible()
        await expect(self._find(DataDiri.city_input)).to_be_enabled()

    async def self_info_city_insert(self, text: str):
        await self._type(DataDiri.city_input, text)
        await expect(self._find(DataDiri.city_input)).to_have_value(text)
        await expect(self._find(DataDiri.city_lists)).to_be_attached()

    async def self_info_city_click_filled(self):
        await self._click(DataDiri.city_selected)
        await expect(self._find(DataDiri.city_input)).to_be_focused()
        await expect(self._find(DataDiri.city_lists)).to_be_visible()

    async def self_info_city_select_option_within(self, text):
        await self.self_info_city_insert(text)
        count = await self._find(DataDiri.city_item).count()
        for x in range(1, count + 1):
            await self._click(f"{DataDiri.city_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick input field
            if x != count:
                await self.self_info_city_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(DataDiri.city_lists)).not_to_be_visible()

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

    """Education History Validation"""
    async def edu_title_presence(self):
        await self._look(EduHistory.title)
        await expect(self._find(EduHistory.title)).to_have_text("Riwayat Pendidikan")

    async def edu_desc_presence(self):
        await self._look(EduHistory.description)
        await expect(self._find(EduHistory.description)).to_contain_text("Tambah riwayat pendidikan")

    async def edu_main_hints_presence(self):
        await self._look(EduHistory.hint_main)
        await expect(self._find(EduHistory.hint_main)).to_be_visible()

    async def edu_hints_title_presence(self):
        await self._look(EduHistory.hint_title)
        await expect(self._find(EduHistory.hint_title)).to_have_text('Tips Professional')

    async def edu_hints_desc_presence(self):
        await self._look(EduHistory.hint_desc)
        await expect(self._find(EduHistory.hint_desc)).to_contain_text('Sertakan pendidikan terakhir')

    async def edu_add_form_button_presence(self):
        await self._touch(EduHistory.add_btn)
        await expect(self._find(EduHistory.add_btn)).to_have_text("Riwayat Pendidikan")

    async def edu_degree_presence(self):
        await self._look(EduHistory.degree_label)
        await expect(self._find(EduHistory.degree_label)).to_have_text("Jenjang Pendidikan")

        await self._touch(EduHistory.degree_input)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute("title", 'Sarjana (S1)')

    async def edu_institution_presence(self):
        await self._look(EduHistory.name_label)
        await expect(self._find(EduHistory.name_label)).to_have_text("Nama Institusi")

        await self._touch(EduHistory.name_input)
        await expect(self._find(EduHistory.name_input)).to_be_empty()
        await expect(self._find(EduHistory.name_empty)).to_have_text("Universitas Cirebon")

    async def edu_faculty_presence(self):
        await self._look(EduHistory.faculty_label)
        await expect(self._find(EduHistory.faculty_label)).to_have_text("Jurusan")

        await self._touch(EduHistory.faculty_input)
        await expect(self._find(EduHistory.faculty_input)).to_be_empty()
        await expect(self._find(EduHistory.faculty_empty)).to_have_text("Hukum")

    async def edu_gpa_presence(self):
        await self._look(EduHistory.gpa_label)
        await expect(self._find(EduHistory.gpa_label)).to_have_text("IPK atau Nilai")

        await self._touch(EduHistory.gpa_input)
        await expect(self._find(EduHistory.gpa_input)).to_have_value('0')

        await expect(self._find(EduHistory.gpa_increase)).to_be_enabled()
        await expect(self._find(EduHistory.gpa_decrease)).to_be_enabled()

    async def edu_max_score_presence(self):
        await self._look(EduHistory.max_gpa_label)
        await expect(self._find(EduHistory.max_gpa_label)).to_have_text("Skala Maximum")

        await self._touch(EduHistory.max_gpa_input)
        await expect(self._find(EduHistory.max_gpa_input)).to_have_value('0')

        await expect(self._find(EduHistory.max_gpa_increase)).to_be_enabled()
        await expect(self._find(EduHistory.max_gpa_decrease)).to_be_enabled()

    async def edu_country_presence(self):
        await self._look(EduHistory.country_label)
        await expect(self._find(EduHistory.country_label)).to_have_text("Negara Institusi")

        await self._touch(EduHistory.country_input)
        await expect(self._find(EduHistory.country_content)).to_have_attribute("title", "Indonesia")

    async def edu_prov_presence(self):
        await self._look(EduHistory.province_label)
        await expect(self._find(EduHistory.province_label)).to_have_text("Provinsi Institusi")

        await self._touch(EduHistory.province_input)
        await expect(self._find(EduHistory.province_input)).to_be_empty()
        await expect(self._find(EduHistory.province_empty)).to_have_text("Jawa Barat")

    async def edu_city_presence(self):
        await self._look(EduHistory.city_label)
        await expect(self._find(EduHistory.city_label)).to_have_text("Kota Institusi")

        await self._touch(EduHistory.city_input)
        await expect(self._find(EduHistory.city_input)).to_be_empty()
        await expect(self._find(EduHistory.city_empty)).to_have_text("Cirebon")

    async def edu_start_presence(self):
        await self._look(EduHistory.start_label)
        await expect(self._find(EduHistory.start_label)).to_have_text("Waktu Mulai")

        await self._touch(EduHistory.start_input)
        await expect(self._find(EduHistory.start_input)).to_be_empty()
        await expect(self._find(EduHistory.start_input)).to_have_attribute("placeholder", "Pilih Waktu Mulai")

    async def edu_end_presence(self):
        await self._look(EduHistory.end_label)
        await expect(self._find(EduHistory.end_label)).to_have_text("Waktu Lulus")

        await self._touch(EduHistory.end_input)
        await expect(self._find(EduHistory.end_input)).to_be_empty()
        await expect(self._find(EduHistory.end_input)).to_have_attribute("placeholder", "Masih Aktif")

        await self._touch(EduHistory.end_status)
        await expect(self._find(EduHistory.end_status)).to_have_text("Pendidikan masih aktif")
        await expect(self._find(EduHistory.end_status_check)).to_be_checked()

    async def edu_cancel_form_btn_presence(self):
        await self._touch(EduHistory.cancel_btn)
        await expect(self._find(EduHistory.cancel_btn)).to_have_text("Batal")

    async def edu_save_form_btn_presence(self):
        await self._touch(EduHistory.save_btn)
        await expect(self._find(EduHistory.save_btn)).to_have_text("Simpan")

    """Education History Interaction"""
    async def edu_title_click_collapse(self):
        await self._click(EduHistory.toggle)
        await expect(self._find(EduHistory.add_btn)).to_be_hidden()
        await expect(self._find(EduHistory.toggle)).to_have_attribute('aria-expanded', 'false')

    async def edu_title_click_expand(self):
        await self._click(EduHistory.toggle)
        await expect(self._find(EduHistory.add_btn)).to_be_visible()
        await expect(self._find(EduHistory.toggle)).to_have_attribute('aria-expanded', 'true')

    async def edu_click_add_form(self):
        await self._click(EduHistory.add_btn)
        await expect(self._find(EduHistory.add_btn)).to_be_focused()

    async def edu_hints_click_show(self):
        await self._click(EduHistory.hint_btn)
        await expect(self._find(EduHistory.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(EduHistory.hint_desc)).not_to_be_hidden()

    async def edu_hints_click_hide(self):
        await self._click(EduHistory.hint_btn)
        await expect(self._find(EduHistory.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(EduHistory.hint_desc)).to_be_hidden()

    async def edu_click_degree(self):
        await self._force(EduHistory.degree_input)
        await expect(self._find(EduHistory.degree_lists)).to_be_visible()

    async def edu_click_degree_sma(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_sma)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'SMA/SMK/Sederajat')

    async def edu_click_degree_d1(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d1)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Ahli Pratama (D1)')

    async def edu_click_degree_d2(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d2)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Ahli Muda (D2)')

    async def edu_click_degree_d3(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d3)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Ahli Madya (D3)')

    async def edu_click_degree_d4(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d4)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Sarjana Sains Terapan (D4)')

    async def edu_click_degree_s1(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_s1)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Sarjana (S1)')

    async def edu_click_degree_s2(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_s2)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Magister (S2)')

    async def edu_click_degree_s3(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_s3)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Doktor (S3)')

    async def edu_click_degree_course(self):
        await self.edu_click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_course)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Kursus & Pelatihan')

    async def edu_institution_insert(self, text):
        await self._type(EduHistory.name_input, text)
        await expect(self._find(EduHistory.name_list)).to_be_visible(timeout=20000)
        await expect(self._find(EduHistory.name_add)).to_contain_text(text)

    async def edu_institution_click_filled(self):
        await self._click(EduHistory.name_selected)
        await expect(self._find(EduHistory.name_input)).to_be_focused()
        await expect(self._find(EduHistory.name_list)).to_be_visible()

    async def edu_institution_select_option_within(self, text):
        await self.edu_institution_insert(text)
        count = await self._find(EduHistory.name_item).count()
        for x in range(1, count + 1):
            await self._click(f"{EduHistory.name_item}[{x}]")
            await self._click(".ant-layout-content")
            await self.edu_institution_click_filled()

    async def edu_faculty_insert(self, text):
        await self._type(EduHistory.faculty_input, text)
        await expect(self._find(EduHistory.faculty_list)).to_be_visible()
        await expect(self._find(EduHistory.faculty_add)).to_contain_text(text)

    async def edu_faculty_click_filled(self):
        await self._force(EduHistory.faculty_selected)
        await expect(self._find(EduHistory.faculty_input)).to_be_focused()
        await expect(self._find(EduHistory.faculty_list)).to_be_visible()

    async def faculty_select_option_within(self, text):
        await self.edu_faculty_insert(text)
        for x in range(1, 6):
            await self._click(f"{EduHistory.faculty_item}[{x}]")
            await self._click(".ant-layout-content")
            await self.edu_faculty_click_filled()

    async def faculty_gpa_insert(self, text: str):
        await self._type(EduHistory.gpa_input, text)
        await expect(self._find(EduHistory.gpa_input)).to_be_focused()
        await expect(self._find(EduHistory.gpa_input)).to_have_value(text)

    async def faculty_gpa_score_increase(self, step: int):
        current_score = float(await self._find(EduHistory.gpa_input).get_attribute('value'))
        for x in range(step):
            await self._click(EduHistory.gpa_increase)
        await expect(self._find(EduHistory.gpa_input)).to_have_value(str(current_score + step))

    async def faculty_gpa_score_decrease(self, step: int):
        current_score = float(await self._find(EduHistory.gpa_input).get_attribute('value'))
        for x in range(step):
            await self._click(EduHistory.gpa_decrease)
        await expect(self._find(EduHistory.gpa_input)).to_have_value(str(current_score - step))

    async def faculty_max_gpa_insert(self, text: str):
        await self._type(EduHistory.max_gpa_input, text)
        await expect(self._find(EduHistory.max_gpa_input)).to_be_focused()
        await expect(self._find(EduHistory.max_gpa_input)).to_have_value(text)

    async def faculty_max_gpa_score_increase(self, step: int):
        current_score = float(await self._find(EduHistory.max_gpa_input).get_attribute('value'))
        for x in range(step):
            await self._click(EduHistory.max_gpa_increase)
        await expect(self._find(EduHistory.max_gpa_input)).to_have_value(str(current_score + step))

    async def faculty_max_gpa_score_decrease(self, step: int):
        current_score = float(await self._find(EduHistory.max_gpa_input).get_attribute('value'))
        for x in range(step):
            await self._click(EduHistory.max_gpa_decrease)
        await expect(self._find(EduHistory.max_gpa_input)).to_have_value(str(current_score - step))

    async def edu_click_country(self):
        await self._click(EduHistory.country_input)
        await expect(self._find(EduHistory.country_lists)).to_be_visible()

    async def edu_select_wni(self):
        await self.edu_click_country()

        await self._click(EduHistory.country_wni)
        await expect(self._find(EduHistory.country_content)).to_have_attribute('title', 'Indonesia')

    async def edu_select_wna(self):
        await self.edu_click_country()

        await self._click(EduHistory.country_wna)
        await expect(self._find(EduHistory.country_content)).to_have_attribute('title', 'Luar Indonesia')

    async def edu_prov_click_filled(self):
        await self._force(EduHistory.province_selected)
        await expect(self._find(EduHistory.province_input)).to_be_focused()
        await expect(self._find(EduHistory.province_lists)).to_be_visible()

    async def edu_prov_insert(self, text: str):
        await self._type(EduHistory.province_input, text)
        await expect(self._find(EduHistory.province_input)).to_have_value(text)
        await expect(self._find(EduHistory.province_lists)).to_be_visible()

    async def edu_prov_select_option_within(self, text):
        await self.edu_prov_insert(text)
        count = await self._find(EduHistory.province_item).count()

        for x in range(1, count + 1):
            await self._click(f"{EduHistory.province_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick the input field
            if x != count:
                await self.edu_prov_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(EduHistory.province_lists)).not_to_be_visible()
        await expect(self._find(EduHistory.city_input)).to_be_enabled()

    async def edu_city_click_filled(self):
        await self._force(EduHistory.city_selected)
        await expect(self._find(EduHistory.city_input)).to_be_focused()
        await expect(self._find(EduHistory.city_lists)).to_be_visible()

    async def edu_city_insert(self, text: str):
        await self._type(EduHistory.city_input, text)
        await expect(self._find(EduHistory.city_input)).to_have_value(text)
        await expect(self._find(EduHistory.city_lists)).to_be_visible()

    async def edu_city_select_option_within(self, text):
        await self.edu_city_insert(text)
        count = await self._find(EduHistory.city_item).count()
        for x in range(1, count + 1):
            await self._click(f"{EduHistory.city_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick input field
            if x != count:
                await self.edu_city_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(EduHistory.city_lists)).not_to_be_visible()

    async def edu_start_date_insert(self, month: str, year: int):
        await self._click(EduHistory.start_input)
        await expect(self._find(EduHistory.start_input)).to_be_focused()

        await self._type(EduHistory.start_input, f"{month} - {year}")
        await self._find(EduHistory.start_input).press("Enter")
        await expect(self._find(EduHistory.start_input)).to_have_value(f"{month} - {year}")

    async def edu_start_date_clear(self):
        await self._click(EduHistory.start_clear)
        await expect(self._find(EduHistory.start_input)).to_be_focused()

    async def edu_end_date_insert(self, month: str, year: int):
        await self._click(EduHistory.end_input)
        await expect(self._find(EduHistory.end_input)).to_be_focused()

        await self._type(EduHistory.end_input, f"{month} - {year}")
        await self._find(EduHistory.end_input).press("Enter")
        await expect(self._find(EduHistory.end_input)).to_have_value(f"{month} - {year}")

    async def edu_end_active_checking(self):
        await expect(self._find(EduHistory.end_status_check)).not_to_be_checked()

        await self._click(EduHistory.end_status_check)
        await expect(self._find(EduHistory.end_status_check)).to_be_checked()
        await expect(self._find(EduHistory.end_input)).to_be_disabled()

    async def edu_end_active_unchecking(self):
        await expect(self._find(EduHistory.end_status_check)).to_be_checked()

        await self._click(EduHistory.end_status_check)
        await expect(self._find(EduHistory.end_status_check)).not_to_be_checked()
        await expect(self._find(EduHistory.end_input)).to_be_enabled()

    async def edu_end_date_clear(self):
        await self._force(EduHistory.end_clear)
        await expect(self._find(EduHistory.start_input)).to_have_value("")

    async def edu_save_btn_click(self):
        await self._click(EduHistory.save_btn)
        await expect(self._find(EduHistory.save_btn)).to_be_focused()

    async def edu_cancel_btn_click(self):
        await self._click(EduHistory.cancel_btn)

        await expect(self._find(EduHistory.cancel_btn)).not_to_be_attached()
        await expect(self._find(EduHistory.hint_desc)).not_to_be_attached()
        await expect(self._find(EduHistory.description)).to_be_visible()

    """Work History Validation"""
    async def job_title_presence(self):
        await self._look(JobHistory.title)
        await expect(self._find(JobHistory.title)).to_have_text("Riwayat Pekerjaan")

    async def job_desc_presence(self):
        await self._look(JobHistory.description)
        await expect(self._find(JobHistory.description)).to_contain_text("Tambah riwayat pekerjaan")

    async def job_main_hints_presence(self):
        await self._look(JobHistory.hint_main)
        await expect(self._find(JobHistory.hint_main)).to_be_visible()

    async def job_hints_title_presence(self):
        await self._look(JobHistory.hint_title)
        await expect(self._find(JobHistory.hint_title)).to_have_text('Tips Professional')

    async def job_hints_desc_presence(self):
        await self._look(JobHistory.hint_desc)
        await expect(self._find(JobHistory.hint_desc)).to_contain_text('Cantumkan pengalaman magang')

    async def job_add_form_button_presence(self):
        await self._touch(JobHistory.add_btn)
        await expect(self._find(JobHistory.add_btn)).to_have_text("Riwayat Pekerjaan")

    async def job_position_presence(self):
        await self._look(JobHistory.pos_label)
        await expect(self._find(JobHistory.pos_label)).to_have_text("Posisi")

        await self._touch(JobHistory.pos_input)
        await expect(self._find(JobHistory.pos_input)).to_be_empty()
        await expect(self._find(JobHistory.pos_empty)).to_have_text("Sales Analyst")

    async def job_company_name_presence(self):
        await self._look(JobHistory.company_label)
        await expect(self._find(JobHistory.company_label)).to_have_text("Nama Perusahaan")

        await self._touch(JobHistory.company_input)
        await expect(self._find(JobHistory.company_input)).to_have_attribute("placeholder", "PT. ABC")

    async def job_country_presence(self):
        await self._look(JobHistory.country_label)
        await expect(self._find(JobHistory.country_label)).to_have_text("Negara Perusahaan/Organisasi")

        await self._touch(JobHistory.country_input)
        await expect(self._find(JobHistory.country_content)).to_have_attribute("title", "Indonesia")

    async def job_prov_presence(self):
        await self._look(JobHistory.province_label)
        await expect(self._find(JobHistory.province_label)).to_have_text("Provinsi Perusahaan/Organisasi")

        await self._touch(JobHistory.province_input)
        await expect(self._find(JobHistory.province_input)).to_be_empty()
        await expect(self._find(JobHistory.province_empty)).to_have_text("Jawa Barat")

    async def job_city_presence(self):
        await self._look(JobHistory.city_label)
        await expect(self._find(JobHistory.city_label)).to_have_text("Kota Perusahaan/Organisasi")

        await self._touch(JobHistory.city_input)
        await expect(self._find(JobHistory.city_input)).to_be_empty()
        await expect(self._find(JobHistory.city_empty)).to_have_text("Cirebon")

    async def job_status_presence(self):
        await self._look(JobHistory.status_label)
        await expect(self._find(JobHistory.status_label)).to_have_text("Status Pekerjaan")

        await self._touch(JobHistory.status_input)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Purnawaktu')

    async def job_start_presence(self):
        await self._look(JobHistory.start_label)
        await expect(self._find(JobHistory.start_label)).to_have_text("Waktu Mulai")

        await self._touch(JobHistory.start_input)
        await expect(self._find(JobHistory.start_input)).to_be_empty()
        await expect(self._find(JobHistory.start_input)).to_have_attribute("placeholder", "Pilih Waktu Mulai")

    async def job_end_presence(self):
        await self._look(JobHistory.end_label)
        await expect(self._find(JobHistory.end_label)).to_have_text("Waktu Selesai")

        await self._touch(JobHistory.end_input)
        await expect(self._find(JobHistory.end_input)).to_be_empty()
        await expect(self._find(JobHistory.end_input)).to_have_attribute("placeholder", "Masih Aktif")

        await self._touch(JobHistory.end_status)
        await expect(self._find(JobHistory.end_status)).to_have_text("Posisi masih aktif")
        await expect(self._find(JobHistory.end_status_check)).to_be_checked()

    async def job_cancel_form_btn_presence(self):
        await self._touch(JobHistory.form_cancel)
        await expect(self._find(JobHistory.form_cancel)).to_have_text("Batal")

    async def job_save_form_btn_presence(self):
        await self._touch(JobHistory.form_save)
        await expect(self._find(JobHistory.form_save)).to_have_text("Simpan")

    """Work History Interaction"""

    async def job_title_click_collapse(self):
        await self._click(JobHistory.toggle)
        await expect(self._find(JobHistory.add_btn)).to_be_hidden()
        await expect(self._find(JobHistory.toggle)).to_have_attribute('aria-expanded', 'false')

    async def job_title_click_expand(self):
        await self._click(JobHistory.toggle)
        await expect(self._find(JobHistory.add_btn)).to_be_visible()
        await expect(self._find(JobHistory.toggle)).to_have_attribute('aria-expanded', 'true')

    async def job_click_add_form(self):
        await self._click(JobHistory.add_btn)
        await expect(self._find(JobHistory.add_btn)).to_be_focused()

    async def job_hints_click_show(self):
        await self._click(JobHistory.hint_btn)
        await expect(self._find(JobHistory.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(JobHistory.hint_desc)).not_to_be_hidden()

    async def job_hints_click_hide(self):
        await self._click(JobHistory.hint_btn)
        await expect(self._find(JobHistory.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(JobHistory.hint_desc)).to_be_hidden()

    async def job_position_insert(self, text):
        await self._type(JobHistory.pos_input, text)
        await expect(self._find(JobHistory.pos_list)).to_be_visible()
        await expect(self._find(JobHistory.pos_add)).to_contain_text(text)

    async def job_position_click_filled(self):
        await self._click(JobHistory.pos_selected)
        await expect(self._find(JobHistory.pos_input)).to_be_focused()
        await expect(self._find(JobHistory.pos_list)).to_be_visible()

    async def job_position_select_option_within(self, text):
        await self.job_position_insert(text)
        jobs = await self._find(JobHistory.pos_item).count()
        for x in range(1, jobs):
            await self._click(f"{JobHistory.pos_item}[{x + 1}]")
            await self._click(".ant-layout-content")
            await self.job_position_click_filled()

    async def job_company_name_insert(self, text: str):
        await self._type(JobHistory.company_input, text)
        await expect(self._find(JobHistory.company_input)).to_be_focused()
        await expect(self._find(JobHistory.company_input)).to_have_value(text)

    async def job_click_country(self):
        await self._click(JobHistory.country_input)
        await expect(self._find(JobHistory.country_lists)).to_be_visible()

    async def job_select_wni(self):
        await self.job_click_country()
        await self._force(JobHistory.country_wni)
        await expect(self._find(JobHistory.country_content)).to_have_attribute('title', 'Indonesia')

    async def job_select_wna(self):
        await self.job_click_country()
        await self._force(JobHistory.country_wna)
        await expect(self._find(JobHistory.country_content)).to_have_attribute('title', 'Luar Indonesia')

    async def job_prov_click_filled(self):
        await self._force(JobHistory.province_selected)
        await expect(self._find(JobHistory.province_input)).to_be_focused()
        await expect(self._find(JobHistory.province_lists)).to_be_visible()

    async def job_prov_insert(self, text: str):
        await self._type(JobHistory.province_input, text)
        await expect(self._find(JobHistory.province_input)).to_have_value(text)
        await expect(self._find(JobHistory.province_lists)).to_be_visible()

    async def job_prov_select_option_within(self, text):
        await self.job_prov_insert(text)
        count = await self._find(JobHistory.province_item).count()

        for x in range(1, count + 1):
            await self._click(f"{JobHistory.province_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick the input field
            if x != count:
                await self.job_prov_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(JobHistory.province_lists)).not_to_be_visible()
        await expect(self._find(JobHistory.city_input)).to_be_enabled()

    async def job_city_click_filled(self):
        await self._force(JobHistory.city_selected)
        await expect(self._find(JobHistory.city_input)).to_be_focused()
        await expect(self._find(JobHistory.city_lists)).to_be_visible()

    async def job_city_insert(self, text: str):
        await self._type(JobHistory.city_input, text)
        await expect(self._find(JobHistory.city_input)).to_have_value(text)
        await expect(self._find(JobHistory.city_lists)).to_be_visible()

    async def job_city_select_option_within(self, text):
        await self.job_city_insert(text)
        count = await self._find(JobHistory.city_item).count()
        for x in range(1, count + 1):
            await self._click(f"{JobHistory.city_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick input field
            if x != count:
                await self.job_city_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(JobHistory.city_lists)).not_to_be_visible()

    async def job_click_status(self):
        await self._force(JobHistory.status_input)
        await expect(self._find(JobHistory.status_lists)).to_be_visible()

    async def job_click_status_full(self):
        await self.job_click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_full)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Purnawaktu')

    async def job_click_status_part(self):
        await self.job_click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_part)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Paruh Waktu')

    async def job_click_status_freelance(self):
        await self.job_click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_freelance)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Pekerja Lepas')

    async def job_click_status_internship(self):
        await self.job_click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_intern)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Magang')

    async def job_click_status_volunteer(self):
        await self.job_click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_volunteer)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Sukarela')

    async def job_start_date_insert(self, month: str, year: int):
        await self._click(JobHistory.start_input)
        await expect(self._find(JobHistory.start_input)).to_be_focused()

        await self._type(JobHistory.start_input, f"{month} - {year}")
        await self._find(JobHistory.start_input).press("Enter")
        await expect(self._find(JobHistory.start_input)).to_have_value(f"{month} - {year}")

    async def job_start_date_clear(self):
        await self._force(JobHistory.start_clear)
        await expect(self._find(JobHistory.start_input)).to_have_value("")

    async def job_end_date_insert(self, month: str, year: int):
        await self._click(JobHistory.end_input)
        await expect(self._find(JobHistory.end_input)).to_be_focused()

        await self._type(JobHistory.end_input, f"{month} - {year}")
        await self._find(JobHistory.end_input).press("Enter")
        await expect(self._find(JobHistory.end_input)).to_have_value(f"{month} - {year}")

    async def job_end_active_checking(self):
        await expect(self._find(JobHistory.end_status_check)).not_to_be_checked()

        await self._click(JobHistory.end_status_check)
        await expect(self._find(JobHistory.end_status_check)).to_be_checked()
        await expect(self._find(JobHistory.end_input)).to_be_disabled()

    async def job_end_active_unchecking(self):
        await expect(self._find(JobHistory.end_status_check)).to_be_checked()

        await self._click(JobHistory.end_status_check)
        await expect(self._find(JobHistory.end_status_check)).not_to_be_checked()
        await expect(self._find(JobHistory.end_input)).to_be_enabled()

    async def job_end_date_clear(self):
        await self._force(JobHistory.end_clear)
        await expect(self._find(JobHistory.start_input)).to_have_value("")

    async def job_save_btn_click(self):
        await self._click(JobHistory.form_save)

    async def job_cancel_btn_click(self):
        await self._click(JobHistory.form_cancel)

        await expect(self._find(JobHistory.form_cancel)).not_to_be_attached()
        await expect(self._find(JobHistory.hint_desc)).not_to_be_attached()
        await expect(self._find(JobHistory.description)).to_be_visible()

    """Keahlian Section Validation"""
    async def skill_main_form_presence(self):
        await self._look(Proficiency.form)
        await expect(self._find(Proficiency.form)).to_be_attached()

    async def skill_title_presence(self):
        await self._look(Proficiency.title)
        await expect(self._find(Proficiency.title)).to_have_text("Keahlian")

    async def skill_desc_presence(self):
        await self._look(Proficiency.description)
        await expect(self._find(Proficiency.description)).to_contain_text("Tambah keahlian untuk")

    async def skill_add_button_presence(self):
        await self._look(Proficiency.add_btn)
        await expect(self._find(Proficiency.add_btn)).to_be_enabled()
        await expect(self._find(Proficiency.add_btn)).to_have_text('Keahlian')

    async def skill_main_hints_presence(self):
        await self._look(Proficiency.hint_main)
        await expect(self._find(Proficiency.hint_main)).to_be_attached()

    async def skill_hints_title_presence(self):
        await self._look(Proficiency.hint_title)
        await expect(self._find(Proficiency.hint_title)).to_have_text('Tips Professional')

    async def skill_hints_desc_presence(self):
        await self._look(Proficiency.hint_desc)
        await expect(self._find(Proficiency.hint_desc)).to_contain_text('Sertakan skills yang relevan')

    async def skill_name_input_presence(self):
        await self._look(Proficiency.name_label)
        await expect(self._find(Proficiency.name_label)).to_have_text("Keahlian")

        await self._touch(Proficiency.name_input)
        await expect(self._find(Proficiency.name_input)).to_have_attribute("placeholder", "Microsoft Office")

    async def skill_level_presence(self):
        await self._look(Proficiency.level_label)
        await expect(self._find(Proficiency.level_label)).to_have_text("Tingkat Keahlian")

        await self._touch(Proficiency.level_input)
        await expect(self._find(Proficiency.level_content)).to_have_attribute("title", "Pemula")

    async def skill_cancel_form_btn_presence(self):
        await self._touch(Proficiency.form_cancel)
        await expect(self._find(Proficiency.form_cancel)).to_have_text("Batal")

    async def skill_save_form_btn_presence(self):
        await self._touch(Proficiency.form_save)
        await expect(self._find(Proficiency.form_save)).to_have_text("Simpan")

    """Keahlian Section Interaction"""
    async def skill_title_click_collapse(self):
        await self._click(Proficiency.toggle)
        await expect(self._find(Proficiency.add_btn)).to_be_hidden()
        await expect(self._find(Proficiency.toggle)).to_have_attribute('aria-expanded', 'false')

    async def skill_title_click_expand(self):
        await self._click(Proficiency.toggle)
        await expect(self._find(Proficiency.add_btn)).to_be_visible()
        await expect(self._find(Proficiency.toggle)).to_have_attribute('aria-expanded', 'true')

    async def skill_click_add_form(self):
        await self._click(Proficiency.add_btn)
        await expect(self._find(Proficiency.add_btn)).to_be_focused()

    async def skill_hints_click_show(self):
        await self._click(Proficiency.hint_btn)
        await expect(self._find(Proficiency.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(Proficiency.hint_desc)).not_to_be_hidden()

    async def skill_hints_click_hide(self):
        await self._click(Proficiency.hint_btn)
        await expect(self._find(Proficiency.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(Proficiency.hint_desc)).to_be_hidden()

    async def skill_name_insert(self, text: str):
        await self._type(Proficiency.name_input, text)
        await expect(self._find(Proficiency.name_input)).to_be_focused()
        await expect(self._find(Proficiency.name_input)).to_have_value(text)

    async def skill_name_clear_text(self):
        await self._touch(Proficiency.name_input)
        await expect(self._find(Proficiency.name_input)).to_be_focused()
        await expect(self._find(Proficiency.name_input)).not_to_be_empty()

        await self._find(Proficiency.name_input).clear()
        await expect(self._find(Proficiency.name_input)).to_have_value("")

    async def _skill_level_input_click(self):
        await self._click(Proficiency.level_input)
        await expect(self._find(Proficiency.level_lists)).to_be_visible()

    async def skill_level_click_pemula(self):
        await self._skill_level_input_click()
        await self._force(Proficiency.level_item_pemula)
        await expect(self._find(Proficiency.level_content)).to_have_attribute('title', 'Pemula')

    async def skill_level_click_menengah(self):
        await self._skill_level_input_click()
        await self._force(Proficiency.level_item_menengah)
        await expect(self._find(Proficiency.level_content)).to_have_attribute('title', 'Menengah')

    async def skill_level_click_lanjut(self):
        await self._skill_level_input_click()
        await self._force(Proficiency.level_item_lanjut)
        await expect(self._find(Proficiency.level_content)).to_have_attribute('title', 'Lanjut')

    async def skill_save_form_click(self):
        await self._click(Proficiency.form_save)

    async def skill_cancel_form_click(self):
        await self._click(Proficiency.form_cancel)

        await expect(self._find(Proficiency.form_cancel)).not_to_be_attached()
        await expect(self._find(Proficiency.hint_desc)).not_to_be_attached()
        await expect(self._find(Proficiency.description)).to_be_visible()

    """Achievements & Honor Validation"""
    async def honor_main_form_presence(self):
        await self._look(Achievements.form)
        await expect(self._find(Achievements.form)).to_be_attached()

    async def honor_title_presence(self):
        await self._look(Achievements.title)
        await expect(self._find(Achievements.title)).to_have_text("Prestasi & Penghargaan Non-akademik")

    async def honor_desc_presence(self):
        await self._look(Achievements.description)
        await expect(self._find(Achievements.description)).to_contain_text("Tambah Prestasi dan penghargaan")

    async def honor_add_button_presence(self):
        await self._look(Achievements.add_btn)
        await expect(self._find(Achievements.add_btn)).to_be_enabled()
        await expect(self._find(Achievements.add_btn)).to_have_text(' Prestasi & Penghargaan')

    async def honor_main_hints_presence(self):
        await self._look(Achievements.hint_main)
        await expect(self._find(Achievements.hint_main)).to_be_attached()

    async def honor_hints_title_presence(self):
        await self._look(Achievements.hint_title)
        await expect(self._find(Achievements.hint_title)).to_have_text('Tips Professional')

    async def honor_hints_desc_presence(self):
        await self._look(Achievements.hint_desc)
        await expect(self._find(Achievements.hint_desc)).to_contain_text('Pastikan penulisan award konsisten')

    async def honor_year_presence(self):
        await self._look(Achievements.year_label)
        await expect(self._find(Achievements.year_label)).to_have_text("Tahun")

        await self._touch(Achievements.year_input)
        await expect(self._find(Achievements.year_input)).to_be_empty()
        await expect(self._find(Achievements.year_input)).to_have_attribute("placeholder", "2021")

    async def honor_name_input_presence(self):
        await self._look(Achievements.name_label)
        await expect(self._find(Achievements.name_label)).to_have_text("Prestasi & Penghargaan")

        await self._touch(Achievements.name_input)
        await expect(self._find(Achievements.name_input)).to_have_attribute("placeholder",
                                                                            "Juara 1 Olimpiade Sains Nasional (OSN) "
                                                                            "Matematika Tingkat Nasional")

    async def honor_cancel_form_btn_presence(self):
        await self._touch(Achievements.form_cancel)
        await expect(self._find(Achievements.form_cancel)).to_have_text("Batal")

    async def honor_save_form_btn_presence(self):
        await self._touch(Achievements.form_save)
        await expect(self._find(Achievements.form_save)).to_have_text("Simpan")

    """Achievements & Honor Interaction"""
    async def honor_title_click_collapse(self):
        await self._click(Achievements.toggle)
        await expect(self._find(Achievements.add_btn)).to_be_hidden()
        await expect(self._find(Achievements.toggle)).to_have_attribute('aria-expanded', 'false')

    async def honor_title_click_expand(self):
        await self._click(Achievements.toggle)
        await expect(self._find(Achievements.add_btn)).to_be_visible()
        await expect(self._find(Achievements.toggle)).to_have_attribute('aria-expanded', 'true')

    async def honor_click_add_form(self):
        await self._click(Achievements.add_btn)
        await expect(self._find(Achievements.add_btn)).to_be_focused()

    async def honor_hints_click_show(self):
        await self._click(Achievements.hint_btn)
        await expect(self._find(Achievements.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(Achievements.hint_desc)).not_to_be_hidden()

    async def honor_hints_click_hide(self):
        await self._click(Achievements.hint_btn)
        await expect(self._find(Achievements.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(Achievements.hint_desc)).to_be_hidden()

    async def honor_year_insert(self, year: int):
        await self._click(Achievements.year_input)
        await expect(self._find(Achievements.year_input)).to_be_focused()

        await self._type(Achievements.year_input, str(year))
        await self._find(Achievements.year_input).press("Enter")
        await expect(self._find(Achievements.year_input)).to_have_value(str(year))

    async def honor_year_clear(self):
        await self._click(Achievements.year_clear)
        await expect(self._find(Achievements.year_input)).to_be_focused()

    async def honor_name_insert(self, name: str):
        await self._click(Achievements.name_input)
        await expect(self._find(Achievements.name_input)).to_be_focused()

        await self._type(Achievements.name_input, name)
        await self._find(Achievements.name_input).press("Enter")
        await expect(self._find(Achievements.name_input)).to_have_value(name)

    async def honor_name_clear(self):
        await self._find(Achievements.name_input).clear()

        await expect(self._find(Achievements.name_input)).to_be_focused()
        await expect(self._find(Achievements.name_input)).to_have_value("")

    async def honor_save_form_click(self):
        await self._click(Achievements.form_save)
        await expect(self._find(Achievements.form_save)).to_be_focused()

    async def honor_cancel_form_click(self):
        await self._click(Achievements.form_cancel)

        await expect(self._find(Achievements.form_cancel)).not_to_be_attached()
        await expect(self._find(Achievements.hint_desc)).not_to_be_attached()
        await expect(self._find(Achievements.description)).to_be_visible()

    """Hobby Validation"""
    async def hobby_main_form_presence(self):
        await self._look(Hobby.form)
        await expect(self._find(Hobby.form)).to_be_attached()

    async def hobby_title_presence(self):
        await self._look(Hobby.title)
        await expect(self._find(Hobby.title)).to_have_text("Minat")

    async def hobby_desc_presence(self):
        await self._look(Hobby.desc)
        await expect(self._find(Hobby.desc)).to_contain_text("Tambah Minat untuk membantu perusahaan mengenalimu")

    async def hobby_add_button_presence(self):
        await self._look(Hobby.add_btn)
        await expect(self._find(Hobby.add_btn)).to_be_enabled()
        await expect(self._find(Hobby.add_btn)).to_have_text('Minat')

    async def hobby_main_hints_presence(self):
        await self._look(Hobby.hint_main)
        await expect(self._find(Hobby.hint_main)).to_be_attached()

    async def hobby_hints_title_presence(self):
        await self._look(Hobby.hint_title)
        await expect(self._find(Hobby.hint_title)).to_have_text('Tips Professional')

    async def hobby_hints_desc_presence(self):
        await self._look(Hobby.hint_desc)
        await expect(self._find(Hobby.hint_desc)).to_contain_text('Pikirkan minat yang menarik')

    async def hobby_name_input_presence(self):
        await self._look(Hobby.name_label)
        await expect(self._find(Hobby.name_label)).to_have_text("Minat")

        await self._touch(Hobby.name_input)
        await expect(self._find(Hobby.name_input)).to_be_empty()
        await expect(self._find(Hobby.name_input)).to_have_attribute("placeholder", "Fotografi & Videografi")

    async def hobby_cancel_form_btn_presence(self):
        await self._touch(Hobby.form_cancel)
        await expect(self._find(Hobby.form_cancel)).to_have_text("Batal")

    async def hobby_save_form_btn_presence(self):
        await self._touch(Hobby.form_save)
        await expect(self._find(Hobby.form_save)).to_have_text("Simpan")

    """Hobby Interaction"""
    async def hobby_title_click_collapse(self):
        await self._click(Hobby.toggle)
        await expect(self._find(Hobby.add_btn)).to_be_hidden()
        await expect(self._find(Hobby.toggle)).to_have_attribute('aria-expanded', 'false')

    async def hobby_title_click_expand(self):
        await self._click(Hobby.toggle)
        await expect(self._find(Hobby.add_btn)).to_be_visible()
        await expect(self._find(Hobby.toggle)).to_have_attribute('aria-expanded', 'true')

    async def hobby_click_add_form(self):
        await self._click(Hobby.add_btn)
        await expect(self._find(Hobby.add_btn)).to_be_focused()

    async def hobby_hints_click_show(self):
        await self._click(Hobby.hint_btn)
        await expect(self._find(Hobby.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(Hobby.hint_desc)).not_to_be_hidden()

    async def hobby_hints_click_hide(self):
        await self._click(Hobby.hint_btn)
        await expect(self._find(Hobby.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(Hobby.hint_desc)).to_be_hidden()

    async def hobby_name_insert(self, name: str):
        await self._click(Hobby.name_input)
        await expect(self._find(Hobby.name_input)).to_be_focused()

        await self._type(Hobby.name_input, name)
        await self._find(Hobby.name_input).press("Enter")
        await expect(self._find(Hobby.name_input)).to_have_value(name)

    async def hobby_name_clear(self):
        await self._find(Hobby.name_input).clear()

        await expect(self._find(Hobby.name_input)).to_be_focused()
        await expect(self._find(Hobby.name_input)).to_have_value("")

    async def hobby_save_form_click(self):
        await self._click(Hobby.form_save)
        await expect(self._find(Hobby.form_save)).to_be_focused()

    async def hobby_cancel_form_click(self):
        await self._click(Hobby.form_cancel)

        await expect(self._find(Hobby.form_cancel)).not_to_be_attached()
        await expect(self._find(Hobby.hint_desc)).not_to_be_attached()
        await expect(self._find(Hobby.desc)).to_be_visible()

    # Todo 9: Preview
    # Todo 10: Toast Result Action
