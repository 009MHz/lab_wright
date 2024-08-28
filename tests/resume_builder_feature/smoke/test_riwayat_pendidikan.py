import pytest
from pages.resume_builder.res_builder_page import Builder
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def builder(user_auth):
    builder = Builder(user_auth)
    await builder.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Resume Builder/ Smoke Test")
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pendidikan Hints Existence")
    @allure.feature("Riwayat Pendidikan", "Hints", "Resume Builder/ Riwayat Pendidikan",
                    "Resume Builder/ Riwayat Pendidikan/ Hints")
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
    @allure.feature("Riwayat Pendidikan", "Resume Builder/ Riwayat Pendidikan")
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
