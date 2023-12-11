*** Settings ***
Resource        ../../resources/job/list_job.resource
Resource        ../browser.resource
Resource        ../../resources/resume_builder/create_resume_builder.resource
Resource        ../landing_page.robot
Library        SeleniumLibrary
Test Teardown   Close Browser

*** Test Cases ***
# Suite Setup
#     Open Login page

Validate Header Section
    FOR    ${input_resume_name}    IN    @{LIST}
        Log    ${element}
        
    END