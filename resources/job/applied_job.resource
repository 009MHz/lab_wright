*** Settings ***
Library     SeleniumLibrary
Library     String
Library     Collections
Library     OperatingSystem
Resource    ../../tests/browser.resource

*** Variables ***
${URL_applied_job}      https://staging.karirlab.co/job/automation-msib-test-status-badges--karirlab/applicant

# More than 60 minutes state
# Header
${header_breadcrumb}    //a[contains(@class, 'breadcrumbs')]
${header_title}         //h3[contains(., 'Lamar')]
${header_status}        //h5[contains(@class, 'submitted')]

# Employers Profile
${emp_logo}        //img[@alt='company logo']
${emp_job_state}    //div[contains(@class, 'StatusLabel')]
${emp_job_title}    //h5[contains(@class, 'jobTitle')]
${emp_used_resume}    (//div[contains(@class, 'JobCard')]//div[contains(@class,'horizontal')])[2]
${emp_apply_day_count}    (//div[contains(@class, 'JobCard')]//div[contains(@class,'horizontal')])[3]


*** Keywords ***
Locators to list
	[Arguments]                         ${identical_locator}
	${total_element}=                   Get Element Count           xpath:${identical_locator}
	${collected_elements}=              Create List
	FOR    ${counter}    IN RANGE       ${total_element}
		${current_locator}=             Convert To String           xpath:(${identical_locator})[${counter+1}]
		Append To List                  ${collected_elements}       ${current_locator}
	END
	[Return]    ${collected_elements}

Scroll down to the bottom page
    Execute JavaScript                  window.scrollTo(0, document.body.scrollHeight)