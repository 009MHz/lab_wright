from pages.__base import BasePage
from elements.__job import *
from playwright.async_api import Page, expect


class JobPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def open_page(self):
        await self.page.goto(PageInfo.url)

    """Job List Sorting Control"""

    async def sort_control_presence(self):
        await self._look(JobSort.control)
        await expect(self._find(JobSort.control)).to_be_visible()

    async def sort_control_click(self):
        await self._click(JobSort.control)

    async def sort_item_presence(self):
        for item in JobSort.options:
            await self._look(JobSort.control_expanded)
            await expect(self._find(JobSort.control_expanded)).to_be_visible()

            await self._look(JobSort.options[item])
            await expect(self._find(JobSort.options[item])).to_be_visible()
            await self._click(JobSort.options[item])
            await self.sort_control_click()

    """Job List Main Button Filter"""

    async def click_easy_apply(self):
        await self._click(MainFilter.easy_apply)
        await expect(self._find(MainFilter.easy_apply)).to_be_focused()

    async def click_msib(self):
        await self._click(MainFilter.msib)
        await expect(self._find(MainFilter.msib)).to_be_focused()

    async def click_clear(self):
        await self._click(MainFilter.clear)
        await expect(self._find(MainFilter.clear)).to_be_focused()

    async def click_apply(self):
        await self._click(MainFilter.apply_btn)
        await expect(self._find(MainFilter.apply_btn)).to_be_focused()

    """Job List Carousel"""

    async def _card_component(self, locator, component_name, index):
        locator = f"({locator})[{index}]"
        await self._look(locator)
        await expect(self._find(locator)).to_be_visible(
            timeout=3000), f"{component_name} is not visible for card {index}"

    async def job_cards_logo_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.logo, 'logo', index)

    async def job_cards_company_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.company, 'company', index)

    async def job_cards_title_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.title, 'title', index)

    async def job_cards_location_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.location, 'location', index)

    async def job_cards_description_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.description, 'description', index)

    async def job_cards_industry_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.industry, 'industry', index)

    async def job_cards_type_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.type, 'type', index)

    async def check_job_cards_daycount(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobResult.daycount, 'daycount', index)

    async def job_cards_easyapply_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            if not await self._find(f"({JobResult.easy_apply})[{index}]").is_visible():
                print(f"easyapply button doesn't apply for card {index}")
                continue
            await self._card_component(JobResult.easy_apply, 'easyapply', index)

    async def job_cards_msib_presence(self):
        await self._look(JobResult.cards)
        total_cards = await self._find(JobResult.cards).count()
        for index in range(1, total_cards + 1):
            if not await self._find(f"({JobResult.msib})[{index}]").is_visible():
                print(f"msib button doesn't apply for card {index}")
                continue
            await self._card_component(JobResult.msib, 'msib', index)

    async def position_input_presence(self):
        await self._touch(SearchInput.position)
        await expect(self._find(SearchInput.position)).to_be_visible()

        await self._click(SearchInput.position)
        await expect(self._find(SearchInput.position)).to_be_focused()

    """Filter Input Field Search"""

    async def position_input_type(self, text: str):
        await self._type(SearchInput.position, text)
        await expect(self._find(SearchInput.position)).not_to_be_empty()

    async def position_input_clear(self):
        await self._look(SearchInput.position_clear)
        await self._click(SearchInput.position_clear)
        await expect(self._find(SearchInput.position)).to_be_empty()

    async def company_input_presence(self):
        await self._touch(SearchInput.company)
        await expect(self._find(SearchInput.company)).to_be_visible()

        await self._click(SearchInput.company)
        await expect(self._find(SearchInput.company)).to_be_focused()

    async def company_input_type(self, text: str):
        await self._type(SearchInput.company, text)
        await expect(self._find(SearchInput.company)).not_to_be_empty()

    async def company_input_clear(self):
        await self._look(SearchInput.company_clear)
        await self._click(SearchInput.company_clear)
        await expect(self._find(SearchInput.company)).to_be_empty()

    async def industry_input_presence(self):
        await self._touch(SearchInput.industry)
        await expect(self._find(SearchInput.industry)).to_be_visible()

        await self._click(SearchInput.industry)
        await expect(self._find(SearchInput.industry)).to_be_focused()

    async def industry_input_type(self, text: str):
        await self._type(SearchInput.industry, text)
        await expect(self._find(SearchInput.industry)).not_to_be_empty()

    async def industry_input_clear(self):
        await self._force(SearchInput.industry_clear)
        await self._click(SearchInput.industry_clear)
        await expect(self._find(SearchInput.industry)).to_be_empty()

    async def location_input_presence(self):
        await self._touch(SearchInput.location)
        await expect(self._find(SearchInput.location)).to_be_visible()

        await self._click(SearchInput.location)
        await expect(self._find(SearchInput.location)).to_be_focused()

    async def location_input_type(self, text: str):
        await self._type(SearchInput.location, text)
        await expect(self._find(SearchInput.location)).not_to_be_empty()

    async def location_input_clear(self):
        await self._force(SearchInput.location_clear)
        await self._click(SearchInput.location_clear)
        await expect(self._find(SearchInput.location)).to_be_empty()

    async def skill_input_presence(self):
        await self._touch(SearchInput.skill)
        await expect(self._find(SearchInput.skill)).to_be_visible()

        await self._click(SearchInput.skill)
        await expect(self._find(SearchInput.skill)).to_be_focused()

    async def skill_input_type(self, text: str):
        await self._type(SearchInput.skill, text)
        await expect(self._find(SearchInput.skill)).not_to_be_empty()

    async def skill_input_clear(self):
        await self._force(SearchInput.skill_clear)
        await self._click(SearchInput.skill_clear)
        await expect(self._find(SearchInput.skill)).to_be_empty()

    """Work Type Checkboxes Section"""

    async def full_time_presence(self):
        await self._look(WorkType.full)
        await expect(self._find(WorkType.full)).to_be_visible()

    async def full_time_check(self):
        await self._touch(WorkType.full)
        await self._find(WorkType.full).check()
        await expect(self._find(WorkType.full)).to_be_checked()

    async def full_time_uncheck(self):
        await self._click(WorkType.full)
        await expect(self._find(WorkType.full)).not_to_be_checked()

    async def part_time_presence(self):
        await self._look(WorkType.part)
        await expect(self._find(WorkType.part)).to_be_visible()

    async def part_time_check(self):
        await self._touch(WorkType.part)
        await self._find(WorkType.part).check()
        await expect(self._find(WorkType.part)).to_be_checked()

    async def part_time_uncheck(self):
        await self._click(WorkType.part)
        await expect(self._find(WorkType.part)).not_to_be_checked()

    async def internship_presence(self):
        await self._look(WorkType.intern)
        await expect(self._find(WorkType.intern)).to_be_visible()

    async def internship_check(self):
        await self._touch(WorkType.intern)
        await self._find(WorkType.intern).check()
        await expect(self._find(WorkType.intern)).to_be_checked()

    async def internship_uncheck(self):
        await self._click(WorkType.intern)
        await expect(self._find(WorkType.intern)).not_to_be_checked()

    async def volunteer_presence(self):
        await self._look(WorkType.volunteer)
        await expect(self._find(WorkType.volunteer)).to_be_visible()

    async def volunteer_check(self):
        await self._touch(WorkType.volunteer)
        await self._find(WorkType.volunteer).check()
        await expect(self._find(WorkType.volunteer)).to_be_checked()

    async def volunteer_uncheck(self):
        await self._click(WorkType.volunteer)
        await expect(self._find(WorkType.volunteer)).not_to_be_checked()

    async def contract_presence(self):
        await self._look(WorkType.contract)
        await expect(self._find(WorkType.contract)).to_be_visible()

    async def contract_check(self):
        await self._touch(WorkType.contract)
        await self._find(WorkType.contract).check()
        await expect(self._find(WorkType.contract)).to_be_checked()

    async def contract_uncheck(self):
        await self._click(WorkType.contract)
        await expect(self._find(WorkType.contract)).not_to_be_checked()

    async def scholarship_presence(self):
        await self._look(WorkType.scholar)
        await expect(self._find(WorkType.scholar)).to_be_visible()

    async def scholarship_check(self):
        await self._touch(WorkType.scholar)
        await self._find(WorkType.scholar).check()
        await expect(self._find(WorkType.scholar)).to_be_checked()

    async def scholarship_uncheck(self):
        await self._click(WorkType.scholar)
        await expect(self._find(WorkType.scholar)).not_to_be_checked()

    async def partnership_presence(self):
        await self._look(WorkType.partner)
        await expect(self._find(WorkType.partner)).to_be_visible()

    async def partnership_check(self):
        await self._touch(WorkType.partner)
        await self._find(WorkType.partner).check()
        await expect(self._find(WorkType.partner)).to_be_checked()

    async def partnership_uncheck(self):
        await self._click(WorkType.partner)
        await expect(self._find(WorkType.partner)).not_to_be_checked()

    """Work Arrangement Section"""

    async def hybrid_presence(self):
        await self._look(Arrangement.hybrid)
        await expect(self._find(Arrangement.hybrid)).to_be_visible()

    async def hybrid_check(self):
        await self._touch(Arrangement.hybrid)
        await self._find(Arrangement.hybrid).check()
        await expect(self._find(Arrangement.hybrid)).to_be_checked()

    async def hybrid_uncheck(self):
        await self._click(Arrangement.hybrid)
        await expect(self._find(Arrangement.hybrid)).not_to_be_checked()

    async def on_site_presence(self):
        await self._look(Arrangement.on_site)
        await expect(self._find(Arrangement.on_site)).to_be_visible()

    async def on_site_check(self):
        await self._touch(Arrangement.on_site)
        await self._find(Arrangement.on_site).check()
        await expect(self._find(Arrangement.on_site)).to_be_checked()

    async def on_site_uncheck(self):
        await self._click(Arrangement.on_site)
        await expect(self._find(Arrangement.on_site)).not_to_be_checked()

    async def remote_presence(self):
        await self._look(Arrangement.remote)
        await expect(self._find(Arrangement.remote)).to_be_visible()

    async def remote_check(self):
        await self._touch(Arrangement.remote)
        await self._find(Arrangement.remote).check()
        await expect(self._find(Arrangement.remote)).to_be_checked()

    async def remote_uncheck(self):
        await self._click(Arrangement.remote)
        await expect(self._find(Arrangement.remote)).not_to_be_checked()

    """Job Experience Section"""

    async def no_exp_presence(self):
        await self._look(Experience.zero)
        await expect(self._find(Experience.zero)).to_be_visible()

    async def no_exp_check(self):
        await self._touch(Experience.zero)
        await self._find(Experience.zero).check()
        await expect(self._find(Experience.zero)).to_be_checked()

    async def no_exp_uncheck(self):
        await self._click(Experience.zero)
        await expect(self._find(Experience.zero)).not_to_be_checked()

    async def year_01_presence(self):
        await self._look(Experience.one_year)
        await expect(self._find(Experience.one_year)).to_be_visible()

    async def year_01_check(self):
        await self._touch(Experience.one_year)
        await self._find(Experience.one_year).check()
        await expect(self._find(Experience.one_year)).to_be_checked()

    async def year_01_uncheck(self):
        await self._click(Experience.one_year)
        await expect(self._find(Experience.one_year)).not_to_be_checked()

    async def year_02_presence(self):
        await self._look(Experience.two_years)
        await expect(self._find(Experience.two_years)).to_be_visible()

    async def year_02_check(self):
        await self._touch(Experience.two_years)
        await self._find(Experience.two_years).check()
        await expect(self._find(Experience.two_years)).to_be_checked()

    async def year_02_uncheck(self):
        await self._click(Experience.two_years)
        await expect(self._find(Experience.two_years)).not_to_be_checked()

    async def year_03_presence(self):
        await self._look(Experience.three_years)
        await expect(self._find(Experience.three_years)).to_be_visible()

    async def year_03_check(self):
        await self._touch(Experience.three_years)
        await self._find(Experience.three_years).check()
        await expect(self._find(Experience.three_years)).to_be_checked()

    async def year_03_uncheck(self):
        await self._click(Experience.three_years)
        await expect(self._find(Experience.three_years)).not_to_be_checked()

    async def year_04_presence(self):
        await self._look(Experience.four_years)
        await expect(self._find(Experience.four_years)).to_be_visible()

    async def year_04_check(self):
        await self._touch(Experience.four_years)
        await self._find(Experience.four_years).check()
        await expect(self._find(Experience.four_years)).to_be_checked()

    async def year_04_uncheck(self):
        await self._click(Experience.four_years)
        await expect(self._find(Experience.four_years)).not_to_be_checked()

    """Pagination Section"""

    async def prev_chevron_presence(self):
        await self._look(Pagination.previous)
        await expect(self._find(Pagination.previous)).to_be_visible()

    async def prev_chevron_click(self):
        await self._click(Pagination.previous)
        await expect(self._find(Pagination.previous)).to_be_focused()

    async def next_chevron_presence(self):
        await self._look(Pagination.next)
        await expect(self._find(Pagination.next)).to_be_visible()

    async def next_chevron_click(self):
        await self._click(Pagination.next)
        await expect(self._find(Pagination.next)).to_be_focused()

    async def page_number_count(self):
        print(f"Total Pages: {self._find(Pagination.container).count()}")

    async def page_number_presence(self):
        await self._look(Pagination.container)
        await expect(self._find(Pagination.container)).to_be_visible()
