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
@allure.story("Smoke Testing: Resume Builder")
@pytest.mark.res_builder
@pytest.mark.achievement
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @allure.title("Prestasi Hints Existence")
    @allure.feature("Resume Builder/ Achievements", "Resume Builder/ Achievements/ Hints")
    @allure.severity(severity.MINOR)
    async def test_achievement_section_hints(self, builder):
        with allure.step('1. Click on the Add Prestasi Form button'):
            await builder.honor_click_add_form()

        with allure.step('2. Validate the Prestasi Hints section after form is added'):
            await builder.honor_main_hints_presence()
            await builder.honor_hints_title_presence()
            await builder.honor_hints_desc_presence()

        with allure.step('3. Interact with Keahlian hint toggle'):
            await builder.honor_hints_click_hide()
            await builder.honor_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Prestasi Section Validation")
    @allure.feature("Resume Builder/ Achievements")
    @allure.severity(severity.CRITICAL)
    async def test_achievement_section(self, builder):
        with allure.step('1. Validate Prestasi form default state'):
            await builder.honor_main_form_presence()
            await builder.honor_title_presence()
            await builder.honor_desc_presence()
            await builder.honor_add_button_presence()
            await builder.honor_title_click_collapse()
            await builder.honor_title_click_expand()

        with allure.step('2. Click on the Add Prestasi Form button'):
            await builder.honor_click_add_form()

        with allure.step('3. Validate each input field completeness'):
            await builder.honor_year_presence()
            await builder.honor_name_input_presence()
            await builder.honor_cancel_form_btn_presence()
            await builder.honor_save_form_btn_presence()

        with allure.step('4. Interact with the year insert field'):
            await builder.honor_year_insert(2005)
            await builder.honor_year_clear()

        with allure.step('5. Interact with the Achievement title insert field'):
            await builder.honor_name_insert("UEFA Champions MVP")
            await builder.honor_name_clear()

        with allure.step('6. Click on the Save button'):
            await builder.honor_save_form_click()

        with allure.step('7. Click on the Cancel button'):
            await builder.honor_cancel_form_click()
