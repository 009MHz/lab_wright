*** Settings ***
Resource        ../../resources/job/list_job.resource
Resource        ../browser.resource
Task Tags       Job Page
Task Teardown   Close Browser
Task Setup      Open Page    staging    job     headless=True

*** Test Cases ***
Validate filter section
	[Tags]      Smoke Test      Filter
    # Main Filter button
    FOR    ${btn}    IN    @{btn_filters}
        Wait Until Keyword Succeeds    3    5s    Element Should Be Visible    ${btn}
        Click Button                        ${btn}
    END
    # Filter Textboxes
    FOR    ${textbox}    IN    @{text_boxes}
        Wait Until Element Is Enabled       ${textbox}
        Input Text                          ${textbox}     Writing on ${textbox}
    END
    # Filter Checkboxes
    FOR    ${checkbox}    IN    @{checkboxes}
        Wait Until Element Is Enabled       ${checkbox}
        Wait Until Keyword Succeeds    3s    2    Click Element    ${checkbox}
    END

Validate sort controller
	[Tags]      Smoke Test      Sort Controller
	Wait Until Element Is Visible    ${sort_control}
    FOR    ${opt}    IN    @{sort_options}
        Click Element    ${sort_control}
        Wait Until Element Is Visible    ${sort_control_expanded}
        Wait Until Element Is Visible    ${opt}
        Click Element   ${opt}
    END

Validate pagination element
	[Tags]      Smoke Test      Pagination
	FOR    ${page_button_arrow}    IN    @{page_arrow}
	    Wait Until Element Is Visible    ${page_button_arrow}
	    Wait Until Keyword Succeeds    3s    2    Click Element    ${page_button_arrow}
	END

	${page_index}=  Retrieve all pages locator
	FOR    ${element}    IN    @{page_index}
	    Log    ${element}
	    Wait Until Element Is Visible    ${element}
	    Wait Until Keyword Succeeds    3s    2    Click Element    ${element}
	END

Validate job list content
	${cards_count}=     Get Element Count    ${body_cards}
	FOR    ${counter}    IN RANGE    ${cards_count}
	    ${card_logo}=           Convert To String    xpath:(${body_logo})[${counter+1}]
	    ${card_company}=        Convert To String    xpath:(${body_company_name})[${counter+1}]
	    ${card_title}=          Convert To String    xpath:(${body_job_title})[${counter+1}]
	    ${card_location}=       Convert To String    xpath:(${body_job_location})[${counter+1}]
	    ${card_description}=    Convert To String    xpath:(${body_job_description})[${counter+1}]
	    ${card_industry}=       Convert To String    xpath:(${body_job_industry})[${counter+1}]
	    ${card_type}=           Convert To String    xpath:(${body_job_type})[${counter+1}]
	    ${card_daycount}=       Convert To String    xpath:(${body_job_daycount})[${counter+1}]
	    ${card_easy_apply}=     Convert To String    xpath:(${body_job_easy_apply})[${counter+1}]

	    Wait Until Element Is Visible    ${card_logo}
	    Wait Until Element Is Visible    ${card_company}
	    Wait Until Element Is Visible    ${card_title}
	    Wait Until Element Is Visible    ${card_location}
	    Wait Until Element Is Visible    ${card_description}
	    Wait Until Element Is Visible    ${card_industry}
	    Wait Until Element Is Visible    ${card_type}
	    Wait Until Element Is Visible    ${card_daycount}
	    Wait Until Element Is Visible    ${card_easy_apply}
	    Wait Until Keyword Succeeds    3s    2    Click Element    ${card_easy_apply}
	END