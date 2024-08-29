import pytest
from pages.resume_builder.res_builder_page import Builder
import allure
from allure import severity_level as severity


@pytest.fixture(scope='function')
async def builder(user_auth):
    builder = Builder(user_auth)
    with allure.step("▸ Navigate the resume builder page"):
        await builder.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Smoke Test", "Resume Builder/ Smoke Test")
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Keahlian Hints Existence")
    @allure.feature("Keahlian", "Hints", "Resume Builder/ Keahlian", "Resume Builder/ Keahlian/ Hints")
    @allure.severity(severity.MINOR)
    async def test_proficient_section_hints(self, builder):
        with allure.step('1. Click on the Add Keahlian Form button'):
            await builder.skill_click_add_form()

        with allure.step('2. Validate the Keahlian Hints section after form is added'):
            await builder.skill_main_hints_presence()
            await builder.skill_hints_title_presence()
            await builder.skill_hints_desc_presence()

        with allure.step('3. Interact with Keahlian hint toggle'):
            await builder.skill_hints_click_hide()
            await builder.skill_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Keahlian Section Validation")
    @allure.feature("Keahlian", "Resume Builder/ Keahlian")
    @allure.severity(severity.CRITICAL)
    async def test_proficient_section(self, builder):
        with allure.step('1. Validate Keahlian default state'):
            await builder.skill_main_form_presence()
            await builder.skill_title_presence()
            await builder.skill_desc_presence()
            await builder.skill_add_button_presence()
            await builder.skill_title_click_collapse()
            await builder.skill_title_click_expand()

        with allure.step('2. Click on the Add Keahlian Form button'):
            await builder.skill_click_add_form()

        with allure.step('3. Validate each input field completeness'):
            await builder.skill_name_input_presence()
            await builder.skill_level_presence()
            await builder.skill_cancel_form_btn_presence()
            await builder.skill_save_form_btn_presence()

        with allure.step('4. Insert a valid skill to the Keahlian Input Field'):
            await builder.skill_name_insert('Adobe')
            await builder.skill_name_clear_text()

        with allure.step('5. Interact with all Tingkat Keahlian options'):
            await builder.skill_level_click_pemula()
            await builder.skill_level_click_menengah()
            await builder.skill_level_click_lanjut()

        with allure.step('6. Click on the Save button'):
            await builder.skill_save_form_click()

        with allure.step('7. Click on the Cancel button'):
            await builder.skill_cancel_form_click()
