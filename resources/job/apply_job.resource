*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections
Library     OperatingSystem
Resource    ../persona/admin/variable_admin.resource
Resource    ../../tests/browser.resource

*** Variables ***
${URL_screening}            https://staging.karirlab.co/job/automation-msib-test-status-badges--karirlab/applicant
${URL_no_screening}         https://staging.karirlab.co/job/automation-test-apply-job-with-no-screening--karirlab/applicant
${data_path}                ${CURDIR}${/}..${/}..${/}resources${/}data${/}file_upload/

# Header Components
${nav_back}                 xpath://a[contains(@class, 'BackNavigation')]
${page_title}               xpath://h3[@class='ant-typography']

# Resume Section
${res_title}                css:label[title='Pilih Resume']
${res_description}          xpath:(//span[contains(@class, 'typography')])[1]
${res_field}                xpath://div[contains(@name, 'resume_id')]
${res_field_expand}         class:rc-virtual-list-holder-inner
${res_field_content}        //div[@class='ant-select-item-option-content']
${res_create}               xpath://span[contains(@class, 'Resume__link')]

# Job Cards Default State Component
${card_image}               xpath://img[@alt='Company thumbnail']
${card_top_deadline}        xpath:(//span[contains(@class, 'deadline')])[1]
${card_easy_apply}          xpath://span[contains(@class, 'easyApply')]
${card_title}               xpath:(//h4[@class='ant-typography'])[1]
${card_badge_index}         (//span[contains(@class, 'chip')])
${card_badge_msib}          xpath://div[contains(@class,'jobDetail__chip')]
${card_badge_location}      xpath:(//span[contains(@class, 'chip')])[1]
${card_badge_industry}      xpath:(//span[contains(@class, 'chip')])[2]
${card_badge_type}          xpath:(//span[contains(@class, 'chip')])[3]
${card_arrow_expand}        xpath://div[contains(text(),'Lihat Lebih Banyak')]
@{card_default_visual}      ${card_image}   ${card_top_deadline}    ${card_easy_apply}  ${card_title}   ${card_badge_msib}  ${card_badge_location}  ${card_badge_industry}  ${card_badge_type}  ${card_arrow_expand}
@{card_default_text}        ${card_top_deadline}    ${card_easy_apply}  ${card_title}   ${card_badge_location}  ${card_badge_industry}  ${card_badge_type}  ${card_arrow_expand}

# Job Cards Expanded State Component
${card_bot_deadline}        xpath:(//span[contains(@class, 'deadline')])[2]
${card_description_title}   xpath:(//h4[@class='ant-typography'])[2]
${card_tag_wrapper}         xpath://div[contains(@class,'horizontal')])[3]
${card_tag_index}           //a[contains(@href, '/job?tags')]
${card_arrow_collapse}      xpath://div[contains(@class, 'item') and text()='Lihat Lebih Sedikit']
@{card_expand_component}    ${card_bot_deadline}    ${card_description_title}   ${card_arrow_collapse}

# Screening Question
${scr_title}                xpath://h5[@class='ant-typography']
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
${apply_btn}                //button[contains(., 'Lamar Sekarang')]


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

Screening Questions Checker
	${status}=  Run Keyword And Return Status       Wait Until Page Contains Element    ${scr_wrapper}
	[Return]                            ${status}

Inject file
    [Arguments]                         ${locator}                  ${file_name}
    [Documentation]     Requires a valid name with the supported file types(test.csv, test.xlsx, test.doc, test.pdf, test.png, test.jpeg)
    ${complete_file_path}=   Join Path       ${data_path}${file_name}
    Choose File                         ${locator}                  ${complete_file_path}
