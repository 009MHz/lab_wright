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
    @allure.feature("Resume Builder", "Input Text", "Dropdown")
    async def test_informasi_resume_section(self, builder):
        await builder.page_title_presence()
        await builder.info_section_title_presence()
        await builder.info_resume_name_title_presence()
        await builder.info_resume_name_input_presence()
        await builder.info_resume_lang_title_presence()
        await builder.info_resume_lang_input_presence()
        await builder.info_resume_goal_title_presence()
        await builder.info_resume_goal_desc_presence()
        await builder.info_resume_goal_input_presence()
