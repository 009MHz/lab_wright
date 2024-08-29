from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Keahlian(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

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
