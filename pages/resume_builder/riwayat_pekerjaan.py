from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Profession(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Work History Validation"""
    async def section_title_presence(self):
        await self._look(JobHistory.title)
        await expect(self._find(JobHistory.title)).to_have_text("Riwayat Pekerjaan")

    async def section_desc_presence(self):
        await self._look(JobHistory.description)
        await expect(self._find(JobHistory.description)).to_contain_text("Tambah riwayat pekerjaan")

    async def main_hints_presence(self):
        await self._look(JobHistory.hint_main)
        await expect(self._find(JobHistory.hint_main)).to_be_visible()

    async def hints_title_presence(self):
        await self._look(JobHistory.hint_title)
        await expect(self._find(JobHistory.hint_title)).to_have_text('Tips Professional')

    async def hints_desc_presence(self):
        await self._look(JobHistory.hint_desc)
        await expect(self._find(JobHistory.hint_desc)).to_contain_text('Cantumkan pengalaman magang')

    async def add_form_presence(self):
        await self._touch(JobHistory.add_btn)
        await expect(self._find(JobHistory.add_btn)).to_have_text("Riwayat Pekerjaan")

    async def position_presence(self):
        await self._look(JobHistory.pos_label)
        await expect(self._find(JobHistory.pos_label)).to_have_text("Posisi")

        await self._touch(JobHistory.pos_input)
        await expect(self._find(JobHistory.pos_input)).to_be_empty()
        await expect(self._find(JobHistory.pos_empty)).to_have_text("Sales Analyst")

    async def company_name_presence(self):
        await self._look(JobHistory.company_label)
        await expect(self._find(JobHistory.company_label)).to_have_text("Nama Perusahaan")

        await self._touch(JobHistory.company_input)
        await expect(self._find(JobHistory.company_input)).to_have_attribute("placeholder", "PT. ABC")

    async def country_presence(self):
        await self._look(JobHistory.country_label)
        await expect(self._find(JobHistory.country_label)).to_have_text("Negara Perusahaan/Organisasi")

        await self._touch(JobHistory.country_input)
        await expect(self._find(JobHistory.country_content)).to_have_attribute("title", "Indonesia")

    async def prov_presence(self):
        await self._look(JobHistory.province_label)
        await expect(self._find(JobHistory.province_label)).to_have_text("Provinsi Perusahaan/Organisasi")

        await self._touch(JobHistory.province_input)
        await expect(self._find(JobHistory.province_input)).to_be_empty()
        await expect(self._find(JobHistory.province_empty)).to_have_text("Jawa Barat")

    async def city_presence(self):
        await self._look(JobHistory.city_label)
        await expect(self._find(JobHistory.city_label)).to_have_text("Kota Perusahaan/Organisasi")

        await self._touch(JobHistory.city_input)
        await expect(self._find(JobHistory.city_input)).to_be_empty()
        await expect(self._find(JobHistory.city_empty)).to_have_text("Cirebon")

    async def status_presence(self):
        await self._look(JobHistory.status_label)
        await expect(self._find(JobHistory.status_label)).to_have_text("Status Pekerjaan")

        await self._touch(JobHistory.status_input)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Purnawaktu')

    async def start_date_presence(self):
        await self._look(JobHistory.start_label)
        await expect(self._find(JobHistory.start_label)).to_have_text("Waktu Mulai")

        await self._touch(JobHistory.start_input)
        await expect(self._find(JobHistory.start_input)).to_be_empty()
        await expect(self._find(JobHistory.start_input)).to_have_attribute("placeholder", "Pilih Waktu Mulai")

    async def end_date_presence(self):
        await self._look(JobHistory.end_label)
        await expect(self._find(JobHistory.end_label)).to_have_text("Waktu Selesai")

        await self._touch(JobHistory.end_input)
        await expect(self._find(JobHistory.end_input)).to_be_empty()
        await expect(self._find(JobHistory.end_input)).to_have_attribute("placeholder", "Masih Aktif")

        await self._touch(JobHistory.end_status)
        await expect(self._find(JobHistory.end_status)).to_have_text("Posisi masih aktif")
        await expect(self._find(JobHistory.end_status_check)).to_be_checked()

    async def cancel_form_btn_presence(self):
        await self._touch(JobHistory.form_cancel)
        await expect(self._find(JobHistory.form_cancel)).to_have_text("Batal")

    async def save_form_btn_presence(self):
        await self._touch(JobHistory.form_save)
        await expect(self._find(JobHistory.form_save)).to_have_text("Simpan")

    """Work History Interaction"""

    async def title_click_collapse(self):
        await self._click(JobHistory.toggle)
        await expect(self._find(JobHistory.add_btn)).to_be_hidden()
        await expect(self._find(JobHistory.toggle)).to_have_attribute('aria-expanded', 'false')

    async def title_click_expand(self):
        await self._click(JobHistory.toggle)
        await expect(self._find(JobHistory.add_btn)).to_be_visible()
        await expect(self._find(JobHistory.toggle)).to_have_attribute('aria-expanded', 'true')

    async def click_add_form(self):
        await self._click(JobHistory.add_btn)
        await expect(self._find(JobHistory.add_btn)).to_be_focused()

    async def hints_click_show(self):
        await self._click(JobHistory.hint_btn)
        await expect(self._find(JobHistory.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(JobHistory.hint_desc)).not_to_be_hidden()

    async def hints_click_hide(self):
        await self._click(JobHistory.hint_btn)
        await expect(self._find(JobHistory.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(JobHistory.hint_desc)).to_be_hidden()

    async def position_insert(self, text):
        await self._type(JobHistory.pos_input, text)
        await expect(self._find(JobHistory.pos_list)).to_be_visible()
        await expect(self._find(JobHistory.pos_add)).to_contain_text(text)

    async def position_click_filled(self):
        await self._click(JobHistory.pos_selected)
        await expect(self._find(JobHistory.pos_input)).to_be_focused()
        await expect(self._find(JobHistory.pos_list)).to_be_visible()

    async def position_select_option_within(self, text):
        await self.position_insert(text)
        jobs = await self._find(JobHistory.pos_item).count()
        for x in range(1, jobs):
            await self._click(f"{JobHistory.pos_item}[{x + 1}]")
            await self._click(".ant-layout-content")
            await self.position_click_filled()

    async def company_name_insert(self, text: str):
        await self._type(JobHistory.company_input, text)
        await expect(self._find(JobHistory.company_input)).to_be_focused()
        await expect(self._find(JobHistory.company_input)).to_have_value(text)

    async def click_country(self):
        await self._click(JobHistory.country_input)
        await expect(self._find(JobHistory.country_lists)).to_be_visible()

    async def select_wni(self):
        await self.click_country()
        await self._force(JobHistory.country_wni)
        await expect(self._find(JobHistory.country_content)).to_have_attribute('title', 'Indonesia')

    async def select_wna(self):
        await self.click_country()
        await self._force(JobHistory.country_wna)
        await expect(self._find(JobHistory.country_content)).to_have_attribute('title', 'Luar Indonesia')

    async def prov_click_filled(self):
        await self._force(JobHistory.province_selected)
        await expect(self._find(JobHistory.province_input)).to_be_focused()
        await expect(self._find(JobHistory.province_lists)).to_be_visible()

    async def prov_insert(self, text: str):
        await self._type(JobHistory.province_input, text)
        await expect(self._find(JobHistory.province_input)).to_have_value(text)
        await expect(self._find(JobHistory.province_lists)).to_be_visible()

    async def prov_select_option_within(self, text):
        await self.prov_insert(text)
        count = await self._find(JobHistory.province_item).count()

        for x in range(1, count + 1):
            await self._click(f"{JobHistory.province_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick the input field
            if x != count:
                await self.prov_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(JobHistory.province_lists)).not_to_be_visible()
        await expect(self._find(JobHistory.city_input)).to_be_enabled()

    async def city_click_filled(self):
        await self._force(JobHistory.city_selected)
        await expect(self._find(JobHistory.city_input)).to_be_focused()
        await expect(self._find(JobHistory.city_lists)).to_be_visible()

    async def city_insert(self, text: str):
        await self._type(JobHistory.city_input, text)
        await expect(self._find(JobHistory.city_input)).to_have_value(text)
        await expect(self._find(JobHistory.city_lists)).to_be_visible()

    async def city_select_option_within(self, text):
        await self.city_insert(text)
        count = await self._find(JobHistory.city_item).count()
        for x in range(1, count + 1):
            await self._click(f"{JobHistory.city_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick input field
            if x != count:
                await self.city_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(JobHistory.city_lists)).not_to_be_visible()

    async def click_status(self):
        await self._force(JobHistory.status_input)
        await expect(self._find(JobHistory.status_lists)).to_be_visible()

    async def click_status_full(self):
        await self.click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_full)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Purnawaktu')

    async def click_status_part(self):
        await self.click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_part)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Paruh Waktu')

    async def click_status_freelance(self):
        await self.click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_freelance)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Pekerja Lepas')

    async def click_status_internship(self):
        await self.click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_intern)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Magang')

    async def click_status_volunteer(self):
        await self.click_status()

        await self._look(JobHistory.status_lists)
        await self._click(JobHistory.status_volunteer)
        await expect(self._find(JobHistory.status_content)).to_have_attribute('title', 'Sukarela')

    async def start_date_insert(self, month: str, year: int):
        await self._click(JobHistory.start_input)
        await expect(self._find(JobHistory.start_input)).to_be_focused()

        await self._type(JobHistory.start_input, f"{month} - {year}")
        await self._find(JobHistory.start_input).press("Enter")
        await expect(self._find(JobHistory.start_input)).to_have_value(f"{month} - {year}")

    async def start_date_clear(self):
        await self._force(JobHistory.start_clear)
        await expect(self._find(JobHistory.start_input)).to_have_value("")

    async def end_date_insert(self, month: str, year: int):
        await self._click(JobHistory.end_input)
        await expect(self._find(JobHistory.end_input)).to_be_focused()

        await self._type(JobHistory.end_input, f"{month} - {year}")
        await self._find(JobHistory.end_input).press("Enter")
        await expect(self._find(JobHistory.end_input)).to_have_value(f"{month} - {year}")

    async def end_active_checking(self):
        await expect(self._find(JobHistory.end_status_check)).not_to_be_checked()

        await self._click(JobHistory.end_status_check)
        await expect(self._find(JobHistory.end_status_check)).to_be_checked()
        await expect(self._find(JobHistory.end_input)).to_be_disabled()

    async def end_active_unchecking(self):
        await expect(self._find(JobHistory.end_status_check)).to_be_checked()

        await self._click(JobHistory.end_status_check)
        await expect(self._find(JobHistory.end_status_check)).not_to_be_checked()
        await expect(self._find(JobHistory.end_input)).to_be_enabled()

    async def end_date_clear(self):
        await self._force(JobHistory.end_clear)
        await expect(self._find(JobHistory.start_input)).to_have_value("")

    async def save_btn_click(self):
        await self._click(JobHistory.form_save)

    async def cancel_btn_click(self):
        await self._click(JobHistory.form_cancel)

        await expect(self._find(JobHistory.form_cancel)).not_to_be_attached()
        await expect(self._find(JobHistory.hint_desc)).not_to_be_attached()
        await expect(self._find(JobHistory.description)).to_be_visible()
