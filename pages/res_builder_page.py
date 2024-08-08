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
        await expect(self._find(BuildLoc.info_lang_input)).to_be_enabled()

    async def info_resume_goal_title_presence(self):
        await self._touch(BuildLoc.info_goal_label)
        await expect(self._find(BuildLoc.info_goal_label)).to_have_text('Tujuan Pekerjaan')

    async def info_resume_goal_desc_presence(self):
        await self._touch(BuildLoc.info_goal_desc)
        await expect(self._find(BuildLoc.info_goal_desc)).to_contain_text('memberikan rekomendasi')

    async def info_resume_goal_input_presence(self):
        await self._touch(BuildLoc.info_goal_input)
        await expect(self._find(BuildLoc.info_goal_input)).to_be_enabled()

    async def info_resume_import_data_presence(self):
        await self._touch(BuildLoc.info_import_btn)
        await expect(self._find(BuildLoc.info_import_btn)).to_have_text(" Impor Data")

    # Todo 2: Data Diri Section
    # Todo 3: Riwayat Pendidikan Section
    # Todo 4: Riwayat Pekerjaan Section
    # Todo 5: Keahlian
    # Todo 6: Prestasi & Penghargaan
    # Todo 7: Prestasi & Penghargaan
    # Todo 8: Minat
    # Todo 9: Preview
    # Todo 10: Toast Result Action

