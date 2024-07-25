class JobLoc:
    url = "https://staging.karirlab.co/job"

    # Filter section
    btn_easy_apply = "#EasyBtn"
    btn_MSIB = "#msibBtn"
    btn_clear = "#bersihkanBtn"
    btn_apply = "#terapkanBtn"

    # Search Input Field
    box_position_input = "#posInput"
    box_position_clear = "(//span[contains(@class, 'clear-icon')])[1]"
    box_position_search = "(//span[@aria-label='search'])[1]"
    box_company_input = "#compInput"
    box_company_clear = "(//span[contains(@class, 'clear-icon')])[2]"
    box_company_search = "(//span[@role='button'])[2]"
    box_industri_input = "[placeholder='Cari Industri']"
    box_industri_clear = "(//span[contains(@class, 'clear-icon')])[3]"
    box_industri_search = "(//span[@role='button'])[3]"
    box_lokasi_input = "[placeholder='Cari Lokasi']"
    box_lokasi_clear = "(//span[contains(@class, 'clear-icon')])[4]"
    box_lokasi_search = "(//span[@role='button'])[4]"
    box_skill_input = "[placeholder='Cari Kemampuan']"
    box_skill_clear = "(//span[contains(@class, 'clear-icon')])[5]"
    box_skill_search = "(//span[@role='button'])[5]"
    
    checkbox_full = "[value='Full-Time']"
    checkbox_part = "[value='Part-Time']"
    checkbox_intern = "[value='Internship']"
    checkbox_contract = "[value='Contract']"
    checkbox_volunteer = "[value='Volunteer']"
    checkbox_scholar = "[value='Scholarship']"
    checkbox_partner = "[value='Partnership']"
    checkboxes = [checkbox_intern, checkbox_partner, checkbox_contract, checkbox_volunteer, checkbox_scholar, checkbox_full, checkbox_part]

    # Sort section
    sort_control = "xpath=(//div[@class='ant-select-selector'])[5]"
    sort_control_expanded = "[class='rc-virtual-list-holder-inner']"
    sorter_date_asc = "[title='Tanggal Diposting (A to Z)']"
    sorter_date_desc = "[title='Tanggal Diposting (Z to A)']"
    sorter_end_asc = "[title='Tanggal Batas Registrasi (A to Z)']"
    sorter_name_desc = "[title='Tanggal Batas Registrasi (Z to A)']"
    sort_options = {
        "post_asc": sorter_date_asc,
        "post_desc": sorter_date_desc,
        "end_asc": sorter_end_asc,
        "end_desc": sorter_name_desc
    }

    # Page Body
    body_cards = "//div[contains(@class,'md-12')]"
    body_logo = "//img[@alt='company_logo']"
    body_company_name = "//div[contains(@class, 'jobCard__content')]/span[contains(@class, 'secondary')]"
    body_job_title = "//div[contains(@class, 'jobCard__content')]/h1"
    body_job_location = "//div[contains(@class, 'jobCard__content')]/span[not(contains(@class, 'secondary'))]"
    body_job_description = "//div[contains(@class, 'description')]"
    body_job_industry = "//div[contains(@class, 'description')]/span[1]"
    body_job_type = "//div[contains(@class, 'description')]/span[2]"
    body_job_daycount = "//div[@class='ant-col ant-col-24']"
    body_job_easy_apply = "//span[contains(@class, 'easyApply')]"
    body_job_msib = "//div[@class='ant-image']/img[@alt='msib_logo']"
    body_cards_containers = [body_logo, body_company_name, body_job_title, body_job_location, body_job_description, body_job_industry, body_job_type, body_job_daycount, body_job_easy_apply]

    # Pagination Section
    page_previous = "xpath=//li[@title='Previous Page']"
    page_next = "xpath=//li[@title='Next Page']"
    page_arrow = [page_next, page_previous]
    page_container = "//li[contains(@class, 'ant-pagination-item')]"
