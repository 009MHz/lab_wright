import pytest
from pages.resume_builder.res_builder_page import Builder
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
@allure.story("Smoke Testing: Resume Builder")
@pytest.mark.res_builder
@pytest.mark.resume_info
@pytest.mark.import_data
@allure.feature("Resume Builder/ Informasi Resume/ Import Data")
class TestSmokeResBuildImportPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Main Validation")
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
    @pytest.mark.profile_import
    @allure.title("Import Data Via My Profile Interaction")
    @allure.severity(severity.CRITICAL)
    @allure.feature("Resume Builder/ Informasi Resume/ Import Data/ Profile Import")
    @pytest.mark.parametrize("action, feature", [
        ("toggle", "Resume Builder/ Informasi Resume/ Import Data/ Profile Import/ Toggle"),
        ("back_arrow", "Resume Builder/ Informasi Resume/ Import Data/ Profile Import/ Back Chevron"),
        ("cancel", "Resume Builder/ Informasi Resume/ Import Data/ Profile Import/ Cancel"),
        ("save", "Resume Builder/ Informasi Resume/ Import Data/ Profile Import/ Save"),
        ("close", "Resume Builder/ Informasi Resume/ Import Data/ Profile Import/ Close")])
    async def test_informasi_resume_import_profile_modal(self, builder, action, feature, request):
        marker_mapping = {
            "toggle": pytest.mark.toggle,
            "back_arrow": pytest.mark.back_arrow,
            "cancel": pytest.mark.cancel,
            "save": pytest.mark.save,
            "close": pytest.mark.close
        }

        marker = marker_mapping.get(action)
        if marker:
            request.node.add_marker(marker)

        allure.dynamic.feature(feature)

        with allure.step('1. Click on the "Impor dari profil saya" carousel'):
            await builder.import_data_modal_click_my_profile()

        with allure.step('2. Validate the Import via Profile mandatory content'):
            await builder.import_profile_modal_title_presence()
            await builder.import_profile_modal_info_presence()
            await builder.import_profile_modal_back_arrow_presence()
            await builder.import_data_modal_form_presence()
            await builder.import_form_self_data_presence()
            await builder.import_form_self_data_check_presence()
            await builder.import_form_self_data_name_presence()
            await builder.import_form_self_data_email_presence()
            await builder.import_form_self_data_phone_presence()
            await builder.import_form_self_data_province_presence()
            await builder.import_form_self_data_city_presence()

        with allure.step(f'3. Click on the "{action}" action button'):
            if action == "collapse":
                await builder.import_form_collapse_self_data()
                await builder.import_form_expand_self_data()
            elif action == "back_arrow":
                await builder.import_profile_modal_click_back_arrow()
            elif action == "cancel":
                await builder.import_profile_modal_click_cancel()
            elif action == "save":
                await builder.import_form_uncheck_self_data()
                await builder.import_form_check_self_data()
                await builder.import_profile_modal_click_save()
            elif action == "close":
                await builder.import_profile_modal_click_close()
