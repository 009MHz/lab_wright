import pytest
from pages.resume_builder.info_resume import ResInfo
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def res_info(user_auth):
    builder = ResInfo(user_auth)
    with allure.step("▸ Navigate the resume builder page"):
        await builder.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@pytest.mark.res_builder
@pytest.mark.resume_info
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Validation")
    @allure.feature("Resume Builder/ Informasi Resume")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_section(self, res_info):
        with allure.step('1. Validating Page Header'):
            await res_info.page_title_presence()

        with allure.step('2. Validating Section Header'):
            await res_info.section_title_presence()

        with allure.step('3. Validating Nama resume'):
            await res_info.name_presence()
            await res_info.info_resume_name_insert("Written from playwright")

        with allure.step('4. Validating Bahasa Resume'):
            await res_info.language_presence()
            await res_info.info_resume_lang_click()
            await res_info.info_resume_select_bahasa()
            await res_info.info_resume_lang_click()
            await res_info.info_resume_select_language()

        with allure.step('5. Validating Tujuan Pekerjaan'):
            await res_info.tujuan_pekerjaan_presence()
            await res_info.info_resume_goal_click()
            await res_info.info_resume_goal_items_interact()

        with allure.step('6. Validating Import Data'):
            await res_info.info_resume_import_data_click()
            await res_info.import_data_modal_presence()
