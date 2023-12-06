*** Settings ***
Resource        ../../resources/job/list_job.resource

*** Variables ***
${browser}                  chrome
${url}                      https://staging.karirlab.co/job

*** Keywords ***
Open Current Browser
    Open Browser        ${url}  ${browser}
    Maximize Browser Window

*** Test Cases ***
Validate filter section
    Open Current Browser
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
        Wait Until Keyword Succeeds    2    3s    Click Element    ${checkbox}
    END

Validate Sort Controller
	Open Current Browser
	Wait Until Element Is Visible    ${sort_control}
    FOR    ${opt}    IN    @{sort_options}
        Click Element    ${sort_control}
        Wait Until Element Is Visible    ${opt}
        Click Element   ${opt}
    END