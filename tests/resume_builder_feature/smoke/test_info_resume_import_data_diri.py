import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder.info_resume import ResInfo
from pages.resume_builder import PreCond


@pytest.fixture(scope='function')
async def res_info(user_auth):
    res_info = ResInfo(user_auth)
    pre_cond = PreCond(res_info.page)
    await PreCond(res_info.page).import_data_modal()
    return res_info


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
    async def test_informasi_resume_import_modal(self, res_info):
        with allure.step('1. Validate the Import Data completeness'):
            await res_info.import_data_modal_title_presence()
            await res_info.import_data_modal_info_presence()
            await res_info.import_data_modal_close_presence()
            await res_info.import_data_myProfile_carousel_presence()
            await res_info.import_data_myResume_carousel_presence()

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
    async def test_informasi_resume_import_profile_modal(self, res_info, action, feature, request):
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
            await res_info.import_data_modal_click_my_profile()

        with allure.step('2. Validate the Import via Profile mandatory content'):
            await res_info.import_profile_modal_title_presence()
            await res_info.import_profile_modal_info_presence()
            await res_info.import_profile_modal_back_arrow_presence()
            await res_info.import_data_modal_form_presence()
            await res_info.import_form_self_data_presence()
            await res_info.import_form_self_data_check_presence()
            await res_info.import_form_self_data_name_presence()
            await res_info.import_form_self_data_email_presence()
            await res_info.import_form_self_data_phone_presence()
            await res_info.import_form_self_data_province_presence()
            await res_info.import_form_self_data_city_presence()

        with allure.step(f'3. Click on the "{action}" action button'):
            if action == "collapse":
                await res_info.import_form_collapse_self_data()
                await res_info.import_form_expand_self_data()
            elif action == "back_arrow":
                await res_info.import_profile_modal_click_back_arrow()
            elif action == "cancel":
                await res_info.import_profile_modal_click_cancel()
            elif action == "save":
                await res_info.import_form_uncheck_self_data()
                await res_info.import_form_check_self_data()
                await res_info.import_profile_modal_click_save()
            elif action == "close":
                await res_info.import_profile_modal_click_close()
