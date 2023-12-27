*** Settings ***
Resource        ../../resources/job/applied_job.resource
Suite Setup     Login as normal user    staging       login      headless=True
Task Setup      Go To    ${URL_applied_job}
Suite Teardown  Close Browser

*** Test Cases ***
Applied job > 60 minutes state: Validate header component
    FOR    ${element}    IN    @{header_visuals}
        Wait Until Element Is Visible                           ${element}
    END
    Element Text Should Be          ${header_breadcrumb}        Back to Job List
    Element Text Should Be          ${header_title}             Lamar Pekerjaan
    Element Should Contain          ${header_status}            Lamaran kamu telah berhasil terkirim ke

Applied job > 60 minutes state: Employers profile component
    FOR    ${element}    IN    @{emp_visuals}
        Wait Until Element Is Visible       ${element}
    END
    Element Text Should Be          ${emp_job_state}            Applied
    Element Text Should Not Be      ${emp_job_title}            ${EMPTY}
    Element Text Should Not Be      ${emp_used_resume}          ${EMPTY}
    Element Should Contain          ${emp_apply_day_count}      hari yang lalu
