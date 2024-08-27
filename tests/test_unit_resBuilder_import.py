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
    @allure.feature("Resume Builder", "Informasi Resume", "Impor Data")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal(self, builder):
        with allure.step('1. Validate the Import Data completeness'):
            await builder.import_data_modal_title_presence()
            await builder.import_data_modal_info_presence()
            await builder.import_data_modal_close_presence()
            await builder.import_data_myProfile_carousel_presence()
            await builder.import_data_myResume_carousel_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Close Action Validation")
    @allure.feature("Resume Builder", "Informasi Resume", "Impor Data", "Import Close")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_modal_close(self, builder):
        with allure.step('1. Click on the modal close button'):
            await builder.import_data_modal_click_close()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Via My Profile Interaction")
    @allure.severity(severity.CRITICAL)
    @allure.feature("Resume Builder", "Informasi Resume", "Impor Data", "Profile Import")
    @pytest.mark.parametrize("action, feature", [
        ("toggle", "Profile Import/ Toggle"),
        ("back_arrow", "Profile Import/ Back Chevron"),
        ("cancel", "Profile Import/ Cancel"),
        ("save", "Profile Import/ Save"),
        ("close", "Profile Import/ Close")
    ])
    async def test_informasi_resume_import_profile_modal(self, builder, action, feature):
        allure.dynamic.feature(feature)

        with allure.step('1. Click on the "Impor dari profil saya" carousel'):
            await builder.import_data_modal_click_my_profile()

        with allure.step('2. Validate the Import via Profile mandatory content'):
            await builder.import_profile_modal_title_presence()
            await builder.import_profile_modal_info_presence()
            await builder.import_profile_modal_back_arrow_presence()
            await builder.import_profile_modal_form_presence()
            await builder.import_profile_self_data_form_presence()
            await builder.import_profile_self_data_check_presence()
            await builder.import_profile_self_data_name_presence()
            await builder.import_profile_self_data_email_presence()
            await builder.import_profile_self_data_phone_presence()
            await builder.import_profile_self_data_province_presence()
            await builder.import_profile_self_data_city_presence()

        with allure.step(f'3. Click on the "{action}" action button'):
            if action == "collapse":
                await builder.import_profile_collapse_self_data()
                await builder.import_profile_expand_self_data()
            elif action == "back_arrow":
                await builder.import_profile_modal_click_back_arrow()
            elif action == "cancel":
                await builder.import_profile_modal_click_cancel()
            elif action == "save":
                await builder.import_profile_modal_click_save()
            elif action == "close":
                await builder.import_profile_modal_click_close()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Via My Resume Validation")
    @allure.feature("Informasi Resume", "Impor Data", "Resume Import")
    @allure.severity(severity.CRITICAL)
    @pytest.mark.parametrize("action, feature", [
        ("back_chevron", "Resume Import/ Back Chevron"),
        ("input", "Resume Import/ Input Resume"),
        ("cancel", "Resume Import/ Cancel"),
        ("save", "Resume Import/ Save"),
        ("close", "Resume Import/ Close")
    ])
    async def test_informasi_resume_import_resume_modal(self, builder, action, feature):
        allure.dynamic.feature(feature)

        with allure.step('1. Click on the "Impor dari resume saya" carousel'):
            await builder.import_data_modal_click_my_resume()

        with allure.step('2. Validate the Import via resume modal content'):
            await builder.import_resume_modal_title_presence()
            await builder.import_resume_modal_info_presence()
            await builder.import_resume_modal_back_arrow_presence()
            await builder.import_resume_input_name_presence()
            await builder.import_resume_cancel_button_presence()
            await builder.import_resume_save_button_presence()

        with allure.step(f'3. Click on the "{action}" action button'):
            if action == "back_chevron":
                pass
                # Todo: Click Back chevron
                # Todo: Validate the previous input form
            elif action == "input":
                # Todo: Click Input Resume Name
                # Todo: Validate The Resume Name List
                pass
            elif action == "cancel":
                # Todo: Click Cancel button
                # Todo: Validate the popup dismissed
                pass
            elif action == "save":
                # Todo: Click Save button
                # Todo: Validate the no action
                pass
            elif action == "close":
                # Todo: Click Close button
                # Todo: Validate the popup dismissed
                pass

