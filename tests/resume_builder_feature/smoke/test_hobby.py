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
@allure.feature("Resume Builder/ Minat")
@pytest.mark.res_builder
@pytest.mark.minat
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @allure.title("Minat Hints Existence")
    @allure.feature("Resume Builder/ Minat/ Hints")
    @allure.severity(severity.MINOR)
    async def test_minat_section_hints(self, builder):
        with allure.step('1. Click on the Add Minat Form button'):
            await builder.hobby_click_add_form()

        with allure.step('2. Validate the Minat Hints section after form is added'):
            await builder.hobby_main_hints_presence()
            await builder.hobby_hints_title_presence()
            await builder.hobby_hints_desc_presence()

        with allure.step('3. Interact with Minat hint toggle'):
            await builder.hobby_hints_click_hide()
            await builder.hobby_hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Minat Section Validation")
    @allure.severity(severity.CRITICAL)
    async def test_minat_section(self, builder):
        with allure.step('1. Validate Minat form default state'):
            await builder.hobby_main_form_presence()
            await builder.hobby_title_presence()
            await builder.hobby_desc_presence()
            await builder.hobby_add_button_presence()
            await builder.hobby_title_click_collapse()
            await builder.hobby_title_click_expand()

        with allure.step('2. Click on the Add Minat Form button'):
            await builder.hobby_click_add_form()

        with allure.step('3. Validate each input field completeness'):
            await builder.hobby_name_input_presence()
            await builder.hobby_cancel_form_btn_presence()
            await builder.hobby_save_form_btn_presence()

        with allure.step('4. Interact with the Minat name input field'):
            await builder.hobby_name_insert("Ethical Hacking")
            await builder.hobby_name_clear()

        with allure.step('5. Click on the Save button'):
            await builder.hobby_save_form_click()

        with allure.step('6. Click on the Cancel button'):
            await builder.hobby_cancel_form_click()
