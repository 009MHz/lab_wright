from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Prestasi(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Achievements & Honor Validation"""
    async def main_form_presence(self):
        await self._look(Achievements.form)
        await expect(self._find(Achievements.form)).to_be_attached()

    async def section_title_presence(self):
        await self._look(Achievements.title)
        await expect(self._find(Achievements.title)).to_have_text("Prestasi & Penghargaan Non-akademik")

    async def section_desc_presence(self):
        await self._look(Achievements.description)
        await expect(self._find(Achievements.description)).to_contain_text("Tambah Prestasi dan penghargaan")

    async def add_form_presence(self):
        await self._look(Achievements.add_btn)
        await expect(self._find(Achievements.add_btn)).to_be_enabled()
        await expect(self._find(Achievements.add_btn)).to_have_text(' Prestasi & Penghargaan')

    async def hints_presence(self):
        await self._look(Achievements.hint_main)
        await expect(self._find(Achievements.hint_main)).to_be_attached()

    async def hints_title_presence(self):
        await self._look(Achievements.hint_title)
        await expect(self._find(Achievements.hint_title)).to_have_text('Tips Professional')

    async def hints_desc_presence(self):
        await self._look(Achievements.hint_desc)
        await expect(self._find(Achievements.hint_desc)).to_contain_text('Pastikan penulisan award konsisten')

    async def year_presence(self):
        await self._look(Achievements.year_label)
        await expect(self._find(Achievements.year_label)).to_have_text("Tahun")

        await self._touch(Achievements.year_input)
        await expect(self._find(Achievements.year_input)).to_be_empty()
        await expect(self._find(Achievements.year_input)).to_have_attribute("placeholder", "2021")

    async def name_presence(self):
        await self._look(Achievements.name_label)
        await expect(self._find(Achievements.name_label)).to_have_text("Prestasi & Penghargaan")

        await self._touch(Achievements.name_input)
        await expect(self._find(Achievements.name_input)).to_have_attribute("placeholder",
                                                                            "Juara 1 Olimpiade Sains Nasional (OSN) "
                                                                            "Matematika Tingkat Nasional")

    async def cancel_form_presence(self):
        await self._touch(Achievements.form_cancel)
        await expect(self._find(Achievements.form_cancel)).to_have_text("Batal")

    async def save_form_presence(self):
        await self._touch(Achievements.form_save)
        await expect(self._find(Achievements.form_save)).to_have_text("Simpan")

    """Achievements & Honor Interaction"""
    async def collapse_form(self):
        await self._click(Achievements.toggle)
        await expect(self._find(Achievements.add_btn)).to_be_hidden()
        await expect(self._find(Achievements.toggle)).to_have_attribute('aria-expanded', 'false')

    async def expand_form(self):
        await self._click(Achievements.toggle)
        await expect(self._find(Achievements.add_btn)).to_be_visible()
        await expect(self._find(Achievements.toggle)).to_have_attribute('aria-expanded', 'true')

    async def click_add_form(self):
        await self._click(Achievements.add_btn)
        await expect(self._find(Achievements.add_btn)).to_be_focused()

    async def hints_click_show(self):
        await self._click(Achievements.hint_btn)
        await expect(self._find(Achievements.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(Achievements.hint_desc)).not_to_be_hidden()

    async def hints_click_hide(self):
        await self._click(Achievements.hint_btn)
        await expect(self._find(Achievements.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(Achievements.hint_desc)).to_be_hidden()

    async def insert_year(self, year: int):
        await self._click(Achievements.year_input)
        await expect(self._find(Achievements.year_input)).to_be_focused()

        await self._type(Achievements.year_input, str(year))
        await self._find(Achievements.year_input).press("Enter")
        await expect(self._find(Achievements.year_input)).to_have_value(str(year))

    async def clear_year(self):
        await self._click(Achievements.year_clear)
        await expect(self._find(Achievements.year_input)).to_be_focused()

    async def insert_name(self, name: str):
        await self._click(Achievements.name_input)
        await expect(self._find(Achievements.name_input)).to_be_focused()

        await self._type(Achievements.name_input, name)
        await self._find(Achievements.name_input).press("Enter")
        await expect(self._find(Achievements.name_input)).to_have_value(name)

    async def clear_name(self):
        await self._find(Achievements.name_input).clear()

        await expect(self._find(Achievements.name_input)).to_be_focused()
        await expect(self._find(Achievements.name_input)).to_have_value("")

    async def click_save_form(self):
        await self._click(Achievements.form_save)
        await expect(self._find(Achievements.form_save)).to_be_focused()

    async def click_cancel_form(self):
        await self._click(Achievements.form_cancel)

        await expect(self._find(Achievements.form_cancel)).not_to_be_attached()
        await expect(self._find(Achievements.hint_desc)).not_to_be_attached()
        await expect(self._find(Achievements.description)).to_be_visible()
