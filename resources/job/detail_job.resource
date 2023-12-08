*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections

*** Variables ***
${URL}              https://staging.karirlab.co/job/msib-test-status-badges--karirlab
${nav_back}         class:BackNavigation_breadcrumbs__FZwHF

# Company Detail Section
${comp_deadline_top}        xpath:(//span[contains(@class, 'deadline')])[1]
${comp_image}               class:ant-image-img
${comp_name_small}          xpath:(//span[@class='ant-typography'])[1]
${comp_job_title}           xpath:(//h4[@class='ant-typography'])[2]
${comp_badge_msib}          class:JobDetail_jobDetail__chip__v7Ytc
${comp_badge_location}      xpath:(//span[contains(@class, 'chip')])[1]
${comp_badge_industry}      xpath:(//span[contains(@class, 'chip')])[2]
${comp_badge_type}          xpath:(//span[contains(@class, 'chip')])[3]
${comp_deadline_bottom}     xpath:(//span[contains(@class, 'deadline')])[2]
@{comp_visual}      ${comp_deadline_top}    ${comp_image}   ${comp_name_small}  ${comp_job_title}   ${comp_badge_msib}  ${comp_badge_location}  ${comp_badge_industry}  ${comp_badge_type}  ${comp_deadline_bottom}
@{comp_text}    ${comp_job_title}   ${comp_name_small}  ${comp_badge_location}  ${comp_badge_industry}  ${comp_badge_type}

# Job Description section
${desc_title}               xpath://h4[normalize-space()='Deskripsi Pekerjaan']
${desc_tag_wrapper}         xpath:(//div[contains(@class, 'horizontal')])[4]
${desc_tag_index}           //a[contains(@href, '/job?tags')]

# Job Footer Section
${foot_title}               xpath://h4[normalize-space()='Informasi Perusahaan']
${foot_wrapper}             xpath://div[contains(@class, 'jobInfo')]
${foot_company}             xpath:(//span[@class='ant-typography'])[2]
${foot_location}            xpath:(//span[@class='ant-typography'])[3]
${foot_industry}            xpath:(//span[@class='ant-typography'])[4]
${foot_linkedin}            xpath:(//span[@class='ant-typography'])[5]
${foot_employee}            xpath:(//span[@class='ant-typography'])[6]
${foot_site}                xpath:(//span[@class='ant-typography'])[7]
@{foot_url}        ${foot_linkedin}    ${foot_site}
@{foot_visual}  ${foot_title}   ${foot_wrapper}     ${foot_company}     ${foot_location}    ${foot_industry}    ${foot_linkedin}    ${foot_employee}    ${foot_site}
@{foot_text}    ${foot_company}     ${foot_location}    ${foot_industry}    ${foot_employee}

# Job Detail Apply
${apply_wraper}             class:JobDetail_jobDetail__card__xiqli
${apply_title}              xpath://h4[normalize-space()='Lamar posisi ini?']
${apply_button}             xpath://button[contains(@class, 'apply')]







*** Keywords ***
Open Tested Page
	Open Browser    ${URL}      chrome
	Maximize Browser Window

Calculate element total
	[Arguments]     ${path}
	${total}=   Get Element Count    ${path}
	Log    ${total}

Locators to list
	[Arguments]     ${identical_locator}
	${total_element}=   Get Element Count     xpath:${identical_locator}
	${collected_elements}=  Create List
	FOR    ${counter}    IN RANGE    ${total_element}
		${current_locator}=     Convert To String    xpath:(${identical_locator})[${counter+1}]
		Append To List    ${collected_elements}     ${current_locator}
	END
	[Return]    ${collected_elements}

