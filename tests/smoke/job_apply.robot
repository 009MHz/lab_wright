*** Settings ***
Resource        ../../resources/job/apply_job.resource
Resource        ../browser.resource
Library         SeleniumLibrary
Test Setup      Open job apply page
Test Teardown   Close Browser

*** Test Cases ***
Validate header & job card component
	${tag_elements}=    Locators to list    ${card_tag_index}
	Wait Until Element Is Visible       ${nav_back}
	Element Text Should Be              ${nav_back}             Back to Job List
	Wait Until Element Is Visible       ${page_title}
	Element Text Should Be              ${page_title}           Lamar Pekerjaan
	FOR    ${element}    IN    @{card_default_visual}
	    Wait Until Element Is Visible    ${element}
	END

	FOR    ${element}    IN    @{card_default_text}
	    Element Text Should Not Be    ${element}    ${EMPTY}
	END

	Click Element    ${card_arrow_expand}
	FOR    ${element}    IN    @{card_expand_component}
	    Wait Until Element Is Visible    ${element}
	    Element Text Should Not Be    ${element}    ${EMPTY}
	END

	Scroll down to the bottom page
	FOR    ${element}    IN    @{tag_elements}
	    Wait Until Element Is Visible    ${element}
	    Element Text Should Not Be    ${element}    ${EMPTY}
	END
	Wait Until Keyword Succeeds    3x        5s    Click Element    ${card_arrow_collapse}
