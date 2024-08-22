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
class TestSmokeLoginPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Main Validation")
    @allure.feature("Informasi Resume", "Impor Data")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal(self, importer):
        with allure.step('1. Validate the Import Data completeness'):
            await importer.import_data_modal_title_presence()
            await importer.import_data_modal_info_presence()
            await importer.import_data_modal_close_presence()
            await importer.import_data_modal_myProfile_presence()
            await importer.import_data_modal_myResume_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Main Validation")
    @allure.feature("Informasi Resume", "Impor Data", "Import Close")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal(self, importer):
        with allure.step('1. Validate the Import Data completeness'):
            await importer.import_data_modal_title_presence()
            await importer.import_data_modal_info_presence()
            await importer.import_data_modal_close_presence()
            await importer.import_data_modal_myProfile_presence()
            await importer.import_data_modal_myResume_presence()
