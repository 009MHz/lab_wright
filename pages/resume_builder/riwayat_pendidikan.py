from pages.__base import BasePage
from elements.__res_builder import *
from playwright.async_api import Page, expect


class Education(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    """Education History Validation"""
    async def section_title_presence(self):
        await self._look(EduHistory.title)
        await expect(self._find(EduHistory.title)).to_have_text("Riwayat Pendidikan")

    async def section_desc_presence(self):
        await self._look(EduHistory.description)
        await expect(self._find(EduHistory.description)).to_contain_text("Tambah riwayat pendidikan")

    async def hints_presence(self):
        await self._look(EduHistory.hint_main)
        await expect(self._find(EduHistory.hint_main)).to_be_visible()

    async def hints_title_presence(self):
        await self._look(EduHistory.hint_title)
        await expect(self._find(EduHistory.hint_title)).to_have_text('Tips Professional')

    async def hints_desc_presence(self):
        await self._look(EduHistory.hint_desc)
        await expect(self._find(EduHistory.hint_desc)).to_contain_text('Sertakan pendidikan terakhir')

    async def add_form_presence(self):
        await self._touch(EduHistory.add_btn)
        await expect(self._find(EduHistory.add_btn)).to_have_text("Riwayat Pendidikan")

    async def degree_presence(self):
        await self._look(EduHistory.degree_label)
        await expect(self._find(EduHistory.degree_label)).to_have_text("Jenjang Pendidikan")

        await self._touch(EduHistory.degree_input)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute("title", 'Sarjana (S1)')

    async def institution_presence(self):
        await self._look(EduHistory.name_label)
        await expect(self._find(EduHistory.name_label)).to_have_text("Nama Institusi")

        await self._touch(EduHistory.name_input)
        await expect(self._find(EduHistory.name_input)).to_be_empty()
        await expect(self._find(EduHistory.name_empty)).to_have_text("Universitas Cirebon")

    async def faculty_presence(self):
        await self._look(EduHistory.faculty_label)
        await expect(self._find(EduHistory.faculty_label)).to_have_text("Jurusan")

        await self._touch(EduHistory.faculty_input)
        await expect(self._find(EduHistory.faculty_input)).to_be_empty()
        await expect(self._find(EduHistory.faculty_empty)).to_have_text("Hukum")

    async def gpa_presence(self):
        await self._look(EduHistory.gpa_label)
        await expect(self._find(EduHistory.gpa_label)).to_have_text("IPK atau Nilai")

        await self._touch(EduHistory.gpa_input)
        await expect(self._find(EduHistory.gpa_input)).to_have_value('0')

        await expect(self._find(EduHistory.gpa_increase)).to_be_enabled()
        await expect(self._find(EduHistory.gpa_decrease)).to_be_enabled()

    async def max_score_presence(self):
        await self._look(EduHistory.max_gpa_label)
        await expect(self._find(EduHistory.max_gpa_label)).to_have_text("Skala Maximum")

        await self._touch(EduHistory.max_gpa_input)
        await expect(self._find(EduHistory.max_gpa_input)).to_have_value('0')

        await expect(self._find(EduHistory.max_gpa_increase)).to_be_enabled()
        await expect(self._find(EduHistory.max_gpa_decrease)).to_be_enabled()

    async def country_presence(self):
        await self._look(EduHistory.country_label)
        await expect(self._find(EduHistory.country_label)).to_have_text("Negara Institusi")

        await self._touch(EduHistory.country_input)
        await expect(self._find(EduHistory.country_content)).to_have_attribute("title", "Indonesia")

    async def prov_presence(self):
        await self._look(EduHistory.province_label)
        await expect(self._find(EduHistory.province_label)).to_have_text("Provinsi Institusi")

        await self._touch(EduHistory.province_input)
        await expect(self._find(EduHistory.province_input)).to_be_empty()
        await expect(self._find(EduHistory.province_empty)).to_have_text("Jawa Barat")

    async def city_presence(self):
        await self._look(EduHistory.city_label)
        await expect(self._find(EduHistory.city_label)).to_have_text("Kota Institusi")

        await self._touch(EduHistory.city_input)
        await expect(self._find(EduHistory.city_input)).to_be_empty()
        await expect(self._find(EduHistory.city_empty)).to_have_text("Cirebon")

    async def start_presence(self):
        await self._look(EduHistory.start_label)
        await expect(self._find(EduHistory.start_label)).to_have_text("Waktu Mulai")

        await self._touch(EduHistory.start_input)
        await expect(self._find(EduHistory.start_input)).to_be_empty()
        await expect(self._find(EduHistory.start_input)).to_have_attribute("placeholder", "Pilih Waktu Mulai")

    async def end_presence(self):
        await self._look(EduHistory.end_label)
        await expect(self._find(EduHistory.end_label)).to_have_text("Waktu Lulus")

        await self._touch(EduHistory.end_input)
        await expect(self._find(EduHistory.end_input)).to_be_empty()
        await expect(self._find(EduHistory.end_input)).to_have_attribute("placeholder", "Masih Aktif")

        await self._touch(EduHistory.end_status)
        await expect(self._find(EduHistory.end_status)).to_have_text("Pendidikan masih aktif")
        await expect(self._find(EduHistory.end_status_check)).to_be_checked()

    async def cancel_form_btn_presence(self):
        await self._touch(EduHistory.cancel_btn)
        await expect(self._find(EduHistory.cancel_btn)).to_have_text("Batal")

    async def save_form_btn_presence(self):
        await self._touch(EduHistory.save_btn)
        await expect(self._find(EduHistory.save_btn)).to_have_text("Simpan")

    """Education History Interaction"""
    async def title_click_collapse(self):
        await self._click(EduHistory.toggle)
        await expect(self._find(EduHistory.add_btn)).to_be_hidden()
        await expect(self._find(EduHistory.toggle)).to_have_attribute('aria-expanded', 'false')

    async def title_click_expand(self):
        await self._click(EduHistory.toggle)
        await expect(self._find(EduHistory.add_btn)).to_be_visible()
        await expect(self._find(EduHistory.toggle)).to_have_attribute('aria-expanded', 'true')

    async def click_add_form(self):
        await self._click(EduHistory.add_btn)
        await expect(self._find(EduHistory.add_btn)).to_be_focused()

    async def hints_click_show(self):
        await self._click(EduHistory.hint_btn)
        await expect(self._find(EduHistory.hint_btn)).to_have_attribute('aria-checked', 'true')
        await expect(self._find(EduHistory.hint_desc)).not_to_be_hidden()

    async def hints_click_hide(self):
        await self._click(EduHistory.hint_btn)
        await expect(self._find(EduHistory.hint_btn)).to_have_attribute('aria-checked', 'false')
        await expect(self._find(EduHistory.hint_desc)).to_be_hidden()

    async def click_degree(self):
        await self._force(EduHistory.degree_input)
        await expect(self._find(EduHistory.degree_lists)).to_be_visible()

    async def click_degree_sma(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_sma)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'SMA/SMK/Sederajat')

    async def click_degree_d1(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d1)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Ahli Pratama (D1)')

    async def click_degree_d2(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d2)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Ahli Muda (D2)')

    async def click_degree_d3(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d3)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Ahli Madya (D3)')

    async def click_degree_d4(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_d4)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Sarjana Sains Terapan (D4)')

    async def click_degree_s1(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_s1)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Sarjana (S1)')

    async def click_degree_s2(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_s2)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Magister (S2)')

    async def click_degree_s3(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_s3)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Doktor (S3)')

    async def click_degree_course(self):
        await self.click_degree()

        await self._look(EduHistory.degree_lists)
        await self._click(EduHistory.degree_course)
        await expect(self._find(EduHistory.degree_content)).to_have_attribute('title', 'Kursus & Pelatihan')

    async def institution_insert(self, text):
        await self._type(EduHistory.name_input, text)
        await expect(self._find(EduHistory.name_list)).to_be_visible(timeout=20000)
        await expect(self._find(EduHistory.name_add)).to_contain_text(text)

    async def institution_click_filled(self):
        await self._click(EduHistory.name_selected)
        await expect(self._find(EduHistory.name_input)).to_be_focused()
        await expect(self._find(EduHistory.name_list)).to_be_visible()

    async def institution_select_option_within(self, text):
        await self.institution_insert(text)
        count = await self._find(EduHistory.name_item).count()
        for x in range(1, count + 1):
            await self._click(f"{EduHistory.name_item}[{x}]")
            await self._click(".ant-layout-content")
            await self.institution_click_filled()

    async def faculty_insert(self, text):
        await self._type(EduHistory.faculty_input, text)
        await expect(self._find(EduHistory.faculty_list)).to_be_visible()
        await expect(self._find(EduHistory.faculty_add)).to_contain_text(text)

    async def faculty_click_filled(self):
        await self._force(EduHistory.faculty_selected)
        await expect(self._find(EduHistory.faculty_input)).to_be_focused()
        await expect(self._find(EduHistory.faculty_list)).to_be_visible()

    async def faculty_select_option_within(self, text):
        await self.faculty_insert(text)
        for x in range(1, 6):
            await self._click(f"{EduHistory.faculty_item}[{x}]")
            await self._click(".ant-layout-content")
            await self.faculty_click_filled()

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

    async def click_country(self):
        await self._click(EduHistory.country_input)
        await expect(self._find(EduHistory.country_lists)).to_be_visible()

    async def select_wni(self):
        await self.click_country()

        await self._click(EduHistory.country_wni)
        await expect(self._find(EduHistory.country_content)).to_have_attribute('title', 'Indonesia')

    async def select_wna(self):
        await self.click_country()

        await self._click(EduHistory.country_wna)
        await expect(self._find(EduHistory.country_content)).to_have_attribute('title', 'Luar Indonesia')

    async def prov_click_filled(self):
        await self._force(EduHistory.province_selected)
        await expect(self._find(EduHistory.province_input)).to_be_focused()
        await expect(self._find(EduHistory.province_lists)).to_be_visible()

    async def prov_insert(self, text: str):
        await self._type(EduHistory.province_input, text)
        await expect(self._find(EduHistory.province_input)).to_have_value(text)
        await expect(self._find(EduHistory.province_lists)).to_be_visible()

    async def prov_select_option_within(self, text):
        await self.prov_insert(text)
        count = await self._find(EduHistory.province_item).count()

        for x in range(1, count + 1):
            await self._click(f"{EduHistory.province_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick the input field
            if x != count:
                await self.prov_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(EduHistory.province_lists)).not_to_be_visible()
        await expect(self._find(EduHistory.city_input)).to_be_enabled()

    async def city_click_filled(self):
        await self._force(EduHistory.city_selected)
        await expect(self._find(EduHistory.city_input)).to_be_focused()
        await expect(self._find(EduHistory.city_lists)).to_be_visible()

    async def city_insert(self, text: str):
        await self._type(EduHistory.city_input, text)
        await expect(self._find(EduHistory.city_input)).to_have_value(text)
        await expect(self._find(EduHistory.city_lists)).to_be_visible()

    async def city_select_option_within(self, text):
        await self.city_insert(text)
        count = await self._find(EduHistory.city_item).count()
        for x in range(1, count + 1):
            await self._click(f"{EduHistory.city_item}[{x}]")
            await self._click(".ant-layout-content")  # Unclick input field
            if x != count:
                await self.city_click_filled()
            else:
                await self._click(".ant-layout-content")

        await expect(self._find(EduHistory.city_lists)).not_to_be_visible()

    async def start_date_insert(self, month: str, year: int):
        await self._click(EduHistory.start_input)
        await expect(self._find(EduHistory.start_input)).to_be_focused()

        await self._type(EduHistory.start_input, f"{month} - {year}")
        await self._find(EduHistory.start_input).press("Enter")
        await expect(self._find(EduHistory.start_input)).to_have_value(f"{month} - {year}")

    async def start_date_clear(self):
        await self._click(EduHistory.start_clear)
        await expect(self._find(EduHistory.start_input)).to_be_focused()

    async def end_date_insert(self, month: str, year: int):
        await self._click(EduHistory.end_input)
        await expect(self._find(EduHistory.end_input)).to_be_focused()

        await self._type(EduHistory.end_input, f"{month} - {year}")
        await self._find(EduHistory.end_input).press("Enter")
        await expect(self._find(EduHistory.end_input)).to_have_value(f"{month} - {year}")

    async def end_active_checking(self):
        await expect(self._find(EduHistory.end_status_check)).not_to_be_checked()

        await self._click(EduHistory.end_status_check)
        await expect(self._find(EduHistory.end_status_check)).to_be_checked()
        await expect(self._find(EduHistory.end_input)).to_be_disabled()

    async def end_active_unchecking(self):
        await expect(self._find(EduHistory.end_status_check)).to_be_checked()

        await self._click(EduHistory.end_status_check)
        await expect(self._find(EduHistory.end_status_check)).not_to_be_checked()
        await expect(self._find(EduHistory.end_input)).to_be_enabled()

    async def end_date_clear(self):
        await self._force(EduHistory.end_clear)
        await expect(self._find(EduHistory.start_input)).to_have_value("")

    async def save_btn_click(self):
        await self._click(EduHistory.save_btn)
        await expect(self._find(EduHistory.save_btn)).to_be_focused()

    async def cancel_btn_click(self):
        await self._click(EduHistory.cancel_btn)

        await expect(self._find(EduHistory.cancel_btn)).not_to_be_attached()
        await expect(self._find(EduHistory.hint_desc)).not_to_be_attached()
        await expect(self._find(EduHistory.description)).to_be_visible()
