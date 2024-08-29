import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.data_diri import PersonalInformation


@pytest.fixture(scope='function')
async def data_diri(user_auth):
    data_diri = PersonalInformation(user_auth)
    pre_cond = PreCond(data_diri.page)
    await pre_cond.load_page()
    return data_diri


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@allure.feature("Resume Builder/ Data Diri")
@pytest.mark.res_builder
@pytest.mark.data_diri
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @pytest.mark.toggle
    @allure.title("Data Diri Hints Existence")
    @allure.feature("Resume Builder/ Data Diri/ Hints")
    @allure.severity(severity.MINOR)
    async def test_data_diri_hints(self, data_diri):
        with allure.step('Validating Hints Component'):
            await data_diri.hints_title_presence()
            await data_diri.hints_desc_presence()
            await data_diri.hints_toggle_presence()

        with allure.step('Interact with Data Diri hint toggle'):
            await data_diri.hints_click_hide()
            await data_diri.hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.input_field
    @pytest.mark.auto_complete
    @pytest.mark.accordion
    @pytest.mark.cancel
    @pytest.mark.save
    @allure.title("Data Diri Existence Validation")
    @allure.severity(severity.CRITICAL)
    async def test_data_diri_section(self, data_diri):
        with allure.step('1. Validating each input field completeness'):
            await data_diri.main_form_presence()
            await data_diri.hints_presence()
            await data_diri.section_title_presence()
            await data_diri.first_name_presence()
            await data_diri.last_name_presence()
            await data_diri.email_presence()
            await data_diri.phone_presence()
            await data_diri.country_presence()
            await data_diri.province_presence()
            await data_diri.city_presence()
            await data_diri.address_presence()
            await data_diri.linkedin_presence()
            await data_diri.portfolio_presence()
            await data_diri.save_form_presence()

        with allure.step('2. Interact the section header accordion'):
            await data_diri.collapse_form()
            await data_diri.expand_form()

        with allure.step('3. Insert any text on the Nama Depan Field'):
            await data_diri.insert_first_name('Mr. John ')

        with allure.step('4. Insert any text on the Nama Belakang Field'):
            await data_diri.insert_last_name('Toryono ,M.Sc')

        with allure.step('5. Insert any text on the Email Field'):
            await data_diri.insert_email('ali.nA_p3tr|nK0vA@yahoo.us')

        with allure.step('6. Insert a valid phone number on the No. Telepon field'):
            await data_diri.insert_phone('08987654321')

        with allure.step('7. Click on the Negara option'):
            await data_diri.country_select_wna()
            await data_diri.country_select_wni()

        with allure.step('8. Select displayed province from the input keyword'):
            await data_diri.select_province_option_within('Jawa')

        with allure.step('9. Select displayed city from the input keyword'):
            await data_diri.select_city_option_within('Ban')

        with allure.step('10. Insert any text on the Alamat Field'):
            await data_diri.insert_address("Jl. Belawan No.16, RT.18/RW.1, Cideng")

        with allure.step('11. Insert a valid Linkedin url'):
            await data_diri.insert_linkedin("https://www.linkedin.com/company/karirlab")

        with allure.step('12. Insert a valid url on the portfolio field'):
            await data_diri.insert_portfolio('https://github.com/microsoft/playwright')

        with allure.step('13. Click on the simpan button'):
            await data_diri.click_simpan_button()
