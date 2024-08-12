class PageInfo:
    url = "https://staging.karirlab.co/job"
    title = "//h3[contains(@class,'job__title')]"
    description = ""


class MainFilter:
    easy_apply = "#EasyBtn"
    msib = "#msibBtn"
    clear = "#bersihkanBtn"
    apply_btn = "#terapkanBtn"


class SearchInput:
    position = "#posInput"
    position_clear = "(//span[contains(@class, 'clear-icon')])[1]"
    position_search = "(//span[@aria-label='search'])[1]"
    company = "#compInput"
    company_clear = "(//span[contains(@class, 'clear-icon')])[2]"
    company_search = "(//span[@role='button'])[2]"
    industry = "[placeholder='Cari Industri']"
    industry_clear = "(//span[contains(@class, 'clear-icon')])[3]"
    industry_search = "(//span[@role='button'])[3]"
    location = "[placeholder='Cari Lokasi']"
    location_clear = "(//span[contains(@class, 'clear-icon')])[4]"
    location_search = "(//span[@role='button'])[4]"
    skill = "[placeholder='Cari Kemampuan']"
    skill_clear = "(//span[contains(@class, 'clear-icon')])[5]"
    skill_search = "(//span[@role='button'])[5]"


class WorkType:
    full = "[value='Full-Time']"
    part = "[value='Part-Time']"
    intern = "[value='Internship']"
    contract = "[value='Contract']"
    volunteer = "[value='Volunteer']"
    scholar = "[value='Scholarship']"
    partner = "[value='Partnership']"


class Arrangement:
    hybrid = "[value='Hybrid']"
    on_site = "[value='On-site']"
    remote = "[value='Remote']"


class Experience:
    zero = "[value='0']"
    one_year = "[value='1']"
    two_years = "[value='2']"
    three_years = "[value='3']"
    four_years = "[value='4']"


class JobSort:
    control = "xpath=(//div[@class='ant-select-selector'])[5]"
    control_expanded = "[class='rc-virtual-list-holder-inner']"
    post_date_asc = "[title='Tanggal Diposting (A to Z)']"
    post_date_desc = "[title='Tanggal Diposting (Z to A)']"
    deadline_asc = "[title='Tanggal Batas Registrasi (A to Z)']"
    deadline_desc = "[title='Tanggal Batas Registrasi (Z to A)']"
    options = {
        "post_asc": post_date_asc,
        "post_desc": post_date_desc,
        "end_asc": deadline_asc,
        "end_desc": deadline_desc
    }


class JobResult:
    cards = "//div[contains(@class,'md-12')]"
    logo = "//img[@alt='company_logo']"
    company = "//div[contains(@class, 'jobCard__content')]/span[contains(@class, 'secondary')]"
    title = "//div[contains(@class, 'jobCard__content')]/h1"
    location = "//div[contains(@class, 'jobCard__content')]/span[not(contains(@class, 'secondary'))]"
    description = "//div[contains(@class, 'description')]"
    industry = "//div[contains(@class, 'description')]/span[1]"
    type = "//div[contains(@class, 'description')]/span[2]"
    daycount = "//div[@class='ant-col ant-col-24']"
    easy_apply = "//span[contains(@class, 'easyApply')]"
    msib = "//div[@class='ant-image']/img[@alt='msib_logo']"


class Pagination:
    previous = "//li[@title='Previous Page']//button[@type='button']"
    next = "//li[@title='Next Page']//button[@type='button']"
    container = "//li[contains(@class, 'ant-pagination-item')]"
