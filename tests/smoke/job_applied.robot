*** Settings ***
Resource        ../../resources/job/applied_job.resource
Suite Setup     Login with specific role    job_applicant    staging       login      headless=False
Task Setup      Go To    ${URL_applied_job}
Suite Teardown  Close Browser

*** Test Cases ***
Validate Applied Job: header component
	FOR    ${element}    IN    @{header_visuals}
        Wait Until Element Is Visible                                   ${element}
    END
    Element Text Should Be              ${header_title}                 Lamar Pekerjaan
    Element Should Contain              ${header_status}                Lamaran kamu telah berhasil terkirim ke
    Element Text Should Be              ${header_breadcrumb}            Back to Job List
	${edit_mode}    Edit mode checker
	Run Keyword If    ${edit_mode} == True    Element Should Contain    ${pending_countdown}    Kamu masih bisa mengubah lamaranmu dalam waktu
	Wait Until Keyword Succeeds    2x    4s    Click Element            ${header_breadcrumb}
    Wait Until Location Is Not          ${URL_applied_job}

Validate Applied Job: employers profile component
    ${edit_mode}    Edit mode checker
    IF    ${edit_mode} == True
        FOR    ${element}    IN    @{emp_visuals}
            Element Should Not Be Visible    ${element}
        END
        Pass Execution    Employers profile will not displayed when edit mode is ON
    ELSE
        FOR    ${element}    IN    @{emp_visuals}
            Wait Until Element Is Visible       ${element}
        END
	    Element Text Should Be              ${emp_job_state}            Applied
	    Element Text Should Not Be          ${emp_job_title}            ${EMPTY}
	    Element Text Should Not Be          ${emp_used_resume}          ${EMPTY}
	    Element Should Contain              ${emp_apply_day_count}      yang lalu
    END

Validate Applied Job: job cards/default state
	FOR    ${element}    IN    @{card_default_visuals}
	    Wait Until Element Is Visible       ${element}
	END
	Element Should Contain                  ${card_deadline_top}        Batas Pendaftaran
	Element Text Should Be                  ${card_easy_apply}          Easy Apply
	Element Text Should Not Be              ${card_title}               ${EMPTY}
	Element Text Should Not Be              ${card_badge_location}      ${EMPTY}
	Element Text Should Not Be              ${card_badge_industry}      ${EMPTY}
	Element Text Should Not Be              ${card_badge_type}          ${EMPTY}
	Wait Until Element Is Enabled           ${card_arrow_expand}
	Wait Until Keyword Succeeds    2x    5s    Click Element            ${card_arrow_expand}

Validate Applied Job: job cards/expanded state
    Click Element    ${card_arrow_expand}
    Element Should Contain                  ${card_bot_deadline}        Diunggah
	Element Should Contain                  ${card_bot_deadline}        yang lalu
	Element Text Should Be                  ${card_description_title}   Deskripsi Pekerjaan
	Element Attribute Value Should Be       ${card_expanded_body}       style                   height: auto; gap: 24px;
	FOR    ${element}    IN    @{card_expanded_visuals}
	    Scrol down into side anchor
	    Wait Until Element Is Visible       ${element}
	END
	Scrol down into side anchor
	Wait Until Keyword Succeeds    2x    3s    Click Element            ${card_arrow_collapse}

Validate Applied Job: job cards/expanded state/tags
	${tag_elements}=    Locators to list        ${card_tag_index}
	Click Element        ${card_arrow_expand}
	FOR    ${element}    IN                     @{tag_elements}
	    Scrol down into side anchor
	    Wait Until Element Is Visible       ${element}
	    Element Text Should Not Be          ${element}                  ${EMPTY}
	    Wait Until Keyword Succeeds     2x	    4s      Click Element   ${element}
	    Wait Until Location Is Not          ${URL_applied_job}
	    Go Back
	    Wait Until Keyword Succeeds    2x    4s    Click Element        ${card_arrow_expand}
	END
	Scrol down into side anchor
	Wait Until Keyword Succeeds    2x    3s    Click Element            ${card_arrow_collapse}

Validate Applied Job: Apply button
	${edit_mode}    Edit mode checker
	Wait Until Element Is Visible           ${apply_button}
	Scroll into element                     ${apply_button}
	Element Text Should Be                  ${apply_button}             Lamar Sekarang
	IF    ${edit_mode} == True
	    Element Should Be Enabled           ${apply_button}
	    Click Button                        ${apply_button}
	    Wait Until Location Is Not          ${URL_applied_job}
	ELSE
		Element Should Be Disabled          ${apply_button}
	END

Validate Applied Job > 60 minutes: Screening questions existence
    ${status}   Screening questions checker
	IF    ${status} == True
		Wait Until Page Contains Element    ${scr_title}
        Element Text Should Be              ${scr_title}                Pertanyaan Seleksi Awal
		${scr_question}=    Locators to list    ${scr_index_inactive}
		FOR    ${element}    IN                 @{scr_question}
		        ${element_expanded}=    Convert To String               ${element}${scr_index_nest}
		        ${expand_state}=        Convert To String               ${element}${scr_inactive_header}
				Wait Until Element Is Visible   ${element}
				Wait Until Keyword Succeeds    2x    4s    Click Element    ${element}
				Element Attribute Value Should Be       ${expand_state}        aria-expanded    true
				Wait Until Element Is Visible           ${element_expanded}
				Scroll into element                     ${element_expanded}
				Wait Until Keyword Succeeds    2x    4s    Click Element    ${expand_state}
				Element Attribute Value Should Be       ${expand_state}        aria-expanded    false
		END
	ELSE
	    Page Should Not Contain                 ${scr_index_inactive}
	    Pass Execution                          Screening Questions doesn't exist on the current page
	END

Validate Applied Job > 60 minutes: Screening questions response is disabled
    ${status}   Screening questions checker
	IF    ${status} == True
		Expand all screening questions

		# Validate pharagraph type
		${essay_status}=    Run Keyword And Return Status    Page Should Contain Element    ${scr_paragraph}
		IF    ${essay_status} == True
		    ${elements_paragraph}=     Locators to list      ${scr_paragraph}
		    FOR    ${paragraph}    IN           @{elements_paragraph}
		        Element Should Be Disabled      ${paragraph}
			END
		ELSE
			Pass Execution    No essay questions type on this vacancy
		END

		# Validate multiple choice type
		${choices_status}=    Run Keyword And Return Status    Page Should Contain Element    ${scr_choices}
		IF    ${choices_status} == True
		    ${elements_choices}=     Locators to list      ${scr_choices}
		    FOR    ${choice}    IN             @{elements_choices}
		        Element Should Be Disabled      ${choice}
			END
		ELSE
			Pass Execution    No multiple choice type question on this vacancy
		END

		# Validate checkboxes type
		${checkbox_status}=    Run Keyword And Return Status    Page Should Contain Element    ${scr_checkbox}
		IF    ${checkbox_status} == True
		    ${elements_choices}=     Locators to list      ${scr_checkbox}
		    FOR    ${choice}    IN             @{elements_choices}
		        Element Should Be Disabled      ${choice}
			END
		ELSE
			Pass Execution    No checkboxes type question on this vacancy
		END

		# Todo 4: Validate upload doc type
		# Todo 5: Validate upload datafile type
		# Todo 6: Validate upload image type
	ELSE
	    Page Should Not Contain                 ${scr_index_inactive}
	    Pass Execution                          Screening Questions doesn't exist on the current page
	END