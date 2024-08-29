import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder.info_resume import ResInfo
from pages.resume_builder import PreCond


@pytest.fixture(scope='function')
async def res_info(user_auth):
    res_info = ResInfo(user_auth)
    pre_cond = PreCond(res_info.page)
    await pre_cond.import_data_modal()
    return res_info


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder Page")
@allure.feature("Resume Builder/ Informasi Resume/ Import Data",
                "Resume Builder/ Informasi Resume/ Import Data/ Resume Import")
@pytest.mark.res_builder
@pytest.mark.resume_info
@pytest.mark.import_data
@pytest.mark.popup
@pytest.mark.accordion
class TestSmokeResBuildImportPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.resume_import
    @allure.title("Import Data Via My Resume Validation")
    @allure.severity(severity.CRITICAL)
    @pytest.mark.parametrize("action, feature", [
        ("back_arrow", "Resume Builder/ Informasi Resume/ Import Data/ Resume Import/ Back Chevron"),
        ("cancel", "Resume Builder/ Informasi Resume/ Import Data/ Resume Import/ Cancel"),
        ("input", "Resume Builder/ Informasi Resume/ Import Data/ Resume Import/ Input"),
        ("close", "Resume Builder/ Informasi Resume/ Import Data/ Resume Import/ Close")])
    async def test_informasi_resume_import_resume_modal(self, res_info, action, feature, request):
        marker_mapping = {
            "back_arrow": pytest.mark.back_arrow,
            "cancel": pytest.mark.cancel,
            "input": pytest.mark.input_field,
            "close": pytest.mark.close}

        marker = marker_mapping.get(action)
        if marker:
            request.node.add_marker(marker)
        allure.dynamic.feature(feature)
        with allure.step('1. Click on the "Impor dari resume saya" carousel'):
            await res_info.import_data_modal_click_my_resume()

        with allure.step('2. Validate the Import via resume modal content'):
            await res_info.import_resume_modal_title_presence()
            await res_info.import_resume_modal_info_presence()
            await res_info.import_resume_modal_back_arrow_presence()
            await res_info.import_resume_input_name_presence()
            await res_info.import_resume_cancel_button_presence()
            await res_info.import_resume_save_button_presence()

        with allure.step(f'3. Click on the "{action}" action button'):
            if action == "back_chevron":
                await res_info.import_resume_modal_click_back_arrow()
            elif action == "input":
                await res_info.import_resume_modal_click_input()
            elif action == "cancel":
                await res_info.import_resume_modal_click_cancel()
            elif action == "close":
                await res_info.import_resume_modal_click_close()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.input
    @pytest.mark.checkbox
    @pytest.mark.save
    @allure.title("Import Data Via My Resume Save Action")
    @allure.feature("Resume Builder/ Informasi Resume/ Import Data/ Resume Import/ Save")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_resume_save(self, res_info):
        with allure.step('1. Click on the "Impor dari resume saya" carousel'):
            await res_info.import_data_modal_click_my_resume()

        with allure.step('2. Click on the Input resume name button'):
            await res_info.import_resume_modal_click_input()

        with allure.step('3. Click on the displayed resume'):
            await res_info.import_resume_modal_click_displayed_option()

        with allure.step('4. Verify the required information'):
            await res_info.import_data_modal_form_presence()
            await res_info.import_form_self_data_presence()
            await res_info.import_form_self_data_check_presence()
            await res_info.import_form_self_data_name_presence()
            await res_info.import_form_self_data_email_presence()
            await res_info.import_form_self_data_phone_presence()
            await res_info.import_form_self_data_province_presence()
            await res_info.import_form_self_data_city_presence()

        with allure.step('5. Interact with the action button'):
            await res_info.import_form_collapse_self_data()
            await res_info.import_form_expand_self_data()
            await res_info.import_form_uncheck_self_data()
            await res_info.import_form_check_self_data()

        with allure.step('6. Click on the Save button'):
            await res_info.import_resume_modal_click_save()
            # Todo: Verify the popup is dismissed
            # Todo: Verify the required Resume Form is not empty
            # Todo: Verify the required Resume Form preview is match
            pass
