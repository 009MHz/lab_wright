*** Settings ***
Library     SeleniumLibrary
Library     Collections
Resource    ../../tests/browser.resource

*** Variables ***
${URL_applied_job}          https://staging.karirlab.co/job/automation-msib-test-status-badges--karirlab/applicant

# More than 60 minutes state
# Header
${header_breadcrumb}        //a[contains(@class, 'breadcrumbs')]
${header_title}             //h3[contains(., 'Lamar')]
${header_status}            //h5[contains(@class, 'submitted')]
@{header_visuals}           ${header_breadcrumb}    ${header_title}     ${header_status}

# Employers Profile
${emp_logo}                 //img[@alt='company logo']
${emp_job_state}            //div[contains(@class, 'StatusLabel')]
${emp_job_title}            //h5[contains(@class, 'jobTitle')]
${emp_used_resume}          (//div[contains(@class, 'JobCard')]//div[contains(@class,'horizontal')])[2]
${emp_apply_day_count}      (//div[contains(@class, 'JobCard')]//div[contains(@class,'horizontal')])[3]
@{emp_visuals}              ${emp_logo}     ${emp_job_state}    ${emp_job_title}    ${emp_used_resume}  ${emp_apply_day_count}

# Job card Default State
${card_deadline_top}         (//span[contains(@class, 'deadline')])[1]
${card_company_logo}         //img[@alt='Company thumbnail']
${card_easy_apply}           //span[contains(@class, 'easyApply')]
${card_title}                (//h4[@class='ant-typography'])[1]
${card_badge_index}          (//span[contains(@class, 'chip')])
${card_badge_msib}           //div[contains(@class, 'chip')]
${card_badge_location}       (//span[contains(@class, 'chip')])[1]
${card_badge_industry}       (//span[contains(@class, 'chip')])[2]
${card_badge_type}           (//span[contains(@class, 'chip')])[3]
${card_arrow_expand}         //div[contains(text(),'Lihat Lebih Banyak')]
@{card_default_visuals}     ${card_deadline_top}    ${card_company_logo}    ${card_easy_apply}  ${card_title}   ${card_badge_msib}  ${card_badge_location}  ${card_badge_industry}  ${card_badge_type}

# Job card Expanded State
${card_bot_deadline}        (//span[contains(@class, 'deadline')])[2]
${card_description_title}   (//h4[@class='ant-typography'])[2]
${card_tag_wrapper}         //div[contains(@class,'horizontal')])[3]
${card_tag_index}           //a[contains(@href, '/job?tags')]
${card_arrow_collapse}      xpath://div[contains(@class, 'item') and text()='Lihat Lebih Sedikit']
@{card_expanded_visuals}    ${card_bot_deadline}    ${card_description_title}   ${card_arrow_collapse}

# Apply Button
${apply_button}             //button[@type='submit']

*** Keywords ***
Locators to list
	[Arguments]                         ${identical_locator}
	${total_element}=                   Get Element Count           xpath:${identical_locator}
	${collected_elements}=              Create List
	FOR    ${counter}    IN RANGE       ${total_element}
		${current_locator}=             Convert To String           xpath:(${identical_locator})[${counter+1}]
		Append To List                  ${collected_elements}       ${current_locator}
	END
	[Return]    ${collected_elements}

Scroll down to the bottom page
    Execute JavaScript                  window.scrollTo(0, document.body.scrollHeight)