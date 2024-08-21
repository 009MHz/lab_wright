import pytest
from pages.res_builder_page import Builder
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def builder(user_auth):
    builder = Builder(user_auth)
    await builder.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Resume Builder/ Smoke Test")
class TestSmokeLoginPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Validation")
    @allure.feature("Informasi Resume")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_section(self, builder):
        with allure.step('1. Validating Page Header'):
            await builder.page_title_presence()

        with allure.step('2. Validating Section Header'):
            await builder.info_section_title_presence()

        with allure.step('3. Validating Nama resume'):
            await builder.info_resume_name_presence()
            await builder.info_resume_name_insert("Written from playwright")

        with allure.step('4. Validating Bahasa Resume'):
            await builder.info_resume_language_presence()
            await builder.info_resume_lang_click()
            await builder.info_resume_select_bahasa()
            await builder.info_resume_lang_click()
            await builder.info_resume_select_language()

        with allure.step('5. Validating Tujuan Pekerjaan'):
            await builder.info_resume_goal_title_presence()
            await builder.info_resume_tujuan_presence()
            await builder.info_resume_goal_click()
            await builder.info_resume_goal_items_interact()

        with allure.step('6. Validating Import Data'):
            await builder.info_resume_import_data_click()
            await builder.import_data_modal_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Hints Existence")
    @allure.feature("Data Diri", "Hints")
    @allure.severity(severity.MINOR)
    async def test_data_diri_section_hints(self, builder):
        with allure.step('Validating Hints Component'):
            await builder.self_info_hints_title_presence()
            await builder.self_info_hints_desc_presence()
            await builder.self_info_hints_toggle_presence()

        with allure.step('Interact with Data Diri hint toggle'):
            await builder.self_info_hints_click_hide()
            await builder.self_info_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Data Diri Existence Validation")
    @allure.feature("Data Diri")
    @allure.severity(severity.CRITICAL)
    async def test_data_diri_section(self, builder):
        with allure.step('1. Validating each input field completeness'):
            await builder.self_info_main_form_presence()
            await builder.self_info_main_hints_presence()
            await builder.self_info_title_presence()
            await builder.self_info_first_name_presence()
            await builder.self_info_last_name_presence()
            await builder.self_info_email_presence()
            await builder.self_info_phone_presence()
            await builder.self_info_country_presence()
            await builder.self_info_prov_presence()
            await builder.self_info_city_presence()
            await builder.self_info_address_presence()
            await builder.self_info_linkedin_presence()
            await builder.self_info_portfolio_presence()
            await builder.self_info_simpan_btn_presence()

        with allure.step('2. Interact the section header accordion'):
            await builder.self_info_collapse_form()
            await builder.self_info_expand_form()

        with allure.step('3. Insert any text on the Nama Depan Field'):
            await builder.self_info_first_name_insert('Mr. John ')

        with allure.step('4. Insert any text on the Nama Belakang Field'):
            await builder.self_info_last_name_insert('Toryono ,M.Sc')

        with allure.step('5. Insert any text on the Email Field'):
            await builder.self_info_email_insert('ali.nA_p3tr|nK0vA@yahoo.us')

        with allure.step('6. Insert a valid phone number on the No. Telepon field'):
            await builder.self_info_phone_insert('08987654321')

        with allure.step('7. Click on the Negara option'):
            await builder.self_info_select_wna()
            await builder.self_info_select_wni()

        with allure.step('8. Select displayed province from the input keyword'):
            await builder.self_info_prov_select_option_within('Jawa')

        with allure.step('9. Select displayed city from the input keyword'):
            await builder.self_info_city_select_option_within('Ban')

        with allure.step('10. Insert any text on the Alamat Field'):
            await builder.self_info_address_insert("Jl. Belawan No.16, RT.18/RW.1, Cideng")

        with allure.step('11. Insert a valid Linkedin url'):
            await builder.self_info_linkedin_insert("https://www.linkedin.com/company/karirlab")

        with allure.step('12. Insert a valid url on the portfolio field'):
            await builder.self_info_portfolio_insert('https://github.com/microsoft/playwright')

        with allure.step('13. Click on the simpan button'):
            await builder.self_info_click_simpan()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pendidikan Hints Existence")
    @allure.feature("Riwayat Pendidikan", "Hints")
    @allure.severity(severity.NORMAL)
    async def test_education_section_hints(self, builder):
        with allure.step('1. Click on the Add Riwayat Pendidikan Form button'):
            await builder.edu_click_add_form()

        with allure.step('2. Validate the Hints section after form is added'):
            await builder.edu_main_hints_presence()
            await builder.edu_hints_title_presence()
            await builder.edu_hints_desc_presence()

        with allure.step('3. Interact with Riwayat Pendidikan hint toggle'):
            await builder.edu_hints_click_hide()
            await builder.edu_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pendidikan Validation")
    @allure.feature("Riwayat Pendidikan")
    @allure.severity(severity.CRITICAL)
    async def test_education_section(self, builder):
        with allure.step('1. Validate riwayat pendidikan default state'):
            await builder.edu_title_presence()
            await builder.edu_desc_presence()
            await builder.edu_add_form_button_presence()
            await builder.edu_title_click_collapse()
            await builder.edu_title_click_expand()

        with allure.step('2. Click on the Add Riwayat Pendidikan Form button'):
            await builder.edu_click_add_form()

        with allure.step('3. Validating each input field completeness'):
            await builder.edu_degree_presence()
            await builder.edu_institution_presence()
            await builder.edu_faculty_presence()
            await builder.edu_gpa_presence()
            await builder.edu_max_score_presence()
            await builder.edu_country_presence()
            await builder.edu_prov_presence()
            await builder.edu_city_presence()
            await builder.edu_start_presence()
            await builder.edu_end_presence()
            await builder.edu_cancel_form_btn_presence()
            await builder.edu_save_form_btn_presence()

        with allure.step('4. Click on each Jenjang Pendidikan option'):
            await builder.edu_click_degree_sma()
            await builder.edu_click_degree_d1()
            await builder.edu_click_degree_d2()
            await builder.edu_click_degree_d3()
            await builder.edu_click_degree_d4()
            await builder.edu_click_degree_s1()
            await builder.edu_click_degree_s2()
            await builder.edu_click_degree_s3()
            await builder.edu_click_degree_course()
            await builder.edu_click_degree_s1()

        with allure.step('5. Interact with displayed Institution from the input keyword'):
            await builder.edu_institution_select_option_within("Univ")

        with allure.step('6. Select displayed faculty from the input keyword'):
            await builder.faculty_select_option_within('Bis')

        with allure.step('7. Interact with the GPA input field'):
            await builder.faculty_gpa_insert('3.8')
            await builder.faculty_gpa_score_increase(3)
            await builder.faculty_gpa_score_decrease(2)

        with allure.step('8. Interact with the max score input field'):
            await builder.faculty_max_gpa_insert('4.2')
            await builder.faculty_max_gpa_score_increase(2)
            await builder.faculty_max_gpa_score_decrease(3)

        with allure.step('9. Select all options from Negara institusi'):
            await builder.edu_select_wna()
            await builder.edu_select_wni()

        with allure.step('10. Select displayed province from the input keyword'):
            pass
            await builder.edu_prov_select_option_within('Sum')

        with allure.step('11. Validate Kota Institusi'):
            await builder.edu_city_select_option_within('tan')

        with allure.step('12. Validate Waktu Mulai'):
            await builder.edu_start_date_insert("August", 2016)
            await builder.edu_start_date_clear()

        with allure.step('13. Validate Waktu Lulus'):
            await builder.edu_end_active_unchecking()
            await builder.edu_end_date_insert("December", 2021)
            await builder.edu_end_date_clear()
            await builder.edu_end_active_checking()

        with allure.step('14. Click on Simpan button'):
            await builder.edu_save_btn_click()

        with allure.step('15. Click on Batal button'):
            await builder.edu_cancel_btn_click()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pekerjaan Hints Existence")
    @allure.feature("Riwayat Pekerjaan", "Hints")
    @allure.severity(severity.MINOR)
    async def test_occupation_section_hints(self, builder):
        with allure.step('1. Click on the Add Riwayat Pekerjaan Form button'):
            await builder.job_click_add_form()

        with allure.step('2. Validate the Hints section after form is added'):
            await builder.job_main_hints_presence()
            await builder.job_hints_title_presence()
            await builder.job_hints_desc_presence()

        with allure.step('3. Interact with Riwayat Pendidikan hint toggle'):
            await builder.job_hints_click_hide()
            await builder.job_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pekerjaan Existence")
    @allure.feature("Riwayat Pekerjaan")
    @allure.severity(severity.CRITICAL)
    async def test_occupation_section(self, builder):
        with allure.step('1. Validate the section default state'):
            await builder.job_title_presence()
            await builder.job_desc_presence()
            await builder.job_add_form_button_presence()
            await builder.job_title_click_collapse()
            await builder.job_title_click_expand()

        with allure.step('2. Click on the Add Riwayat Pekerjaan Form button'):
            await builder.job_click_add_form()

        with allure.step('3. Validating each input field completeness'):
            await builder.job_position_presence()
            await builder.job_company_name_presence()
            await builder.job_country_presence()
            await builder.job_prov_presence()
            await builder.job_city_presence()
            await builder.job_status_presence()
            await builder.job_start_presence()
            await builder.job_end_presence()
            await builder.job_cancel_form_btn_presence()
            await builder.job_save_form_btn_presence()

        with allure.step('4. Interact with displayed position from the input keyword'):
            await builder.job_position_select_option_within("Engine")

        with allure.step('5. Insert a valid text on Perusahaan input'):
            await builder.job_company_name_insert('KarirLab')

        with allure.step('6. Select all options from Negara Perusahaan'):
            await builder.job_select_wna()
            await builder.job_select_wni()

        with allure.step('10. Interact with displayed Province from the input keyword'):
            await builder.job_prov_select_option_within('Jak')

        with allure.step('11. Validate Kota Institusi'):
            await builder.job_city_select_option_within('Jakarta')

        with allure.step('4. Validate Status Pekerjaan'):
            await builder.job_click_status_full()
            await builder.job_click_status_part()
            await builder.job_click_status_freelance()
            await builder.job_click_status_internship()
            await builder.job_click_status_volunteer()

        with allure.step('12. Validate Waktu Mulai'):
            await builder.job_start_date_insert("January", 2022)
            await builder.job_start_date_clear()

        with allure.step('13. Validate Waktu Selesai'):
            await builder.job_end_active_unchecking()
            await builder.job_end_date_insert("December", 2022)
            await builder.job_end_date_clear()
            await builder.job_end_active_checking()

        with allure.step('14. Click on Simpan button'):
            await builder.job_save_btn_click()

        with allure.step('15. Click on Batal button'):
            await builder.job_cancel_btn_click()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Keahlian Hints Existence")
    @allure.feature("Keahlian", "Hints")
    @allure.severity(severity.MINOR)
    async def test_proficient_section_hints(self, builder):
        with allure.step('1. Click on the Add Keahlian Form button'):
            await builder.skill_click_add_form()

        with allure.step('2. Validate the Keahlian Hints section after form is added'):
            await builder.skill_main_hints_presence()
            await builder.skill_hints_title_presence()
            await builder.skill_hints_desc_presence()

        with allure.step('3. Interact with Keahlian hint toggle'):
            await builder.skill_hints_click_hide()
            await builder.skill_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Keahlian Section Validation")
    @allure.feature("Keahlian")
    @allure.severity(severity.CRITICAL)
    async def test_proficient_section(self, builder):
        with allure.step('1. Validate Keahlian default state'):
            await builder.skill_main_form_presence()
            await builder.skill_title_presence()
            await builder.skill_desc_presence()
            await builder.skill_add_button_presence()
            await builder.skill_title_click_collapse()
            await builder.skill_title_click_expand()

        with allure.step('2. Click on the Add Keahlian Form button'):
            await builder.skill_click_add_form()

        with allure.step('3. Validate each input field completeness'):
            await builder.skill_name_input_presence()
            await builder.skill_level_presence()
            await builder.skill_cancel_form_btn_presence()
            await builder.skill_save_form_btn_presence()

        with allure.step('4. Insert a valid skill to the Keahlian Input Field'):
            await builder.skill_name_insert('Adobe')
            await builder.skill_name_clear_text()

        with allure.step('5. Interact with all Tingkat Keahlian options'):
            await builder.skill_level_click_pemula()
            await builder.skill_level_click_menengah()
            await builder.skill_level_click_lanjut()

        with allure.step('6. Click on the Save button'):
            await builder.skill_save_form_click()

        with allure.step('7. Click on the Cancel button'):
            await builder.skill_cancel_form_click()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Prestasi Hints Existence")
    @allure.feature("Prestasi", "Hints")
    @allure.severity(severity.MINOR)
    async def test_achievement_section_hints(self, builder):
        with allure.step('1. Click on the Add Prestasi Form button'):
            await builder.honor_click_add_form()

        with allure.step('2. Validate the Prestasi Hints section after form is added'):
            await builder.honor_main_hints_presence()
            await builder.honor_hints_title_presence()
            await builder.honor_hints_desc_presence()

        with allure.step('3. Interact with Keahlian hint toggle'):
            await builder.honor_hints_click_hide()
            await builder.honor_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Prestasi Section Validation")
    @allure.feature("Prestasi")
    @allure.severity(severity.CRITICAL)
    async def test_achievement_section(self, builder):
        with allure.step('1. Validate Prestasi default state'):
            await builder.honor_main_form_presence()