*** Settings ***
Resource        ../../resources/job/applied_job.resource
Suite Setup     Login as job applicant    staging       login      headless=True
Task Setup      Go To    ${URL_applied_job}
Suite Teardown  Close Browser

*** Test Cases ***
Applied job > 60 minutes state: Validate header component
    FOR    ${element}    IN    @{header_visuals}
        Wait Until Element Is Visible                           ${element}
    END
    Element Text Should Be          ${header_title}             Lamar Pekerjaan
    Element Should Contain          ${header_status}            Lamaran kamu telah berhasil terkirim ke
    Element Text Should Be          ${header_breadcrumb}        Back to Job List
    Click Element    ${header_breadcrumb}
    Wait Until Location Is Not              ${URL_applied_job}

Applied job > 60 minutes state: Employers profile component
    FOR    ${element}    IN    @{emp_visuals}
        Wait Until Element Is Visible       ${element}
    END
    Element Text Should Be          ${emp_job_state}            Applied
    Element Text Should Not Be      ${emp_job_title}            ${EMPTY}
    Element Text Should Not Be      ${emp_used_resume}          ${EMPTY}
    Element Should Contain          ${emp_apply_day_count}      hari yang lalu

Applied job > 60 minutes state: Job cards component default state
	FOR    ${element}    IN    @{card_default_visuals}
	    Wait Until Element Is Visible       ${element}
	END
	Element Should Contain          ${card_deadline_top}        Batas Pendaftaran
	Element Text Should Be          ${card_easy_apply}          Easy Apply
	Element Text Should Not Be      ${card_title}               ${EMPTY}
	Element Text Should Not Be      ${card_badge_location}      ${EMPTY}
	Element Text Should Not Be      ${card_badge_industry}      ${EMPTY}
	Element Text Should Not Be      ${card_badge_type}          ${EMPTY}
	Wait Until Element Is Enabled   ${card_arrow_expand}
	Wait Until Keyword Succeeds    2x    5s    Click Element    ${card_arrow_expand}

Applied job > 60 minutes state: Job cards component expanded state
	Wait Until Element Is Enabled    ${card_arrow_expand}
	Wait Until Keyword Succeeds    2x    5s    Click Element    ${card_arrow_expand}
	FOR    ${element}    IN    @{card_expanded_visuals}
	    Wait Until Element Is Visible       ${element}
	END
	Element Should Contain          ${card_bot_deadline}        Diunggah
	Element Text Should Be          ${card_description_title}   Deskripsi Pekerjaan
	Wait Until Keyword Succeeds     2x  3s      Click Element   ${card_arrow_collapse}


Applied job > 60 minutes state: Job cards component expanded state - tags
	${tag_elements}=    Locators to list        ${card_tag_index}
	Click Element        ${card_arrow_expand}
	FOR    ${element}    IN                     @{tag_elements}
	    Scroll down to the bottom page
	    Wait Until Element Is Visible   ${element}
	    Element Text Should Not Be      ${element}              ${EMPTY}
	    Wait Until Keyword Succeeds     2x  3s      Click Element       ${element}
	    Wait Until Location Is Not      ${URL_applied_job}
	    Go Back
	    Wait Until Keyword Succeeds    2x    3s    Click Element        ${card_arrow_expand}
	END
	Scroll down to the bottom page
	Wait Until Keyword Succeeds    2x    3s    Click Element        ${card_arrow_collapse}

Applied job > 60 minutes state: Apply button
	Wait Until Element Is Visible       ${apply_button}
	Element Should Contain              ${apply_button}         Lamar Sekarang
	Element Should Be Disabled          ${apply_button}