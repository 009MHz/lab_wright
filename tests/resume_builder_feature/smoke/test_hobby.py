import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.minat import Minat


@pytest.fixture(scope='function')
async def hobby(user_auth):
    hobby = Minat(user_auth)
    pre_cond = PreCond(hobby.page)
    await pre_cond.load_page()
    return hobby


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@allure.feature("Resume Builder/ Minat")
@pytest.mark.res_builder
@pytest.mark.minat
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @pytest.mark.toggle
    @allure.title("Minat Hints Existence")
    @allure.feature("Resume Builder/ Minat/ Hints")
    @allure.severity(severity.MINOR)
    async def test_minat_section_hints(self, hobby):
        with allure.step('1. Click on the Add Minat Form button'):
            await hobby.click_add_form()

        with allure.step('2. Validate the Minat Hints section after form is added'):
            await hobby.hints_presence()
            await hobby.hints_title_presence()
            await hobby.hints_desc_presence()

        with allure.step('3. Interact with Minat hint toggle'):
            await hobby.click_toggle_hide_hints()
            await hobby.click_toggle_show_hints()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.input_field
    @pytest.mark.accordion
    @pytest.mark.cancel
    @pytest.mark.save
    @allure.title("Minat Section Validation")
    @allure.severity(severity.CRITICAL)
    async def test_minat_section(self, hobby):
        with allure.step('1. Validate Minat form default state'):
            await hobby.main_section_presence()
            await hobby.section_title_presence()
            await hobby.section_info_presence()
            await hobby.add_form_presence()
            await hobby.click_collapse_form()
            await hobby.click_expand_form()

        with allure.step('2. Click on the Add Minat Form button'):
            await hobby.click_add_form()

        with allure.step('3. Validate each input field completeness'):
            await hobby.name_input_presence()
            await hobby.cancel_form_presence()
            await hobby.save_form_presence()

        with allure.step('4. Interact with the Minat name input field'):
            await hobby.insert_hobby_name("Ethical Hacking")
            await hobby.clear_hobby_name()

        with allure.step('5. Click on the Save button'):
            await hobby.click_save_form()

        with allure.step('6. Click on the Cancel button'):
            await hobby.click_cancel_form()
