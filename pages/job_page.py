from pages.__base import BasePage
from elements.__job import JobLoc
from playwright.async_api import Page, expect


class JobPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def open_page(self):
        await self.page.goto(JobLoc.url)

    """Job List Sorting Control"""

    async def sort_control_presence(self):
        await self._look(JobLoc.JobSort.control)
        await expect(self._find(JobLoc.JobSort.control)).to_be_visible()

    async def sort_control_click(self):
        await self._click(JobLoc.JobSort.control)

    async def sort_item_presence(self):
        for item in JobLoc.JobSort.options:
            await self._look(JobLoc.JobSort.control_expanded)
            await expect(self._find(JobLoc.JobSort.control_expanded)).to_be_visible()

            await self._look(JobLoc.JobSort.options[item])
            await expect(self._find(JobLoc.JobSort.options[item])).to_be_visible()
            await self._click(JobLoc.JobSort.options[item])
            await self.sort_control_click()

    """Job List Main Button Filter"""

    async def click_easy_apply(self):
        await self._click(JobLoc.MainFilter.easy_apply)
        await expect(self._find(JobLoc.MainFilter.easy_apply)).to_be_focused()

    async def click_msib(self):
        await self._click(JobLoc.MainFilter.msib)
        await expect(self._find(JobLoc.MainFilter.msib)).to_be_focused()

    async def click_clear(self):
        await self._click(JobLoc.MainFilter.clear)
        await expect(self._find(JobLoc.MainFilter.clear)).to_be_focused()

    async def click_apply(self):
        await self._click(JobLoc.MainFilter.apply_btn)
        await expect(self._find(JobLoc.MainFilter.apply_btn)).to_be_focused()

    """Job List Carousel"""

    async def _card_component(self, locator, component_name, index):
        locator = f"({locator})[{index}]"
        await self._look(locator)
        await expect(self._find(locator)).to_be_visible(
            timeout=3000), f"{component_name} is not visible for card {index}"

    async def job_cards_logo_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.logo, 'logo', index)

    async def job_cards_company_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.company, 'company', index)

    async def job_cards_title_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.title, 'title', index)

    async def job_cards_location_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.location, 'location', index)

    async def job_cards_description_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.description, 'description', index)

    async def job_cards_industry_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.industry, 'industry', index)

    async def job_cards_type_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.type, 'type', index)

    async def check_job_cards_daycount(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            await self._card_component(JobLoc.JobResult.daycount, 'daycount', index)

    async def job_cards_easyapply_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            if not await self._find(f"({JobLoc.JobResult.easy_apply})[{index}]").is_visible():
                print(f"easyapply button doesn't apply for card {index}")
                continue
            await self._card_component(JobLoc.JobResult.easy_apply, 'easyapply', index)

    async def job_cards_msib_presence(self):
        await self._look(JobLoc.JobResult.cards)
        total_cards = await self._find(JobLoc.JobResult.cards).count()
        for index in range(1, total_cards + 1):
            if not await self._find(f"({JobLoc.JobResult.msib})[{index}]").is_visible():
                print(f"msib button doesn't apply for card {index}")
                continue
            await self._card_component(JobLoc.JobResult.msib, 'msib', index)

    async def position_input_presence(self):
        await self._touch(JobLoc.SearchInput.position)
        await expect(self._find(JobLoc.SearchInput.position)).to_be_visible()

        await self._click(JobLoc.SearchInput.position)
        await expect(self._find(JobLoc.SearchInput.position)).to_be_focused()

    """Filter Input Field Search"""

    async def position_input_type(self, text: str):
        await self._type(JobLoc.SearchInput.position, text)
        await expect(self._find(JobLoc.SearchInput.position)).not_to_be_empty()

    async def position_input_clear(self):
        await self._look(JobLoc.SearchInput.position_clear)
        await self._click(JobLoc.SearchInput.position_clear)
        await expect(self._find(JobLoc.SearchInput.position)).to_be_empty()

    async def company_input_presence(self):
        await self._touch(JobLoc.SearchInput.company)
        await expect(self._find(JobLoc.SearchInput.company)).to_be_visible()

        await self._click(JobLoc.SearchInput.company)
        await expect(self._find(JobLoc.SearchInput.company)).to_be_focused()

    async def company_input_type(self, text: str):
        await self._type(JobLoc.SearchInput.company, text)
        await expect(self._find(JobLoc.SearchInput.company)).not_to_be_empty()

    async def company_input_clear(self):
        await self._look(JobLoc.SearchInput.company_clear)
        await self._click(JobLoc.SearchInput.company_clear)
        await expect(self._find(JobLoc.SearchInput.company)).to_be_empty()

    async def industry_input_presence(self):
        await self._touch(JobLoc.SearchInput.industry)
        await expect(self._find(JobLoc.SearchInput.industry)).to_be_visible()

        await self._click(JobLoc.SearchInput.industry)
        await expect(self._find(JobLoc.SearchInput.industry)).to_be_focused()

    async def industry_input_type(self, text: str):
        await self._type(JobLoc.SearchInput.industry, text)
        await expect(self._find(JobLoc.SearchInput.industry)).not_to_be_empty()

    async def industry_input_clear(self):
        await self._force(JobLoc.SearchInput.industry_clear)
        await self._click(JobLoc.SearchInput.industry_clear)
        await expect(self._find(JobLoc.SearchInput.industry)).to_be_empty()

    async def location_input_presence(self):
        await self._touch(JobLoc.SearchInput.location)
        await expect(self._find(JobLoc.SearchInput.location)).to_be_visible()

        await self._click(JobLoc.SearchInput.location)
        await expect(self._find(JobLoc.SearchInput.location)).to_be_focused()

    async def location_input_type(self, text: str):
        await self._type(JobLoc.SearchInput.location, text)
        await expect(self._find(JobLoc.SearchInput.location)).not_to_be_empty()

    async def location_input_clear(self):
        await self._force(JobLoc.SearchInput.location_clear)
        await self._click(JobLoc.SearchInput.location_clear)
        await expect(self._find(JobLoc.SearchInput.location)).to_be_empty()

    async def skill_input_presence(self):
        await self._touch(JobLoc.SearchInput.skill)
        await expect(self._find(JobLoc.SearchInput.skill)).to_be_visible()

        await self._click(JobLoc.SearchInput.skill)
        await expect(self._find(JobLoc.SearchInput.skill)).to_be_focused()

    async def skill_input_type(self, text: str):
        await self._type(JobLoc.SearchInput.skill, text)
        await expect(self._find(JobLoc.SearchInput.skill)).not_to_be_empty()

    async def skill_input_clear(self):
        await self._force(JobLoc.SearchInput.skill_clear)
        await self._click(JobLoc.SearchInput.skill_clear)
        await expect(self._find(JobLoc.SearchInput.skill)).to_be_empty()

    """Work Type Checkboxes Section"""

    async def full_time_presence(self):
        await self._look(JobLoc.WorkType.full)
        await expect(self._find(JobLoc.WorkType.full)).to_be_visible()

    async def full_time_check(self):
        await self._touch(JobLoc.WorkType.full)
        await self._find(JobLoc.WorkType.full).check()
        await expect(self._find(JobLoc.WorkType.full)).to_be_checked()

    async def full_time_uncheck(self):
        await self._click(JobLoc.WorkType.full)
        await expect(self._find(JobLoc.WorkType.full)).not_to_be_checked()

    async def part_time_presence(self):
        await self._look(JobLoc.WorkType.part)
        await expect(self._find(JobLoc.WorkType.part)).to_be_visible()

    async def part_time_check(self):
        await self._touch(JobLoc.WorkType.part)
        await self._find(JobLoc.WorkType.part).check()
        await expect(self._find(JobLoc.WorkType.part)).to_be_checked()

    async def part_time_uncheck(self):
        await self._click(JobLoc.WorkType.part)
        await expect(self._find(JobLoc.WorkType.part)).not_to_be_checked()

    async def internship_presence(self):
        await self._look(JobLoc.WorkType.intern)
        await expect(self._find(JobLoc.WorkType.intern)).to_be_visible()

    async def internship_check(self):
        await self._touch(JobLoc.WorkType.intern)
        await self._find(JobLoc.WorkType.intern).check()
        await expect(self._find(JobLoc.WorkType.intern)).to_be_checked()

    async def internship_uncheck(self):
        await self._click(JobLoc.WorkType.intern)
        await expect(self._find(JobLoc.WorkType.intern)).not_to_be_checked()

    async def volunteer_presence(self):
        await self._look(JobLoc.WorkType.volunteer)
        await expect(self._find(JobLoc.WorkType.volunteer)).to_be_visible()

    async def volunteer_check(self):
        await self._touch(JobLoc.WorkType.volunteer)
        await self._find(JobLoc.WorkType.volunteer).check()
        await expect(self._find(JobLoc.WorkType.volunteer)).to_be_checked()

    async def volunteer_uncheck(self):
        await self._click(JobLoc.WorkType.volunteer)
        await expect(self._find(JobLoc.WorkType.volunteer)).not_to_be_checked()

    async def contract_presence(self):
        await self._look(JobLoc.WorkType.contract)
        await expect(self._find(JobLoc.WorkType.contract)).to_be_visible()

    async def contract_check(self):
        await self._touch(JobLoc.WorkType.contract)
        await self._find(JobLoc.WorkType.contract).check()
        await expect(self._find(JobLoc.WorkType.contract)).to_be_checked()

    async def contract_uncheck(self):
        await self._click(JobLoc.WorkType.contract)
        await expect(self._find(JobLoc.WorkType.contract)).not_to_be_checked()

    async def scholarship_presence(self):
        await self._look(JobLoc.WorkType.scholar)
        await expect(self._find(JobLoc.WorkType.scholar)).to_be_visible()

    async def scholarship_check(self):
        await self._touch(JobLoc.WorkType.scholar)
        await self._find(JobLoc.WorkType.scholar).check()
        await expect(self._find(JobLoc.WorkType.scholar)).to_be_checked()

    async def scholarship_uncheck(self):
        await self._click(JobLoc.WorkType.scholar)
        await expect(self._find(JobLoc.WorkType.scholar)).not_to_be_checked()

    async def partnership_presence(self):
        await self._look(JobLoc.WorkType.partner)
        await expect(self._find(JobLoc.WorkType.partner)).to_be_visible()

    async def partnership_check(self):
        await self._touch(JobLoc.WorkType.partner)
        await self._find(JobLoc.WorkType.partner).check()
        await expect(self._find(JobLoc.WorkType.partner)).to_be_checked()

    async def partnership_uncheck(self):
        await self._click(JobLoc.WorkType.partner)
        await expect(self._find(JobLoc.WorkType.partner)).not_to_be_checked()

    """Work Arrangement Section"""

    async def hybrid_presence(self):
        await self._look(JobLoc.Arrangement.hybrid)
        await expect(self._find(JobLoc.Arrangement.hybrid)).to_be_visible()

    async def hybrid_check(self):
        await self._touch(JobLoc.Arrangement.hybrid)
        await self._find(JobLoc.Arrangement.hybrid).check()
        await expect(self._find(JobLoc.Arrangement.hybrid)).to_be_checked()

    async def hybrid_uncheck(self):
        await self._click(JobLoc.Arrangement.hybrid)
        await expect(self._find(JobLoc.Arrangement.hybrid)).not_to_be_checked()

    async def on_site_presence(self):
        await self._look(JobLoc.Arrangement.on_site)
        await expect(self._find(JobLoc.Arrangement.on_site)).to_be_visible()

    async def on_site_check(self):
        await self._touch(JobLoc.Arrangement.on_site)
        await self._find(JobLoc.Arrangement.on_site).check()
        await expect(self._find(JobLoc.Arrangement.on_site)).to_be_checked()

    async def on_site_uncheck(self):
        await self._click(JobLoc.Arrangement.on_site)
        await expect(self._find(JobLoc.Arrangement.on_site)).not_to_be_checked()

    async def remote_presence(self):
        await self._look(JobLoc.Arrangement.remote)
        await expect(self._find(JobLoc.Arrangement.remote)).to_be_visible()

    async def remote_check(self):
        await self._touch(JobLoc.Arrangement.remote)
        await self._find(JobLoc.Arrangement.remote).check()
        await expect(self._find(JobLoc.Arrangement.remote)).to_be_checked()

    async def remote_uncheck(self):
        await self._click(JobLoc.Arrangement.remote)
        await expect(self._find(JobLoc.Arrangement.remote)).not_to_be_checked()

    """Job Experience Section"""

    async def no_exp_presence(self):
        await self._look(JobLoc.Experience.zero)
        await expect(self._find(JobLoc.Experience.zero)).to_be_visible()

    async def no_exp_check(self):
        await self._touch(JobLoc.Experience.zero)
        await self._find(JobLoc.Experience.zero).check()
        await expect(self._find(JobLoc.Experience.zero)).to_be_checked()

    async def no_exp_uncheck(self):
        await self._click(JobLoc.Experience.zero)
        await expect(self._find(JobLoc.Experience.zero)).not_to_be_checked()

    async def year_01_presence(self):
        await self._look(JobLoc.Experience.one_year)
        await expect(self._find(JobLoc.Experience.one_year)).to_be_visible()

    async def year_01_check(self):
        await self._touch(JobLoc.Experience.one_year)
        await self._find(JobLoc.Experience.one_year).check()
        await expect(self._find(JobLoc.Experience.one_year)).to_be_checked()

    async def year_01_uncheck(self):
        await self._click(JobLoc.Experience.one_year)
        await expect(self._find(JobLoc.Experience.one_year)).not_to_be_checked()

    async def year_02_presence(self):
        await self._look(JobLoc.Experience.two_years)
        await expect(self._find(JobLoc.Experience.two_years)).to_be_visible()

    async def year_02_check(self):
        await self._touch(JobLoc.Experience.two_years)
        await self._find(JobLoc.Experience.two_years).check()
        await expect(self._find(JobLoc.Experience.two_years)).to_be_checked()

    async def year_02_uncheck(self):
        await self._click(JobLoc.Experience.two_years)
        await expect(self._find(JobLoc.Experience.two_years)).not_to_be_checked()

    async def year_03_presence(self):
        await self._look(JobLoc.Experience.three_years)
        await expect(self._find(JobLoc.Experience.three_years)).to_be_visible()

    async def year_03_check(self):
        await self._touch(JobLoc.Experience.three_years)
        await self._find(JobLoc.Experience.three_years).check()
        await expect(self._find(JobLoc.Experience.three_years)).to_be_checked()

    async def year_03_uncheck(self):
        await self._click(JobLoc.Experience.three_years)
        await expect(self._find(JobLoc.Experience.three_years)).not_to_be_checked()

    async def year_04_presence(self):
        await self._look(JobLoc.Experience.four_years)
        await expect(self._find(JobLoc.Experience.four_years)).to_be_visible()

    async def year_04_check(self):
        await self._touch(JobLoc.Experience.four_years)
        await self._find(JobLoc.Experience.four_years).check()
        await expect(self._find(JobLoc.Experience.four_years)).to_be_checked()

    async def year_04_uncheck(self):
        await self._click(JobLoc.Experience.four_years)
        await expect(self._find(JobLoc.Experience.four_years)).not_to_be_checked()

    """Pagination Section"""

    async def prev_chevron_presence(self):
        await self._look(JobLoc.Pagination.previous)
        await expect(self._find(JobLoc.Pagination.previous)).to_be_visible()

    async def prev_chevron_click(self):
        await self._click(JobLoc.Pagination.previous)
        await expect(self._find(JobLoc.Pagination.previous)).to_be_focused()

    async def next_chevron_presence(self):
        await self._look(JobLoc.Pagination.next)
        await expect(self._find(JobLoc.Pagination.next)).to_be_visible()

    async def next_chevron_click(self):
        await self._click(JobLoc.Pagination.next)
        await expect(self._find(JobLoc.Pagination.next)).to_be_focused()

    async def page_number_count(self):
        print(f"Total Pages: {self._find(JobLoc.Pagination.container).count()}")

    async def page_number_presence(self):
        await self._look(JobLoc.Pagination.container)
        await expect(self._find(JobLoc.Pagination.container)).to_be_visible()
