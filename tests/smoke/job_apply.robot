*** Settings ***
Resource        ../../resources/job/apply_job.resource
Resource        ../browser.resource
Library     SeleniumLibrary
Task Setup  Open job apply page


*** Variables ***


*** Test Cases ***
Validate header component
	Wait Until Element Is Visible       ${nav_back}
	Element Text Should Be              ${nav_back}             Back to Job List
	Wait Until Element Is Visible       ${page_title}
	Element Text Should Be              ${page_title}           Lamar Pekerjaan

Validate job card components (collapsed state)
#	FOR    ${element}    IN    @{badge_default_visual}
#	    Wait Until Element Is Visible    ${element}
#	END
#
#	FOR    ${element}    IN    @{badge_default_text}
#	    Element Text Should Not Be    ${element}    ${EMPTY}
#	END

	Wait Until Element Is Visible       ${card_image}
	Wait Until Element Is Visible       ${card_top_deadline}
	Element Should Contain              ${card_top_deadline}    Batas Pendaftaran
	Wait Until Element Is Visible       ${card_easy_apply}
	Element Text Should Be              ${card_easy_apply}      Easy Apply
	Wait Until Element Is Visible       ${card_title}
	Element Text Should Be              ${card_title}           [Automation][MSIB] Test status Badges
	Wait Until Element Is Visible       ${card_badge_msib}
	Wait Until Element Is Visible       ${card_badge_location}
	Element Text Should Be              ${card_badge_location}    Jakarta
	Wait Until Element Is Visible       ${card_badge_industry}
	Element Text Should Be              ${card_badge_industry}    Technology
	Wait Until Element Is Visible       ${card_badge_type}
	Element Text Should Be              ${card_badge_type}    Internship
	Wait Until Element Is Visible       ${card_arrow_expand}

Validate job card components (expanded state)
	Click Element    ${card_arrow_expand}
	Wait Until Element Is Visible       ${card_bot_deadline}
	Element Should Contain              ${card_bot_deadline}    Diunggah
	Wait Until Element Is Visible    ${card_description_title}
	Element Text Should Be    ${card_description_title}    Deskripsi Pekerjaan
	Scroll down to the bottom page
	${tag_elements}=    Locators to list    ${card_tag_index}
	FOR    ${element}    IN    @{tag_elements}
	    Wait Until Element Is Visible    ${element}
	    Element Text Should Not Be    ${element}    ${EMPTY}
	END
	Wait Until Element Is Visible    ${card_arrow_collapse}
	Wait Until Keyword Succeeds    3x        5s    Click Element    ${card_arrow_collapse}

Validate job card components in all state
	Wait Until Element Is Visible       ${card_image}
	Wait Until Element Is Visible       ${card_top_deadline}
	Element Should Contain              ${card_top_deadline}    Batas Pendaftaran
	Wait Until Element Is Visible       ${card_easy_apply}
	Element Text Should Be              ${card_easy_apply}      Easy Apply
	Wait Until Element Is Visible       ${card_title}
	Element Text Should Be              ${card_title}           [Automation][MSIB] Test status Badges
	Wait Until Element Is Visible       ${card_badge_msib}
	Wait Until Element Is Visible       ${card_badge_location}
	Element Text Should Be              ${card_badge_location}    Jakarta
	Wait Until Element Is Visible       ${card_badge_industry}
	Element Text Should Be              ${card_badge_industry}    Technology
	Wait Until Element Is Visible       ${card_badge_type}
	Element Text Should Be              ${card_badge_type}    Internship
	Wait Until Element Is Visible       ${card_arrow_expand}
	Click Element    ${card_arrow_expand}
	Wait Until Element Is Visible       ${card_bot_deadline}
	Element Should Contain              ${card_bot_deadline}    Diunggah
	Wait Until Element Is Visible    ${card_description_title}
	Element Text Should Be    ${card_description_title}    Deskripsi Pekerjaan
	Scroll down to the bottom page
	${tag_elements}=    Locators to list    ${card_tag_index}
	FOR    ${element}    IN    @{tag_elements}
	    Wait Until Element Is Visible    ${element}
	    Element Text Should Not Be    ${element}    ${EMPTY}
	END
	Wait Until Element Is Visible    ${card_arrow_collapse}
	Wait Until Keyword Succeeds    3x        5s    Click Element    ${card_arrow_collapse}
	[Teardown]      Close All Browsers