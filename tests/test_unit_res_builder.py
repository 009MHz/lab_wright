import pytest
from pages.res_builder_page import Builder
import allure


@pytest.fixture(scope='function')
async def builder(auth_page):
    builder = Builder(auth_page)
    await builder.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Resume Builder/ Smoke Test")
class TestSmokeLoginPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Existence Validation")
    @allure.feature("Informasi Resume")
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
    async def test_data_diri_section(self, builder):
        with allure.step('1. Validating Main Form Existence'):
            await builder.self_info_main_form_presence()
            await builder.self_info_main_hints_presence()
        with allure.step('2. Validating Section Header'):
            await builder.self_info_title_presence()
            await builder.self_info_collapse_form()
            await builder.self_info_expand_form()
        with allure.step('3. Validating Nama Depan'):
            await builder.self_info_first_name_presence()
            await builder.self_info_first_name_insert('Mr. John')
        with allure.step('4. Validating Nama Belakang'):
            await builder.self_info_last_name_presence()
            await builder.self_info_last_name_insert('Doe ,M.Sc')
        with allure.step('5. Validating Email'):
            await builder.self_info_email_presence()
            await builder.self_info_email_insert('ali.nA_p3tr|nK0vA@yahoo.us')
        with allure.step('6. Validating No. Telepon'):
            await builder.self_info_phone_presence()
            await builder.self_info_phone_insert('08987654321')
        with allure.step('7. Validating Negara'):
            await builder.self_info_country_presence()
            await builder.self_info_click_country()
            await builder.self_info_select_wna()
            await builder.self_info_click_country()
            await builder.self_info_select_wni()
        with allure.step('8. Validating Provinsi'):
            await builder.self_info_prov_presence()
            await builder.self_info_prov_insert('Pap')
            await builder.self_info_prov_click_all_prov()
        with allure.step('9. Validating Kota'):
            await builder.self_info_city_presence()
            await builder.self_info_city_insert('Jakarta')
            await builder.self_info_city_click_all_city()
        with allure.step('10. Validating Alamat'):
            await builder.self_info_address_presence()
            await builder.self_info_address_insert("Jl. Belawan No.16, RT.18/RW.1, Cideng")
        with allure.step('11. Validating Linkedin'):
            await builder.self_info_linkedin_presence()
            await builder.self_info_linkedin_insert("https://www.linkedin.com/company/karirlab")
        with allure.step('12. Validating Linkedin'):
            await builder.self_info_portfolio_presence()
            await builder.self_info_portfolio_insert('https://github.com/microsoft/playwright')
        with allure.step('13. Validating Simpan Button'):
            await builder.self_info_simpan_btn_presence()
            await builder.self_info_click_simpan()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pendidikan Hints Existence")
    @allure.feature("Riwayat Pendidikan", "Hints")
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
    @allure.title("Riwayat Pendidikan Existence")
    @allure.feature("Riwayat Pendidikan")
    async def test_education_section(self, builder):
        with allure.step('1. Validate the section default state'):
            await builder.edu_title_presence()
            await builder.edu_desc_presence()
            await builder.edu_add_form_button_presence()
            await builder.edu_title_click_collapse()
            await builder.edu_title_click_expand()
        with allure.step('2. Click on the Add Riwayat Pendidikan Form button'):
            await builder.edu_click_add_form()
        with allure.step('3. Validate the empty state form'):
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
        with allure.step('4. Validate Jenjang Pendidikan'):
            degree_options = [
                builder.edu_click_degree_sma,
                builder.edu_click_degree_d1,
                builder.edu_click_degree_d2,
                builder.edu_click_degree_d3,
                builder.edu_click_degree_d4,
                builder.edu_click_degree_s1,
                builder.edu_click_degree_s2,
                builder.edu_click_degree_s3,
                builder.edu_click_degree_course]

            for select_degree in degree_options:
                await builder.edu_click_degree()
                await select_degree()
        with allure.step('5. Validate Nama Institusi'): # possibility fail
            await builder.edu_institution_click_empty()
            await builder.edu_institution_select_all_option("Univ")
        with allure.step('6. Validate Jurusan'):
            await builder.edu_faculty_click_empty()
            await builder.faculty_select_all_option('Bis')
        with allure.step('7. Validate IPK atau Nilai'):
            pass
        with allure.step('8. Validate IPK atau Nilai'):
            pass
        with allure.step('9. Validate Skala Maximum'):
            pass
        with allure.step('10. Validate Negara Institusi'):
            pass
        with allure.step('11. Validate Provinsi Institusi'):
            pass
        with allure.step('12. Validate Kota Institusi'):
            pass
        with allure.step('13. Validate Waktu Mulai'):
            pass
        with allure.step('14. Validate Waktu Lulus'):
            pass
        with allure.step('15. Click on Simpan button'):
            pass
        with allure.step('16. Click on Add form button'):
            pass
        with allure.step('17. Click on Batal button'):
            pass
