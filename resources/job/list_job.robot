*** Settings ***
Library        SeleniumLibrary
Test Teardown   Close Browser


*** Variables ***
${browser}                  chrome
${url}                      https://staging.karirlab.co/job
# Filter section
${btn_easy_apply}           xpath:(//button[contains(@class, 'jobFilter')])[1]
${btn_MSIB}                 xpath:(//button[contains(@class, 'jobFilter')])[2]
@{btn_filters}      ${btn_easy_apply}       ${btn_MSIB}

${textbox_position}         name:keyword
${textbox_company}          name:company_industries
${textbox_location}         name:locations

@{text_boxes}   ${textbox_position}     ${textbox_company}      ${textbox_location}
${checkbox_full}            xpath://input[@value='Full-Time']
${checkbox_part}            xpath://input[@value='Part-Time']
${checkbox_intern}          xpath://input[@value='Internship']
${checkbox_contract}        xpath://input[@value='Contract']
${checkbox_volunteer}       xpath://input[@value='Volunteer']
${checkbox_scholar}         xpath://input[@value='Scholarship']
${checkbox_partner}         xpath://input[@value='Partnership']
@{checkboxes}    ${checkbox_intern}    ${checkbox_partner}  ${checkbox_contract}    ${checkbox_volunteer}    ${checkbox_scholar}    ${checkbox_full}    ${checkbox_part}

# Sort section
${sort_control}             xpath:(//div[@class='ant-select-selector'])[2]
${sort_control_expanded}    class:rc-virtual-list-holder
${sorter_date_asc}          xpath://div[@title='Tanggal Dibuat (A to Z)']
${sorter_date_desc}         xpath://div[@title='Tanggal Dibuat (Z to A)']
${sorter_name_asc}          xpath://div[@title='Nama (A to Z)']
${sorter_name_desc}         xpath://div[@title='Nama (Z to A)']
@{sort_options}     ${sorter_date_asc}     ${sorter_date_desc}    ${sorter_name_asc}     ${sorter_name_desc}


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