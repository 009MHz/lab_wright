*** Settings ***
Resource        ../../resources/job/applied_job.resource
Suite Setup     Login as normal user    staging       login      headless=False
Task Setup      Go To    ${URL_applied_job}
Suite Teardown  Close Browser

*** Test Cases ***
Applied job > 60 minutes state: Validate header component
    Wait Until Element Is Visible    ${header_breadcrumb}
    Element Text Should Be    ${header_breadcrumb}    Back to Job List
    Wait Until Element Is Visible    ${header_title}
    Element Text Should Be    ${header_title}    Lamar Pekerjaan
    Wait Until Element Is Visible    ${header_status}
    Element Should Contain        ${header_status}    Lamaran kamu telah berhasil terkirim ke

Applied job > 60 minutes state: Employers profile component
    Wait Until Element Is Visible    ${emp_logo}
    Wait Until Element Is Visible    ${emp_job_state}
    Element Text Should Be    ${emp_job_state}    Applied
    Wait Until Element Is Visible    ${emp_job_title}
    Element Text Should Not Be    ${emp_job_title}    ${EMPTY}
    Wait Until Element Is Visible    ${emp_used_resume}
    Element Text Should Not Be    ${emp_used_resume}    ${EMPTY}
    Wait Until Element Is Visible    ${emp_apply_day_count}
    Element Should Contain    ${emp_apply_day_count}    hari yang lalu

