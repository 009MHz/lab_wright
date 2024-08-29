import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.keahlian import Keahlian


@pytest.fixture(scope='function')
async def proficient(user_auth):
    builder = Keahlian(user_auth)
    pre_cond = PreCond(builder.page)
    await pre_cond.load_page()
    return builder


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@allure.feature("Resume Builder/ Keahlian")
@pytest.mark.res_builder
@pytest.mark.keahlian
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @pytest.mark.toggle
    @allure.title("Keahlian Hints Existence")
    @allure.feature("Resume Builder/ Keahlian/ Hints")
    @allure.severity(severity.MINOR)
    async def test_proficient_section_hints(self, proficient):
        with allure.step('1. Click on the Add Keahlian Form button'):
            await proficient.click_add_form()

        with allure.step('2. Validate the Keahlian Hints section after form is added'):
            await proficient.main_hints_presence()
            await proficient.hints_title_presence()
            await proficient.hints_desc_presence()

        with allure.step('3. Interact with Keahlian hint toggle'):
            await proficient.hints_click_hide()
            await proficient.hints_click_show()

    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.accordion
    @pytest.mark.input_field
    @pytest.mark.cancel
    @pytest.mark.save
    @allure.title("Keahlian Section Validation")
    @allure.severity(severity.CRITICAL)
    async def test_proficient_section(self, proficient):
        with allure.step('1. Validate Keahlian default state'):
            await proficient.main_form_presence()
            await proficient.title_presence()
            await proficient.desc_presence()
            await proficient.add_button_presence()
            await proficient.title_click_collapse()
            await proficient.title_click_expand()

        with allure.step('2. Click on the Add Keahlian Form button'):
            await proficient.click_add_form()

        with allure.step('3. Validate each input field completeness'):
            await proficient.name_input_presence()
            await proficient.level_presence()
            await proficient.cancel_form_btn_presence()
            await proficient.save_form_btn_presence()

        with allure.step('4. Insert a valid skill to the Keahlian Input Field'):
            await proficient.name_insert('Adobe')
            await proficient.name_clear_text()

        with allure.step('5. Interact with all Tingkat Keahlian options'):
            await proficient.level_click_pemula()
            await proficient.level_click_menengah()
            await proficient.level_click_lanjut()

        with allure.step('6. Click on the Save button'):
            await proficient.save_form_click()

        with allure.step('7. Click on the Cancel button'):
            await proficient.cancel_form_click()
