class JobLoc:
    url = "https://staging.karirlab.co/job"

    # Filter section
    btn_easy_apply = "#EasyBtn"
    btn_MSIB = "#msibBtn"
    btn_filters = [btn_easy_apply, btn_MSIB]

    textbox_position = "name=keyword"
    textbox_company = "name=company_industries"
    textbox_location = "name=locations"
    text_boxes = [textbox_position, textbox_company, textbox_location]

    checkbox_full = "xpath=//input[@value='Full-Time']"
    checkbox_part = "xpath=//input[@value='Part-Time']"
    checkbox_intern = "xpath=//input[@value='Internship']"
    checkbox_contract = "xpath=//input[@value='Contract']"
    checkbox_volunteer = "xpath=//input[@value='Volunteer']"
    checkbox_scholar = "xpath=//input[@value='Scholarship']"
    checkbox_partner = "xpath=//input[@value='Partnership']"
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
    body_cards = "xpath=//div[contains(@class, 'jobCard__41hUw')]"
    body_logo = "//img[contains(@class, 'jobCard__image')]"
    body_company_name = "//div[contains(@class, 'jobCard__content')]/span[contains(@class, 'secondary')]"
    body_job_title = "//div[contains(@class, 'jobCard__content')]/h4"
    body_job_location = "//div[contains(@class, 'jobCard__content')]/span[not(contains(@class, 'secondary'))]"
    body_job_description = "//div[contains(@class, 'description')]"
    body_job_industry = "//div[contains(@class, 'description')]/span[1]"
    body_job_type = "//div[contains(@class, 'description')]/span[2]"
    body_job_daycount = "//div[@class='ant-col ant-col-14']"
    body_job_easy_apply = "//div[contains(@class, 'easyApply')]"
    body_cards_containers = [body_logo, body_company_name, body_job_title, body_job_location, body_job_description, body_job_industry, body_job_type, body_job_daycount, body_job_easy_apply]

    # Pagination Section
    page_previous = "xpath=//li[@title='Previous Page']"
    page_next = "xpath=//li[@title='Next Page']"
    page_arrow = [page_next, page_previous]
    page_container = "//li[contains(@class, 'ant-pagination-item')]"
