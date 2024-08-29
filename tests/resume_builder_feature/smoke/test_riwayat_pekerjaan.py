import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.riwayat_pekerjaan import Profession


@pytest.fixture(scope='function')
async def vocation(user_auth):
    builder = Profession(user_auth)
    pre_cond = PreCond(builder.page)
    await pre_cond.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@allure.feature("Resume Builder/ Riwayat Pekerjaan")
@pytest.mark.res_builder
@pytest.mark.job_history
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @pytest.mark.toggle
    @allure.title("Riwayat Pekerjaan Hints Existence")
    @allure.feature("Resume Builder/ Riwayat Pekerjaan/ Hints")
    @allure.severity(severity.MINOR)
    async def test_occupation_section_hints(self, vocation):
        with allure.step('1. Click on the Add Riwayat Pekerjaan Form button'):
            await vocation.click_add_form()

        with allure.step('2. Validate the Hints section after form is added'):
            await vocation.main_hints_presence()
            await vocation.hints_title_presence()
            await vocation.hints_desc_presence()

        with allure.step('3. Interact with Riwayat Pendidikan hint toggle'):
            await vocation.click_hide_hints()
            await vocation.click_show_hints()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.accordion
    @pytest.mark.input_field
    @pytest.mark.auto_complete
    @pytest.mark.cancel
    @pytest.mark.save
    @allure.title("Riwayat Pekerjaan Existence")
    @allure.severity(severity.CRITICAL)
    async def test_occupation_section(self, vocation):
        with allure.step('1. Validate the section default state'):
            await vocation.section_title_presence()
            await vocation.section_desc_presence()
            await vocation.add_form_presence()
            await vocation.click_collapse_form()
            await vocation.click_expand_form()

        with allure.step('2. Click on the Add Riwayat Pekerjaan Form button'):
            await vocation.click_add_form()

        with allure.step('3. Validating each input field completeness'):
            await vocation.position_presence()
            await vocation.company_name_presence()
            await vocation.country_presence()
            await vocation.prov_presence()
            await vocation.city_presence()
            await vocation.status_presence()
            await vocation.start_date_presence()
            await vocation.end_date_presence()
            await vocation.cancel_form_btn_presence()
            await vocation.save_form_btn_presence()

        with allure.step('4. Interact with displayed position from the input keyword'):
            await vocation.select_position_option_within("Engine")

        with allure.step('5. Insert a valid text on Perusahaan input'):
            await vocation.insert_company_name('KarirLab')

        with allure.step('6. Select all options from Negara Perusahaan'):
            await vocation.country_select_wna()
            await vocation.country_select_wni()

        with allure.step('10. Interact with displayed Province from the input keyword'):
            await vocation.select_prov_option_within('Jak')

        with allure.step('11. Validate Kota Institusi'):
            await vocation.select_city_option_within('Jakarta')

        with allure.step('4. Validate Status Pekerjaan'):
            await vocation.click_status_full()
            await vocation.click_status_part()
            await vocation.click_status_freelance()
            await vocation.click_status_internship()
            await vocation.click_status_volunteer()

        with allure.step('12. Validate Waktu Mulai'):
            await vocation.insert_start_date("January", 2022)
            await vocation.clear_start_date()

        with allure.step('13. Validate Waktu Selesai'):
            await vocation.end_active_unchecking()
            await vocation.insert_end_date("December", 2022)
            await vocation.clear_end_date()
            await vocation.end_active_checking()

        with allure.step('14. Click on Simpan button'):
            await vocation.click_simpan_form()

        with allure.step('15. Click on Batal button'):
            await vocation.click_cancel_form()
