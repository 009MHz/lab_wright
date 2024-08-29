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
@allure.story("Smoke Testing: Resume Builder Page")
@allure.feature("Resume Builder/ Informasi Resume/ Import Data",
                "Resume Builder/ Informasi Resume/ Import Data/ Resume Import")
@pytest.mark.res_builder
@pytest.mark.resume_info
@pytest.mark.import_data
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
    async def test_informasi_resume_import_resume_modal(self, builder, action, feature, request):
        marker_mapping = {
            "back_arrow": pytest.mark.back_arrow,
            "cancel": pytest.mark.cancel,
            "input": pytest.mark.input_field,
            "close": pytest.mark.close
        }

        marker = marker_mapping.get(action)
        if marker:
            request.node.add_marker(marker)

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
                await builder.import_resume_modal_click_back_arrow()
            elif action == "input":
                await builder.import_resume_modal_click_input()
            elif action == "cancel":
                await builder.import_resume_modal_click_cancel()
            elif action == "close":
                await builder.import_resume_modal_click_close()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Import Data Via My Resume Save Action")
    @allure.feature("Informasi Resume", "Impor Data", "Resume Import", "Resume Import/ Save")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_import_resume_save(self, builder):
        with allure.step('1. Click on the "Impor dari resume saya" carousel'):
            await builder.import_data_modal_click_my_resume()

        with allure.step('2. Click on the Input resume name button'):
            await builder.import_resume_modal_click_input()

        with allure.step('3. Click on the displayed resume'):
            await builder.import_resume_modal_click_displayed_option()

        with allure.step('4. Verify the required information'):
            await builder.import_data_modal_form_presence()
            await builder.import_form_self_data_presence()
            await builder.import_form_self_data_check_presence()
            await builder.import_form_self_data_name_presence()
            await builder.import_form_self_data_email_presence()
            await builder.import_form_self_data_phone_presence()
            await builder.import_form_self_data_province_presence()
            await builder.import_form_self_data_city_presence()

        with allure.step('5. Interact with the action button'):
            await builder.import_form_collapse_self_data()
            await builder.import_form_expand_self_data()
            await builder.import_form_uncheck_self_data()
            await builder.import_form_check_self_data()

        with allure.step('6. Click on the Save button'):
            await builder.import_resume_modal_click_save()
            # Todo: Verify the popup is dismissed
            # Todo: Verify the required Resume Form is not empty
            # Todo: Verify the required Resume Form preview is match
            pass
