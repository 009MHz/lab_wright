*** Settings ***
Resource        ../../resources/job/apply_job.resource
Resource        ../browser.resource
Suite Setup     Login as admin    staging       login      headless=False
Test Setup      Go To    ${test_URL}
Suite Teardown  Close Browser

*** Test Cases ***
Validate header & job card component
	${tag_elements}=    Locators to list        ${card_tag_index}
	Wait Until Element Is Visible               ${nav_back}
	Element Text Should Be                      ${nav_back}             Back to Job List
	Wait Until Element Is Visible               ${page_title}
	Element Text Should Be                      ${page_title}           Lamar Pekerjaan
	FOR    ${element}    IN    @{card_default_visual}
	    Wait Until Element Is Visible    ${element}
	END

	FOR    ${element}    IN    @{card_default_text}
	    Element Text Should Not Be    ${element}    ${EMPTY}
	END

	Click Element    ${card_arrow_expand}
	FOR    ${element}    IN    @{card_expand_component}
	    Wait Until Element Is Visible           ${element}
	    Element Text Should Not Be              ${element}              ${EMPTY}
	END

	Scroll down to the bottom page
	FOR    ${element}    IN    @{tag_elements}
	    Wait Until Element Is Visible           ${element}
	    Element Text Should Not Be              ${element}              ${EMPTY}
	END
	Wait Until Keyword Succeeds     3x  5s      Click Element           ${card_arrow_collapse}

Validate resume section
	Wait Until Element Is Visible               ${res_title}
	Element Should Contain                      ${res_description}      Pilih resume KarirLabmu
	Element Should Contain                      ${res_description}      Buat Resume Baru
	Wait Until Element Is Enabled               ${res_field}
	Wait Until Page Contains Element            ${res_create}
	Click Element                               ${res_field}
	${resume_contents}=     Locators to list    ${res_field_content}
	FOR    ${element}    IN    @{resume_contents}
	    Wait Until Keyword Succeeds     2x  3s  Click Element           ${element}
	    Click Element                           ${res_field}
	END
	Press Keys                                  ${None}                 ESC
	Wait Until Keyword Succeeds     2x  3s      Click Element           ${res_create}
	Wait Until Location Is Not                  ${test_URL}
