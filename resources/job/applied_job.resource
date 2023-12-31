*** Settings ***
Library     SeleniumLibrary
Library     Collections
Resource    ../../tests/browser.resource

*** Variables ***
${URL_applied_job}          https://staging.karirlab.co/job/automation-msib-test-status-badges--karirlab/applicant
${data_path}                ${CURDIR}${/}..${/}..${/}resources${/}data${/}file_upload/

# Header
${header_breadcrumb}        //a[contains(@class, 'breadcrumbs')]
${header_title}             //h3[contains(., 'Lamar')]
${header_checkmark}         //span[contains(@class, 'check-circle')]
${header_status}            //h5[contains(@class, 'submitted')]
@{header_visuals}           ${header_breadcrumb}    ${header_title}     ${header_checkmark}     ${header_status}

#Less than 60 minutes
${pending_countdown}        //div[contains(@class, 'Heading')]//strong

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

# Screening Question
${scr_title}                //h5[@class='ant-typography']
${scr_wrapper}              //div[contains(@class, 'screeningQuestion')]
${scr_index}                //div[contains(@class, 'InternalContainer')]
${scr_pharagraph}           //textarea[@type='text']
${scr_choices}              //label[contains(@class, 'radio')]
${scr_checkbox}             //label[contains(@class, 'checkbox')]
${scr_upload_wrapper}       //span[contains(@class,'upload')]
${scr_upload_doc}           //input[@accept='.pdf,.doc']
${scr_upload_data_file}     //input[@accept='.xlsx,.csv']
${scr_upload_image}         //input[@accept='.jpg,.jpeg,.png']

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

Screening Questions Checker
	${status}=  Run Keyword And Return Status       Wait Until Page Contains Element    ${scr_wrapper}
	[Return]                            ${status}

Inject file
    [Arguments]                         ${locator}                  ${file_name}
    [Documentation]     Requires a valid name with the supported file types(test.csv, test.xlsx, test.doc, test.pdf, test.png, test.jpeg)
    ${complete_file_path}=              Join Path                   ${data_path}${file_name}
    Choose File                         ${locator}                  ${complete_file_path}

Scroll down into element
    [Arguments]             ${locator}
	${y_pos}=               Get Vertical Position        ${locator}
	Execute Javascript      window.scrollTo(0, ${y_pos})
