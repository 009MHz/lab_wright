import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.prestasi import Prestasi


@pytest.fixture(scope='function')
async def achievement(user_auth):
    builder = Prestasi(user_auth)
    pre_cond = PreCond(builder.page)
    await pre_cond.load_page()
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
    async def test_achievement_section_hints(self, achievement):
        with allure.step('1. Click on the Add Prestasi Form button'):
            await achievement.click_add_form()

        with allure.step('2. Validate the Prestasi Hints section after form is added'):
            await achievement.hints_presence()
            await achievement.hints_title_presence()
            await achievement.hints_desc_presence()

        with allure.step('3. Interact with Keahlian hint toggle'):
            await achievement.hints_click_hide()
            await achievement.hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Prestasi Section Validation")
    @allure.feature("Resume Builder/ Achievements")
    @allure.severity(severity.CRITICAL)
    async def test_achievement_section(self, achievement):
        with allure.step('1. Validate Prestasi form default state'):
            await achievement.main_form_presence()
            await achievement.section_title_presence()
            await achievement.section_desc_presence()
            await achievement.add_form_presence()
            await achievement.collapse_form()
            await achievement.expand_form()

        with allure.step('2. Click on the Add Prestasi Form button'):
            await achievement.click_add_form()

        with allure.step('3. Validate each input field completeness'):
            await achievement.year_presence()
            await achievement.name_presence()
            await achievement.cancel_form_presence()
            await achievement.save_form_presence()

        with allure.step('4. Interact with the year insert field'):
            await achievement.insert_year(2005)
            await achievement.clear_year()

        with allure.step('5. Interact with the Achievement title insert field'):
            await achievement.insert_name("UEFA Champions MVP")
            await achievement.clear_name()

        with allure.step('6. Click on the Save button'):
            await achievement.click_save_form()

        with allure.step('7. Click on the Cancel button'):
            await achievement.click_cancel_form()
