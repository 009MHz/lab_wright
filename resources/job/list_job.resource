*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections

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

# Page Body
${body_cards}               xpath://div[contains(@class,'md-12')]
${body_logo}                //img[contains(@class, 'jobCard__image')]
${body_company_name}        //div[contains(@class, 'jobCard__content')]/span[contains(@class, 'secondary')]
${body_job_title}           //div[contains(@class, 'jobCard__content')]/h4
${body_job_location}        //div[contains(@class, 'jobCard__content')]/span[not(contains(@class, 'secondary'))]
${body_job_description}     //div[contains(@class, 'description')]
${body_job_industry}        //div[contains(@class, 'description')]/span[1]
${body_job_type}            //div[contains(@class, 'description')]/span[2]
${body_job_daycount}        //div[@class='ant-col ant-col-14']
${body_job_easy_apply}      //div[contains(@class, 'easyApply')]
${body_cards_containers}    ${body_logo}        ${body_company_name}    ${body_job_title}   ${body_job_location}    ${body_job_description}     ${body_job_industry}    ${body_job_type}    ${body_job_daycount}    ${body_job_easy_apply}

# Pagination Section
${page_previous}            xpath://li[@title='Previous Page']
${page_next}                xpath://li[@title='Next Page']
@{page_arrow}   ${page_next}    ${page_previous}
${page_container}           //li[contains(@class, 'ant-pagination-item')]


*** Keywords ***
Collect locators as array
	${total_pages}=         Get Element Count       xpath:${page_container}
	${pages}=               Create List
	FOR    ${counter}    IN RANGE    ${total_pages}
	    ${current_index}=   Convert To String       xpath:(${page_container})[${counter+1}]
	    Append To List      ${pages}                ${current_index}
	END
	[Return]                ${pages}


Whole cards counter
    ${carousel_count}=      Get Element Count       ${body_cards}
    [Return]                ${carousel_count}

Create all job card locators
    [Arguments]             ${total_items}
    ${card_data}=           Create List
    FOR    ${counter}    IN RANGE    ${total_items}
        ${current_card}=    Create Dictionary
        ${card_logo}=       Convert To String       xpath:(${body_logo})[${counter+1}]
        ${card_company}=    Convert To String       xpath:(${body_company_name})[${counter+1}]
        ${card_title}=      Convert To String       xpath:(${body_job_title})[${counter+1}]
        ${card_location}=   Convert To String       xpath:(${body_job_location})[${counter+1}]
        ${card_description}=    Convert To String   xpath:(${body_job_description})[${counter+1}]
        ${card_industry}=   Convert To String       xpath:(${body_job_industry})[${counter+1}]
        ${card_type}=       Convert To String       xpath:(${body_job_type})[${counter+1}]
        ${card_daycount}=   Convert To String       xpath:(${body_job_daycount})[${counter+1}]
        ${card_easy_apply}=     Convert To String   xpath:(${body_job_easy_apply})[${counter+1}]

        Set To Dictionary    ${current_card}    logo=${card_logo}
        Set To Dictionary    ${current_card}    company=${card_company}
        Set To Dictionary    ${current_card}    title=${card_title}
        Set To Dictionary    ${current_card}    location=${card_location}
        Set To Dictionary    ${current_card}    description=${card_description}
        Set To Dictionary    ${current_card}    industry=${card_industry}
        Set To Dictionary    ${current_card}    type=${card_type}
        Set To Dictionary    ${current_card}    daycount=${card_daycount}
        Set To Dictionary    ${current_card}    easy_apply=${card_easy_apply}
        Append To List      ${card_data}    ${current_card}
    END
    [Return]            ${card_data}

Retrieve job card component
    ${collected_cards}=     Create List
    FOR    ${attempt}    IN RANGE    4
        ${counter}=         Whole cards counter
        IF  ${attempt} > 2
            Fail            Unable to retrieve the elements after 3 attempts
        ELSE IF    ${counter} != 0
            ${collected_cards}=    Create all job card locators    ${counter}
            Exit For Loop
        ELSE    
            Log    Attempt ${attempt + 1} failed. Retrying...    
        END
    END
    [Return]    ${collected_cards}


Check job card
	[Arguments]        ${source}
    FOR  ${item}    IN      @{source}
        Wait Until Element Is Visible    ${item["logo"]}
        Wait Until Element Is Visible    ${item["company"]}
        Wait Until Element Is Visible    ${item["title"]}
        Wait Until Element Is Visible    ${item["location"]}
        Wait Until Element Is Visible    ${item["description"]}
        Wait Until Element Is Visible    ${item["industry"]}
        Wait Until Element Is Visible    ${item["type"]}
        Wait Until Element Is Visible    ${item["daycount"]}
        Wait Until Element Is Visible    ${item["easy_apply"]}
        Wait Until Keyword Succeeds    5s    2    Click Element    ${item["easy_apply"]}
    END
