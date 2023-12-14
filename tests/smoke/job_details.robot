*** Settings ***
Resource        ../../resources/job/detail_job.resource
Resource        ../browser.resource
Suite Setup      Open Tested Page
Suite Teardown   Close Browser

*** Test Cases ***
Validate breadcrumb component
	Wait Until Element Is Enabled           ${nav_back}
	Element Text Should Be                  ${nav_back}             Kembali ke daftar lowongan
	Click Element                           ${nav_back}
	Wait Until Location Is Not              ${URL}
	Go Back

Validate company detail section
	FOR    ${element}    IN                 @{comp_visual}
	    Wait Until Element Is Visible       ${element}
	END

	FOR    ${element}    IN                 @{comp_text}
	    Element Text Should Not Be          ${element}              ${EMPTY}
	END


Validate job description component
	Wait Until Element Is Visible           ${desc_title}
	Wait Until Element Is Visible           ${desc_tag_wrapper}
	${tags}=    Locators to list            ${desc_tag_index}
	FOR    ${element}    IN    @{tags}
	    Wait Until Element Is Visible       ${element}
		Element Text Should Not Be          ${element}              ${EMPTY}
	    Wait Until Keyword Succeeds    4s    2    Click Element     ${element}
	    Wait Until Location Is Not          ${URL}
	    Go Back
	END

Validate footer component
	FOR    ${element}    IN                 @{foot_visual}
	    Wait Until Element Is Visible       ${element}
	END

	FOR    ${element}    IN                 @{foot_text}
	    Element Text Should Not Be          ${element}              ${EMPTY}
	END

    FOR  ${element}  IN  @{foot_url}
        Wait Until Keyword Succeeds    3    5s    Click Element     ${element}
        Wait Until Location Is Not          ${URL}
        Go Back
    END

Validate job apply component
    Wait Until Element Is Visible           ${apply_wraper}
	Wait Until Element Is Visible           ${apply_title}
	Element Text Should Be                  ${apply_title}          Lamar posisi ini?
	Wait Until Element Is Enabled           ${apply_button}
	Element Text Should Be                  ${apply_button}         Lamar Posisi
	Click Button                            ${apply_button}
	Wait Until Location Is Not              ${URL}
