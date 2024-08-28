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
@allure.story("Smoke Test", "Resume Builder/ Smoke Test")
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Data Diri Hints Existence")
    @allure.feature("Data Diri", "Hints", "Resume Builder/ Data Diri", "Resume Builder/ Data Diri/ Hints")
    @allure.severity(severity.MINOR)
    async def test_data_diri_hints(self, builder):
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
    @allure.feature("Data Diri", "Resume Builder/ Data Diri")
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
