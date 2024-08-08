import pytest
from pages.res_builder_page import Builder
import allure


@pytest.fixture(scope='function')
async def builder(auth_page):
    builder = Builder(auth_page)
    await builder.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Resume Builder Smoke Test")
class TestSmokeLoginPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Existence Validation")
    @allure.feature("Informasi Resume")
    async def test_informasi_resume_existence(self, builder):
        with allure.step('Validating Page Header'):
            await builder.page_title_presence()
        with allure.step('Validating Section Header'):
            await builder.info_section_title_presence()
        with allure.step('Validating Nama resume'):
            await builder.info_resume_name_title_presence()
            await builder.info_resume_name_input_presence()
        with allure.step('Validating Bahasa Resume'):
            await builder.info_resume_lang_title_presence()
            await builder.info_resume_lang_input_presence()
        with allure.step('Validating Tujuan Pekerjaan'):
            await builder.info_resume_goal_title_presence()
            await builder.info_resume_goal_desc_presence()
            await builder.info_resume_goal_input_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Interaction Check")
    @allure.feature("Informasi Resume")
    async def test_informasi_resume_interaction(self, builder):
        with allure.step('Insert Text on the Nama Resume Input Field'):
            await builder.info_resume_name_insert("Written from playwright")
        with allure.step('Select each Bahasa Resume Option'):
            await builder.info_resume_lang_click()
            await builder.info_resume_select_bahasa()
            await builder.info_resume_lang_click()
            await builder.info_resume_select_language()
        with allure.step('Select each Tujuan Pekerjaan Option'):
            await builder.info_resume_goal_click()
            await builder.info_resume_goal_items_interact()
        with allure.step('Click on Impor Data button'):
            await builder.info_resume_import_data_click()
            await builder.import_data_modal_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Data Diri Existence Validation")
    @allure.feature("Data Diri")
    async def test_data_diri_form_existence(self, builder):
        with allure.step('Validating Section Header'):
            await builder.self_info_title_presence()
        with allure.step('Validating Nama Depan'):
            await builder.self_info_first_name_presence()
        with allure.step('Validating Nama Belakang'):
            await builder.self_info_last_name_presence()
        with allure.step('Validating Email'):
            await builder.self_info_email_presence()
        with allure.step('Validating Email'):
            await builder.self_info_phone_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Existence Hints Validation")
    @allure.feature("Data Diri", "Hints")
    async def test_data_diri_hints_existence(self, builder):
        with allure.step('Validating Hints Component'):
            await builder.self_info_hints_title_presence()
            await builder.self_info_hints_desc_presence()
            await builder.self_info_hints_toggle_presence()
