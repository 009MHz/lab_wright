from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Keahlian(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Keahlian Section Validation"""
    async def main_form_presence(self):
        await self._look(Proficiency.form)
        await expect(self._find(Proficiency.form)).to_be_attached()

    async def title_presence(self):
        await self._look(Proficiency.title)
        await expect(self._find(Proficiency.title)).to_have_text("Keahlian")

    async def desc_presence(self):
        await self._look(Proficiency.description)
        await expect(self._find(Proficiency.description)).to_contain_text("Tambah keahlian untuk")

    async def add_button_presence(self):
        await self._look(Proficiency.add_btn)
        await expect(self._find(Proficiency.add_btn)).to_be_enabled()
        await expect(self._find(Proficiency.add_btn)).to_have_text('Keahlian')

    async def main_hints_presence(self):
        await self._look(Proficiency.hint_main)
        await expect(self._find(Proficiency.hint_main)).to_be_attached()

    async def hints_title_presence(self):
        await self._look(Proficiency.hint_title)
        await expect(self._find(Proficiency.hint_title)).to_have_text('Tips Professional')

    async def hints_desc_presence(self):
        await self._look(Proficiency.hint_desc)
        await expect(self._find(Proficiency.hint_desc)).to_contain_text('Sertakan skills yang relevan')

    async def name_input_presence(self):
        await self._look(Proficiency.name_label)
        await expect(self._find(Proficiency.name_label)).to_have_text("Keahlian")

        await self._touch(Proficiency.name_input)
        await expect(self._find(Proficiency.name_input)).to_have_attribute("placeholder", "Microsoft Office")

    async def level_presence(self):
        await self._look(Proficiency.level_label)
        await expect(self._find(Proficiency.level_label)).to_have_text("Tingkat Keahlian")

        await self._touch(Proficiency.level_input)
        await expect(self._find(Proficiency.level_content)).to_have_attribute("title", "Pemula")

    async def cancel_form_btn_presence(self):
        await self._touch(Proficiency.form_cancel)
        await expect(self._find(Proficiency.form_cancel)).to_have_text("Batal")

    async def save_form_btn_presence(self):
        await self._touch(Proficiency.form_save)
        await expect(self._find(Proficiency.form_save)).to_have_text("Simpan")

    """Keahlian Section Interaction"""
    async def title_click_collapse(self):
        await self._click(Proficiency.toggle)
        await expect(self._find(Proficiency.add_btn)).to_be_hidden()
        await expect(self._find(Proficiency.toggle)).to_have_attribute('aria-expanded', 'false')

    async def title_click_expand(self):
        await self._click(Proficiency.toggle)
        await expect(self._find(Proficiency.add_btn)).to_be_visible()
        await expect(self._find(Proficiency.toggle)).to_have_attribute('aria-expanded', 'true')

    async def click_add_form(self):
        await self._click(Proficiency.add_btn)
        await expect(self._find(Proficiency.add_btn)).to_be_focused()

    async def hints_click_show(self):
        await self._click(Proficiency.hint_btn)
        await expect(self._find(Proficiency.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(Proficiency.hint_desc)).not_to_be_hidden()

    async def hints_click_hide(self):
        await self._click(Proficiency.hint_btn)
        await expect(self._find(Proficiency.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(Proficiency.hint_desc)).to_be_hidden()

    async def name_insert(self, text: str):
        await self._type(Proficiency.name_input, text)
        await expect(self._find(Proficiency.name_input)).to_be_focused()
        await expect(self._find(Proficiency.name_input)).to_have_value(text)

    async def name_clear_text(self):
        await self._touch(Proficiency.name_input)
        await expect(self._find(Proficiency.name_input)).to_be_focused()
        await expect(self._find(Proficiency.name_input)).not_to_be_empty()

        await self._find(Proficiency.name_input).clear()
        await expect(self._find(Proficiency.name_input)).to_have_value("")

    async def _level_input_click(self):
        await self._click(Proficiency.level_input)
        await expect(self._find(Proficiency.level_lists)).to_be_visible()

    async def level_click_pemula(self):
        await self._level_input_click()
        await self._force(Proficiency.level_item_pemula)
        await expect(self._find(Proficiency.level_content)).to_have_attribute('title', 'Pemula')

    async def level_click_menengah(self):
        await self._level_input_click()
        await self._force(Proficiency.level_item_menengah)
        await expect(self._find(Proficiency.level_content)).to_have_attribute('title', 'Menengah')

    async def level_click_lanjut(self):
        await self._level_input_click()
        await self._force(Proficiency.level_item_lanjut)
        await expect(self._find(Proficiency.level_content)).to_have_attribute('title', 'Lanjut')

    async def save_form_click(self):
        await self._click(Proficiency.form_save)

    async def cancel_form_click(self):
        await self._click(Proficiency.form_cancel)

        await expect(self._find(Proficiency.form_cancel)).not_to_be_attached()
        await expect(self._find(Proficiency.hint_desc)).not_to_be_attached()
        await expect(self._find(Proficiency.description)).to_be_visible()
