import pytest
from pages.res_builder_page import Builder
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def builder(user_auth):
    builder = Builder(user_auth)
    with allure.step("▸ Navigate the resume builder page"):
        await builder.load_page()
    with allure.step("▸ Click on the Import Data button"):
        await builder.info_resume_import_data_click()
        await builder.import_data_modal_presence()
    return builder


@allure.epic("Resume Builder")
@allure.story("Resume Builder/ Smoke Test")
class TestSmokeResBuildImportPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Main Validation")
    @allure.feature("Informasi Resume", "Impor Data")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal(self, builder):
        with allure.step('1. Validate the Import Data completeness'):
            await builder.import_data_modal_title_presence()
            await builder.import_data_modal_info_presence()
            await builder.import_data_modal_close_presence()
            await builder.import_data_modal_myProfile_presence()
            await builder.import_data_modal_myResume_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Close Action Validation")
    @allure.feature("Informasi Resume", "Impor Data", "Import Close")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal_close(self, builder):
        with allure.step('1. Click on the modal close button'):
            await builder.import_data_modal_click_close()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Via My Profile Validation")
    @allure.feature("Informasi Resume", "Impor Data", "Profile Import")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal_my_profile(self, builder):
        with allure.step('1. Click on the "Impor dari profil saya" carousel'):
            await builder.import_data_modal_click_my_profile()

        with allure.step('2. Validate the Import via Profile modal content'):
            pass

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Via My Resume Validation")
    @allure.feature("Informasi Resume", "Impor Data", "Resume Import")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal_my_resume(self, builder):
        with allure.step('1. Click on the "Impor dari resume saya" carousel'):
            await builder.import_data_modal_click_my_resume()

        with allure.step('2. Validate the Import via resume modal content'):
            pass
