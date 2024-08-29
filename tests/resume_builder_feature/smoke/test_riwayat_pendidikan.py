import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.riwayat_pendidikan import Education


@pytest.fixture(scope='function')
async def education(user_auth):
    builder = Education(user_auth)
    pre_cond = PreCond(builder.page)
    await pre_cond.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@allure.feature("Resume Builder/ Riwayat Pendidikan")
@pytest.mark.res_builder
@pytest.mark.history
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pendidikan Hints Existence")
    @allure.feature("Resume Builder/ Riwayat Pendidikan/ Hints")
    @allure.severity(severity.NORMAL)
    async def test_education_section_hints(self, education):
        with allure.step('1. Click on the Add Riwayat Pendidikan Form button'):
            await education.click_add_form()

        with allure.step('2. Validate the Hints section after form is added'):
            await education.hints_presence()
            await education.hints_title_presence()
            await education.hints_desc_presence()

        with allure.step('3. Interact with Riwayat Pendidikan hint toggle'):
            await education.hints_click_hide()
            await education.hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Riwayat Pendidikan Validation")
    @allure.severity(severity.CRITICAL)
    async def test_education_section(self, education):
        with allure.step('1. Validate riwayat pendidikan default state'):
            await education.section_title_presence()
            await education.section_desc_presence()
            await education.add_form_presence()
            await education.title_click_collapse()
            await education.title_click_expand()

        with allure.step('2. Click on the Add Riwayat Pendidikan Form button'):
            await education.click_add_form()

        with allure.step('3. Validating each input field completeness'):
            await education.degree_presence()
            await education.institution_presence()
            await education.faculty_presence()
            await education.gpa_presence()
            await education.max_score_presence()
            await education.country_presence()
            await education.prov_presence()
            await education.city_presence()
            await education.start_presence()
            await education.end_presence()
            await education.cancel_form_btn_presence()
            await education.save_form_btn_presence()

        with allure.step('4. Click on each Jenjang Pendidikan option'):
            await education.click_degree_sma()
            await education.click_degree_d1()
            await education.click_degree_d2()
            await education.click_degree_d3()
            await education.click_degree_d4()
            await education.click_degree_s1()
            await education.click_degree_s2()
            await education.click_degree_s3()
            await education.click_degree_course()
            await education.click_degree_s1()

        with allure.step('5. Interact with displayed Institution from the input keyword'):
            await education.institution_select_option_within("Univ")

        with allure.step('6. Select displayed faculty from the input keyword'):
            await education.faculty_select_option_within('Bis')

        with allure.step('7. Interact with the GPA input field'):
            await education.faculty_gpa_insert('3.8')
            await education.faculty_gpa_score_increase(3)
            await education.faculty_gpa_score_decrease(2)

        with allure.step('8. Interact with the max score input field'):
            await education.faculty_max_gpa_insert('4.2')
            await education.faculty_max_gpa_score_increase(2)
            await education.faculty_max_gpa_score_decrease(3)

        with allure.step('9. Select all options from Negara institusi'):
            await education.select_wna()
            await education.select_wni()

        with allure.step('10. Select displayed province from the input keyword'):
            await education.prov_select_option_within('Sum')

        with allure.step('11. Validate Kota Institusi'):
            await education.city_select_option_within('tan')

        with allure.step('12. Validate Waktu Mulai'):
            await education.start_date_insert("August", 2016)
            await education.start_date_clear()

        with allure.step('13. Validate Waktu Lulus'):
            await education.end_active_unchecking()
            await education.end_date_insert("December", 2021)
            await education.end_date_clear()
            await education.end_active_checking()

        with allure.step('14. Click on Simpan button'):
            await education.save_btn_click()

        with allure.step('15. Click on Batal button'):
            await education.cancel_btn_click()
