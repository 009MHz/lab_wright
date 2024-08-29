from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Minat(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Hobby Validation"""
    async def main_section_presence(self):
        await self._look(Hobby.form)
        await expect(self._find(Hobby.form)).to_be_visible()

    async def section_title_presence(self):
        await self._look(Hobby.title)
        await expect(self._find(Hobby.title)).to_have_text("Minat")

    async def section_info_presence(self):
        await self._look(Hobby.desc)
        await expect(self._find(Hobby.desc)).to_contain_text("Tambah Minat untuk membantu perusahaan mengenalimu")

    async def add_form_presence(self):
        await self._look(Hobby.add_btn)
        await expect(self._find(Hobby.add_btn)).to_be_enabled()
        await expect(self._find(Hobby.add_btn)).to_have_text('Minat')

    async def hints_presence(self):
        await self._look(Hobby.hint_main)
        await expect(self._find(Hobby.hint_main)).to_be_attached()

    async def hints_title_presence(self):
        await self._look(Hobby.hint_title)
        await expect(self._find(Hobby.hint_title)).to_have_text('Tips Professional')

    async def hints_desc_presence(self):
        await self._look(Hobby.hint_desc)
        await expect(self._find(Hobby.hint_desc)).to_contain_text('Pikirkan minat yang menarik')

    async def name_input_presence(self):
        await self._look(Hobby.name_label)
        await expect(self._find(Hobby.name_label)).to_have_text("Minat")

        await self._touch(Hobby.name_input)
        await expect(self._find(Hobby.name_input)).to_be_empty()
        await expect(self._find(Hobby.name_input)).to_have_attribute("placeholder", "Fotografi & Videografi")

    async def cancel_form_presence(self):
        await self._touch(Hobby.form_cancel)
        await expect(self._find(Hobby.form_cancel)).to_have_text("Batal")

    async def save_form_presence(self):
        await self._touch(Hobby.form_save)
        await expect(self._find(Hobby.form_save)).to_have_text("Simpan")

    """Hobby Interaction"""
    async def click_collapse_form(self):
        await self._click(Hobby.toggle)
        await expect(self._find(Hobby.add_btn)).to_be_hidden()
        await expect(self._find(Hobby.toggle)).to_have_attribute('aria-expanded', 'false')

    async def click_expand_form(self):
        await self._click(Hobby.toggle)
        await expect(self._find(Hobby.add_btn)).to_be_visible()
        await expect(self._find(Hobby.toggle)).to_have_attribute('aria-expanded', 'true')

    async def click_add_form(self):
        await self._click(Hobby.add_btn)
        await expect(self._find(Hobby.add_btn)).to_be_focused()

    async def click_toggle_show_hints(self):
        await self._click(Hobby.hint_btn)
        await expect(self._find(Hobby.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(Hobby.hint_desc)).not_to_be_hidden()

    async def click_toggle_hide_hints(self):
        await self._click(Hobby.hint_btn)
        await expect(self._find(Hobby.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(Hobby.hint_desc)).to_be_hidden()

    async def insert_hobby_name(self, name: str):
        await self._click(Hobby.name_input)
        await expect(self._find(Hobby.name_input)).to_be_focused()

        await self._type(Hobby.name_input, name)
        await self._find(Hobby.name_input).press("Enter")
        await expect(self._find(Hobby.name_input)).to_have_value(name)

    async def clear_hobby_name(self):
        await self._find(Hobby.name_input).clear()

        await expect(self._find(Hobby.name_input)).to_be_focused()
        await expect(self._find(Hobby.name_input)).to_have_value("")

    async def click_save_form(self):
        await self._click(Hobby.form_save)
        await expect(self._find(Hobby.form_save)).to_be_focused()

    async def click_cancel_form(self):
        await self._click(Hobby.form_cancel)

        await expect(self._find(Hobby.form_cancel)).not_to_be_attached()
        await expect(self._find(Hobby.hint_desc)).not_to_be_attached()
        await expect(self._find(Hobby.desc)).to_be_visible()
