import pytest
from pages.resume_builder.res_builder_page import Builder
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def builder(user_auth):
    builder = Builder(user_auth)
    with allure.step("▸ Navigate the resume builder page"):
        await builder.load_page()
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
    @allure.title("Riwayat Pekerjaan Hints Existence")
    @allure.feature("Resume Builder/ Riwayat Pekerjaan/ Hints")
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
