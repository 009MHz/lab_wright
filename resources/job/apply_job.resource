*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections
Resource    ../persona/admin/variable_admin.resource
Resource    ../../tests/browser.resource

*** Variables ***
# Pre-requisite
${URL_screening}            https://staging.karirlab.co/job/automation-msib-test-status-badges--karirlab/applicant
${URL_no_screening}         https://staging.karirlab.co/job/automation-test-apply-job-with-no-screening--karirlab/applicant
# Header Components
${nav_back}                 class:BackNavigation_breadcrumbs__FZwHF
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
${card_badge_msib}          class:JobDetail_jobDetail__chip__v7Ytc
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
${scr_wrapper}              //div[contains(@class, 'screeningQuestion__lGS3L')]
${scr_index}                //div[contains(@class, 'InternalContainer')]
${scr_pharagraph}           //textarea[@type='text']
${scr_choices}          //label[contains(@class, 'ant-radio')]
${scr_checkbox}          //span[@class='ant-checkbox']
${scr_upload}          //span[contains(@class, 'upload-btn')]


*** Keywords ***
Locators to list
	[Arguments]             ${identical_locator}
	${total_element}=       Get Element Count       xpath:${identical_locator}
	${collected_elements}=  Create List
	FOR    ${counter}    IN RANGE    ${total_element}
		${current_locator}=     Convert To String   xpath:(${identical_locator})[${counter+1}]
		Append To List      ${collected_elements}   ${current_locator}
	END
	[Return]                ${collected_elements}

Scroll down to the bottom page
    Execute JavaScript      window.scrollTo(0, document.body.scrollHeight)

Screening question check
	Run Keyword And Return Status    Wait Until Page Contains Element    ${scr_wrapper}

Validate screening question wrapper
	${status}=  Run Keyword And Return Status    Screening question check
	IF    ${status}==True
	    Wait Until Page Contains Element    ${scr_title}
	    Element Text Should Be    ${scr_title}    Pertanyaan Seleksi Awal
	    ${scr_question_elements}=   Locators to list    ${scr_index}
	    FOR    ${element}    IN    @{scr_question_elements}
	        Wait Until Element Is Visible    ${element}
		END
	ELSE
	    Element Should Not Be Visible    ${scr_index}
	END

Validate screening questions multiple choice
	${status}=  Run Keyword And Return Status    Screening question check
	IF    ${status}==True
	    ${elements_radio}=   Locators to list    ${scr_choices}
	    FOR    ${element}    IN    @{elements_radio}
	        Wait Until Element Is Enabled    ${element}
	        Element Text Should Not Be    ${element}    ${EMPTY}
	        Wait Until Keyword Succeeds    3x    1s    Click Element    ${element}
		END
	ELSE
	    Element Should Not Be Visible    ${scr_index}
	END

# TODO 2: screening questions checkboxes
Validate screening questions checkboxes
	Pass Execution    For Now just to store the keywords

# TODO 3: screening questions pharagraph
Validate screening questions pharagraph
	Pass Execution    For Now just to store the keywords

# TODO 4: screening questions upload file
Validate screening questions upload file
	Pass Execution    For Now just to store the keywords