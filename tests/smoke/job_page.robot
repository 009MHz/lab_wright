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

Validate body job card component
	[Tags]      Smoke Test      Job Carousel
    ${card_data}=    Retrieve job card component
    IF    ${card_data}!=[]
        Check job card    ${card_data}
    ELSE
        Fail   Unable to fetching the valid data
    END