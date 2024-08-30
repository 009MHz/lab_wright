import pytest
import allure
from allure import severity_level as severity
from pages.resume_builder import PreCond
from pages.resume_builder.data_diri import PersonalInformation


@pytest.fixture(scope='function')
async def data_diri(user_auth):
    data_diri = PersonalInformation(user_auth)
    pre_cond = PreCond(data_diri.page)
    await pre_cond.load_page()
    return data_diri


@allure.epic("Resume Builder")
@allure.story("Smoke Testing: Resume Builder")
@allure.feature("Resume Builder/ Data Diri, Resume Builder/ Preview")
@pytest.mark.res_builder
@pytest.mark.data_diri
@pytest.mark.skip
class TestSmokeResumeBuilderPage:
    @pytest.mark.positive
    @pytest.mark.smoke
    @pytest.mark.hints
    @pytest.mark.toggle
    @allure.feature("Resume Builder/ Data Diri/ Preview")
    @allure.title("The Data Diri preview should be matched with the input")
    @allure.severity(severity.NORMAL)
    async def test_data_diri_preview(self, data_diri):
        with allure.step('1. Insert the necessary data on the Data Diri input field'):
            pass
            # await data_diri.hints_desc_presence()
            # await data_diri.hints_toggle_presence()

        with allure.step('2. Click on the Simpan button'):
            pass

        with allure.step('3. Data Diri Initial state should be hidden '):
            pass

        with allure.step('4. Verify that the Data Diri Input Field should be hidden '):
            pass

        with allure.step('5. Verify that the Edit input action should be displayed'):
            pass

        with allure.step('6. Verify that the Data Diri preview matched with saved input'):
            pass
