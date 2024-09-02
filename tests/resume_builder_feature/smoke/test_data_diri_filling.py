import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.data_diri import PersonalInformation


@pytest.fixture(scope='function')
async def data_diri(user_auth):
    data_diri = PersonalInformation(user_auth)
    await PreCond(data_diri.page).self_data_filling(user_auth)
    return data_diri


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@allure.feature("Resume Builder/ Data Diri", "Resume Builder/ Data Diri/ Saved State")
@pytest.mark.res_builder
@pytest.mark.data_diri
@pytest.mark.preview
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @pytest.mark.input_field
    @pytest.mark.auto_complete
    @pytest.mark.accordion
    @pytest.mark.save
    @allure.title("The Data Diri saved state should be exist after user click save on Data Diri form")
    @allure.severity(severity.NORMAL)
    async def test_data_diri_saved_state(self, data_diri):
        with allure.step('1. Verify that the Data Diri Initial state should be hidden'):
            await data_diri.hints_absence()
            await data_diri.first_name_absence()
            await data_diri.last_name_absence()
            await data_diri.email_absence()
            await data_diri.phone_absence()
            await data_diri.country_absence()
            await data_diri.province_absence()
            await data_diri.city_absence()
            await data_diri.address_absence()
            await data_diri.linkedin_absence()
            await data_diri.portfolio_absence()

        with allure.step('2. Verify that the Edit input action should be displayed'):
            await data_diri.saved_button_save_presence()
            await data_diri.saved_button_edit_presence()
            await data_diri.saved_button_delete_presence()

        with allure.step('3. Verify that the Data Diri saved state is exist'):
            await data_diri.saved_first_name_presence()
            await data_diri.saved_last_name_presence()
            await data_diri.saved_email_presence()
            await data_diri.saved_phone_presence()
            await data_diri.saved_province_presence()
            await data_diri.saved_city_presence()
            await data_diri.saved_address_presence()
            await data_diri.saved_linkedin_presence()
            await data_diri.saved_portfolio_presence()

    @pytest.mark.auto_complete
    @pytest.mark.accordion
    @allure.feature("Resume Builder/ Data Diri/ Preview")
    @allure.title("The Data Diri saved state should be exist after user click save on Data Diri form")
    async def test_data_diri_preview(self, data_diri):
        with allure.step('1. Verify that the Preview main section is exist'):
            await data_diri.preview_main_form_presence()
            await data_diri.preview_section_title_presence()
            await data_diri.preview_section_info_presence()

        with allure.step('2. Verify that the Data Diri preview is exist and matched the saved state'):
            await data_diri.preview_first_name_presence()
            await data_diri.preview_last_name_presence()
            await data_diri.preview_phone_presence()
            await data_diri.preview_email_presence()
            await data_diri.preview_linkedin_presence()
            await data_diri.preview_portfolio_presence()
            await data_diri.preview_province_presence()
            await data_diri.preview_city_presence()
            await data_diri.preview_address_presence()
