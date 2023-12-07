*** Settings ***
Library        SeleniumLibrary
Library    String
Library    Collections

*** Variables ***
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

# Pagination Section
${page_previous}        xpath://li[@title='Previous Page']
${page_next}        xpath://li[@title='Next Page']
@{page_arrow}   ${page_next}    ${page_previous}
${page_container}   xpath://li[contains(@class, 'ant-pagination-item')]


*** Keywords ***
Retrieve all pages locator
	${total_pages}=     Get Element Count    ${page_container}
	${pages}=   Create List
	FOR    ${counter}    IN RANGE    ${total_pages}
	    ${current_index}=    Convert To Lower Case   xpath:(//li[contains(@class, 'ant-pagination-item')])[${counter+1}]
	    Append To List    ${pages}      ${current_index}
	END
	[Return]    ${pages}