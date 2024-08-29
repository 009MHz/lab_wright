import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder.info_resume import ResInfo
from pages.resume_builder import PreCond


@pytest.fixture(scope='function')
async def res_info(user_auth):
    res_info = ResInfo(user_auth)
    pre_cond = PreCond(res_info.page)
    await pre_cond.load_page()
    return res_info


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@pytest.mark.res_builder
@pytest.mark.resume_info
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.input_field
    @pytest.mark.accordion
    @allure.title("Informasi Resume Validation")
    @allure.feature("Resume Builder/ Informasi Resume")
    @allure.severity(severity.CRITICAL)
    async def test_informasi_resume_section(self, res_info):
        with allure.step('1. Validating Section Header'):
            await res_info.section_title_presence()

        with allure.step('2. Validating Nama resume'):
            await res_info.name_presence()
            await res_info.name_insert("Written from playwright")

        with allure.step('3. Validating Bahasa Resume'):
            await res_info.language_presence()
            await res_info.lang_click()
            await res_info.lang_select_bahasa()
            await res_info.lang_click()
            await res_info.lang_select_language()

        with allure.step('4. Validating Tujuan Pekerjaan'):
            await res_info.tujuan_pekerjaan_presence()
            await res_info.tujuan_pekerjaan_click()
            await res_info.tujuan_items_interact()

        with allure.step('5. Validating Import Data'):
            await res_info.import_data_click()
            await res_info.import_data_modal_presence()
