from pages.__base import BasePage
from elements.__res_builder import PageInfo, ResumeInfo, DataDiri
from playwright.async_api import Page, expect


class ResInfo(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Resume Information Section Validation"""
    async def section_title_presence(self):
        await self._look(ResumeInfo.title)
        await expect(self._find(ResumeInfo.title)).to_have_text("Informasi Resume")

    async def name_presence(self):
        await self._look(ResumeInfo.name_label)
        await expect(self._find(ResumeInfo.name_label)).to_have_text("Nama Resume")

        await self._touch(ResumeInfo.name_input)
        await expect(self._find(ResumeInfo.name_input)).to_have_attribute("placeholder", "Yoga 2 Januari 2023")

    async def language_presence(self):
        await self._touch(ResumeInfo.lang_label)
        await expect(self._find(ResumeInfo.lang_label)).to_have_text("Bahasa Resume")

        await self._touch(ResumeInfo.lang_input)
        await expect(self._find(ResumeInfo.lang_input)).to_have_text("Bahasa Indonesia")

    async def tujuan_pekerjaan_presence(self):
        await self._touch(ResumeInfo.goal_label)
        await expect(self._find(ResumeInfo.goal_label)).to_have_text('Tujuan Pekerjaan')

        await self._touch(ResumeInfo.goal_desc)
        await expect(self._find(ResumeInfo.goal_desc)).to_contain_text('memberikan rekomendasi')

        await self._touch(ResumeInfo.goal_input)
        await expect(self._find(ResumeInfo.goal_content_empty)).to_have_text('Pilih kategori pekerjaan')

    async def import_data_presence(self):
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

    async def _import_resume_item_count(self):
        await self._look(ResumeInfo.ImportModal.Resume.input_lists)
        return await self._find(ResumeInfo.ImportModal.Resume.input_item).count()

    async def import_resume_modal_click_input(self):
        await self._click(ResumeInfo.ImportModal.Resume.input_wrapper)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_lists)).to_be_visible(timeout=10000)

    async def import_resume_modal_insert(self, text: str):
        await self._type(ResumeInfo.ImportModal.Resume.input_name, text)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_name)).to_have_value(text)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_lists)).to_be_visible(timeout=10000)

    async def import_resume_modal_select_filled(self):
        await self._click(ResumeInfo.ImportModal.Resume.input_selected)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_lists)).to_be_visible(timeout=10000)

    async def import_resume_modal_click_displayed_option(self):
        count = await self._find(ResumeInfo.ImportModal.Resume.input_item).count()

        for x in range(1, count + 1):
            await self._click(f"{ResumeInfo.ImportModal.Resume.input_item}[{x}]")
            await self.import_resume_modal_select_filled()

        await expect(self._find(DataDiri.province_lists)).not_to_be_visible()
        await expect(self._find(DataDiri.city_input)).to_be_enabled()

    async def import_resume_modal_click_cancel(self):
        await self._click(ResumeInfo.ImportModal.Resume.cancel)
        await expect(self._find(ResumeInfo.ImportModal.Resume.input_wrapper)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    async def import_resume_modal_click_save(self):
        await self._click(ResumeInfo.ImportModal.Resume.save)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    async def import_resume_modal_click_close(self):
        await self._click(ResumeInfo.ImportModal.close)
        await expect(self._find(ResumeInfo.ImportModal.Resume.title)).not_to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.main_form)).not_to_be_visible()

    """Resume Information Section Interaction"""
    async def name_insert(self, text):
        await self._touch(ResumeInfo.name_input)
        await self._type(ResumeInfo.name_input, text)
        await expect(self._find(ResumeInfo.name_input)).to_have_value(text)

    async def lang_click(self):
        await self._touch(ResumeInfo.lang_input)
        await self._force(ResumeInfo.lang_input)
        await expect(self._find(ResumeInfo.lang_id)).to_be_attached()
        await expect(self._find(ResumeInfo.lang_en)).to_be_attached()

    async def lang_select_bahasa(self):
        await self._click(ResumeInfo.lang_id)
        await expect(self._find(ResumeInfo.lang_input)).to_contain_text("Bahasa Indonesia")

    async def lang_select_language(self):
        await self._click(ResumeInfo.lang_en)
        await expect(self._find(ResumeInfo.lang_input)).to_contain_text("Bahasa Inggris")

    async def tujuan_pekerjaan_click(self):
        await self._force(ResumeInfo.goal_input)
        await expect(self._find(ResumeInfo.goal_lists)).to_be_attached()

    async def tujuan_items_interact(self):
        total_goals = await self._find(ResumeInfo.goal_items).count()
        for index in range(1, total_goals + 1):
            option = f"{ResumeInfo.goal_items}[{index}]"
            opt_label = await self._find(option).get_attribute('title')
            print(f"Selecting: {opt_label}")
            await self._click(option)
            await expect(self._find(ResumeInfo.goal_content_selected)).to_have_attribute('title', opt_label)
            await self.tujuan_pekerjaan_click()

    async def import_data_click(self):
        await self._click(ResumeInfo.import_btn)
        await expect(self._find(ResumeInfo.import_btn)).to_be_focused()

    """ Resume Information - Import Data - Data Form Validation"""
    async def import_data_modal_form_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_main)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).to_be_visible()

    async def import_form_self_data_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_main)

        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_main)).to_be_visible()
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_title)).to_have_text("Data Diri")

    async def import_form_self_data_check_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_check)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).to_be_enabled()
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).to_be_checked()

    async def import_form_self_data_name_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_name)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_name)).not_to_have_text("")

    async def import_form_self_data_email_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_email)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_email)).not_to_have_text("")

    async def import_form_self_data_phone_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_phone)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_phone)).not_to_have_text("")

    async def import_form_self_data_province_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_prov)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_prov)).not_to_have_text("")

    async def import_form_self_data_city_presence(self):
        await self._look(ResumeInfo.ImportModal.DataForm.info_city)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_city)).not_to_have_text("")

    """ Resume Information - Import Data - Data Form Interaction"""
    async def import_form_collapse_self_data(self):
        await self._click(ResumeInfo.ImportModal.DataForm.info_toggle)
        await self._conceal(ResumeInfo.ImportModal.DataForm.info_name)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_toggle)).to_have_attribute('aria-expanded', 'false')

    async def import_form_expand_self_data(self):
        await self._click(ResumeInfo.ImportModal.DataForm.info_toggle)
        await self._look(ResumeInfo.ImportModal.DataForm.info_name)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_toggle)).to_have_attribute('aria-expanded', 'true')

    async def import_form_uncheck_self_data(self):
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).to_be_checked()
        await self._click(ResumeInfo.ImportModal.DataForm.info_check)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).not_to_be_checked()

    async def import_form_check_self_data(self):
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).not_to_be_checked()
        await self._click(ResumeInfo.ImportModal.DataForm.info_check)
        await expect(self._find(ResumeInfo.ImportModal.DataForm.info_check)).to_be_checked()
