*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections
Resource    ../persona/admin/variable_admin.resource
Resource    ../../tests/browser.resource

*** Variables ***
# Pre-requisite
${test_URL}                 https://staging.karirlab.co/job/automation-msib-test-status-badges--karirlab/applicant

# Header Components
${nav_back}                 class:BackNavigation_breadcrumbs__FZwHF
${page_title}               xpath://h3[@class='ant-typography']

# Job Cards Default State Component
${card_image}               xpath://img[@alt='Company thumbnail']
${card_top_deadline}        xpath:(//span[contains(@class, 'deadline')])[1]
${card_easy_apply}          xpath://span[contains(@class, 'easyApply')]
${card_title}               xpath:(//h4[@class='ant-typography'])[1]
${card_badge_index}         (//span[contains(@class, 'chip')])
${card_badge_msib}          class:JobDetail_jobDetail__chip__v7Ytc
${card_badge_location}      xpath:(//span[contains(@class, 'chip')])[1]
${card_badge_industry}      xpath:(//span[contains(@class, 'chip')])[2]
${card_badge_type}          xpath:(//span[contains(@class, 'chip')])[3]
${card_arrow_expand}        xpath://div[contains(text(),'Lihat Lebih Banyak')]
@{badge_default_visual}     ${card_image}   ${card_top_deadline}    ${card_easy_apply}  ${card_title}   ${card_badge_msib}  ${card_badge_location}  ${card_badge_industry}  ${card_badge_type}  ${card_arrow_expand}
@{badge_default_text}       ${card_top_deadline}    ${card_easy_apply}  ${card_title}   ${card_badge_location}  ${card_badge_industry}  ${card_badge_type}  ${card_arrow_expand}

${card_bot_deadline}        xpath:(//span[contains(@class, 'deadline')])[2]
${card_description_title}   xpath:(//h4[@class='ant-typography'])[2]
${card_tag_wrapper}         xpath://div[contains(@class,'horizontal')])[3]
${card_tag_index}           //a[contains(@href, '/job?tags')]
${card_arrow_collapse}      xpath://div[contains(@class, 'item') and text()='Lihat Lebih Sedikit']
${footer}                   xpath://div[contains(@class, 'footer')]




*** Keywords ***
Open job apply page
	Login as admin  staging  login  headless=False
    Go To    ${test_URL}

Locators to list
	[Arguments]     ${identical_locator}
	${total_element}=   Get Element Count     xpath:${identical_locator}
	${collected_elements}=  Create List
	FOR    ${counter}    IN RANGE    ${total_element}
		${current_locator}=     Convert To String    xpath:(${identical_locator})[${counter+1}]
		Append To List    ${collected_elements}     ${current_locator}
	END
	[Return]    ${collected_elements}

Scroll down to the bottom page
    Execute JavaScript    window.scrollTo(0, document.body.scrollHeight)