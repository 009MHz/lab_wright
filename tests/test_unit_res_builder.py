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
    @allure.feature("Resume Builder", "Informasi Resume", "Input Text", "Dropdown")
    async def test_informasi_resume_existence(self, builder):
        await builder.page_title_presence()
        await builder.info_section_title_presence()
        await builder.info_resume_name_title_presence()
        await builder.info_resume_name_input_presence()
        await builder.info_resume_lang_title_presence()
        await builder.info_resume_lang_input_presence()
        await builder.info_resume_goal_title_presence()
        await builder.info_resume_goal_desc_presence()
        await builder.info_resume_goal_input_presence()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Informasi Resume Interaction Check")
    @allure.feature("Resume Builder", "Informasi Resume", "Input Text", "Dropdown")
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


