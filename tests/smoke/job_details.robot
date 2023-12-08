*** Settings ***
Resource        ../../resources/job/detail_job.resource
Resource        ../browser.resource
Task Tags       Job Details
Test Setup      Open Tested Page
Task Teardown   Close Browser

*** Test Cases ***
Validate breadcrumb component
	Wait Until Element Is Enabled    ${nav_back}
	Click Element    ${nav_back}
	Wait Until Location Is Not    ${URL}
	Go Back

Validate company detail section
	Wait Until Element Is Visible    ${comp_deadline_top}
	Wait Until Element Is Visible    ${comp_image}
	Wait Until Element Is Visible    ${comp_job_title}
	Element Text Should Not Be    ${comp_job_title}    ${EMPTY}
	Wait Until Element Is Visible    ${comp_name_small}
	Element Text Should Not Be    ${comp_name_small}    ${EMPTY}
	Wait Until Element Is Visible    ${comp_badge_msib}
	Wait Until Element Is Visible    ${comp_badge_location}
	Element Text Should Not Be    ${comp_badge_location}    ${EMPTY}
	Wait Until Element Is Visible    ${comp_badge_industry}
	Element Text Should Not Be    ${comp_badge_industry}    ${EMPTY}
	Wait Until Element Is Visible    ${comp_badge_type}
	Element Text Should Not Be    ${comp_badge_type}    ${EMPTY}
	Wait Until Element Is Visible    ${comp_deadline_bottom}

Validate job description component
	Wait Until Element Is Visible    ${desc_title}
	Wait Until Element Is Visible    ${desc_tag_wrapper}
	${tags}=    Locators to list    ${desc_tag_index}
	FOR    ${element}    IN    @{tags}
	    Log    ${element}
	    Wait Until Element Is Visible    ${element}
		Element Text Should Not Be    ${element}    ${EMPTY}
	    Wait Until Keyword Succeeds    4s    2    Click Element    ${element}
	    Wait Until Location Is Not    ${URL}
	    Go Back
	END

Validate footer component
    Wait Until Element Is Visible    ${foot_title}
    Wait Until Element Is Visible    ${foot_wrapper}
    Wait Until Element Is Visible    ${foot_company}
	Element Text Should Not Be    ${foot_company}    ${EMPTY}
    Wait Until Element Is Visible    ${foot_location}
	Element Text Should Not Be    ${foot_location}    ${EMPTY}
    Wait Until Element Is Visible    ${foot_industry}
	Element Text Should Not Be    ${foot_industry}    ${EMPTY}
    Wait Until Element Is Visible    ${foot_employee}
	Element Text Should Not Be    ${foot_employee}    ${EMPTY}
    FOR  ${element}  IN  @{foot_url}
        Log    ${element}
        Wait Until Element Is Visible    ${element}
        Wait Until Keyword Succeeds    3    5s    Click Element    ${element}
        Wait Until Location Is Not    ${URL}
        Go Back
    END

Validate job apply component
    Wait Until Element Is Visible    ${apply_wraper}
	Wait Until Element Is Visible    ${apply_title}
	Element Text Should Be    ${apply_title}    Lamar posisi ini?
	Wait Until Element Is Enabled    ${apply_button}
	Element Text Should Be    ${apply_button}    Lamar Posisi
	Click Button    ${apply_button}
	Wait Until Location Is Not    ${URL}
