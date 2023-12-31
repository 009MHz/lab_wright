*** Settings ***
Resource        ../../resources/job/applied_job.resource
Suite Setup     Login with specific role    job_applicant    staging       login      headless=False
Task Setup      Go To    ${URL_applied_job}
Suite Teardown  Close Browser

*** Test Cases ***
Validate Applied Job: header component
	FOR    ${element}    IN    @{header_visuals}
        Wait Until Element Is Visible                           ${element}
    END
    Element Text Should Be              ${header_title}             Lamar Pekerjaan
    Element Should Contain              ${header_status}            Lamaran kamu telah berhasil terkirim ke
    Element Text Should Be              ${header_breadcrumb}        Back to Job List
	${edit_mode}    Run Keyword And Return Status    Wait Until Page Contains Element    ${pending_countdown}
	IF    '${edit_mode}' == True
	    Element Should Contain          ${pending_countdown}        Kamu masih bisa mengubah lamaranmu dalam waktu
	END
	Wait Until Keyword Succeeds    2x    4s    Click Element        ${header_breadcrumb}
    Wait Until Location Is Not          ${URL_applied_job}

Validate Applied Job: employers profile component
    FOR    ${element}    IN    @{emp_visuals}
        Wait Until Element Is Visible       ${element}
    END
    Element Text Should Be              ${emp_job_state}            Applied
    Element Text Should Not Be          ${emp_job_title}            ${EMPTY}
    Element Text Should Not Be          ${emp_used_resume}          ${EMPTY}
    Element Should Contain              ${emp_apply_day_count}      yang lalu

Validate Applied Job: job cards/default state
	FOR    ${element}    IN    @{card_default_visuals}
	    Wait Until Element Is Visible       ${element}
	END
	Element Should Contain              ${card_deadline_top}        Batas Pendaftaran
	Element Text Should Be              ${card_easy_apply}          Easy Apply
	Element Text Should Not Be          ${card_title}               ${EMPTY}
	Element Text Should Not Be          ${card_badge_location}      ${EMPTY}
	Element Text Should Not Be          ${card_badge_industry}      ${EMPTY}
	Element Text Should Not Be          ${card_badge_type}          ${EMPTY}
	Wait Until Element Is Enabled       ${card_arrow_expand}
	Wait Until Keyword Succeeds    2x    5s    Click Element        ${card_arrow_expand}

Validate Applied Job: job cards/expanded state
    Click Element    ${card_arrow_expand}	
	FOR    ${element}    IN    @{card_expanded_visuals}
	    Scroll down into element            ${element}
	    Wait Until Element Is Visible       ${element}
	END
	Element Should Contain              ${card_bot_deadline}        Diunggah
	Element Text Should Be              ${card_description_title}   Deskripsi Pekerjaan
	Wait Until Keyword Succeeds     2x  3s      Click Element       ${card_arrow_collapse}


Validate Applied Job: job cards/expanded state/tags
	${tag_elements}=    Locators to list        ${card_tag_index}
	Click Element        ${card_arrow_expand}
	FOR    ${element}    IN                     @{tag_elements}
	    Scroll down into element        ${element}
	    Wait Until Element Is Visible   ${element}
	    Element Text Should Not Be      ${element}                  ${EMPTY}
	    Wait Until Keyword Succeeds     2x	    4s      Click Element       ${element}
	    Wait Until Location Is Not      ${URL_applied_job}
	    Go Back
	    Wait Until Keyword Succeeds    2x    4s    Click Element    ${card_arrow_expand}
	END
	Scroll down into element        ${card_arrow_collapse}
	Wait Until Keyword Succeeds    2x    3s    Click Element        ${card_arrow_collapse}

Validate Applied Job: Apply button
	Wait Until Element Is Visible       ${apply_button}
	Scroll down into element            ${apply_button}
	Element Text Should Be              ${apply_button}             Lamar Sekarang
	Element Should Be Disabled          ${apply_button}
