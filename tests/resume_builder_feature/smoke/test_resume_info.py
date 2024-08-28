import pytest
from pages.resume_builder.res_builder_page import Builder
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def builder(user_auth):
    builder = Builder(user_auth)
    await builder.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Resume Builder/ Smoke Test")
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Validation")
    @allure.feature("Resume Builder", "Informasi Resume", "Resume Builder/ Informasi Resume")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_section(self, builder):
        with allure.step('1. Validating Page Header'):
            await builder.page_title_presence()

        with allure.step('2. Validating Section Header'):
            await builder.info_section_title_presence()

        with allure.step('3. Validating Nama resume'):
            await builder.info_resume_name_presence()
            await builder.info_resume_name_insert("Written from playwright")

        with allure.step('4. Validating Bahasa Resume'):
            await builder.info_resume_language_presence()
            await builder.info_resume_lang_click()
            await builder.info_resume_select_bahasa()
            await builder.info_resume_lang_click()
            await builder.info_resume_select_language()

        with allure.step('5. Validating Tujuan Pekerjaan'):
            await builder.info_resume_goal_title_presence()
            await builder.info_resume_tujuan_presence()
            await builder.info_resume_goal_click()
            await builder.info_resume_goal_items_interact()

        with allure.step('6. Validating Import Data'):
            await builder.info_resume_import_data_click()
            await builder.import_data_modal_presence()
