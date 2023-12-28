*** Settings ***
Resource    ../resources/setting.resource
Resource    ../resources/persona/admin/variable_admin.resource
Library     String
Library     Process
Library     RequestsLibrary
Library     OperatingSystem
Library     json

*** Variables ***
${email_field}      id:username
${password_field}   id:password
${button_masuk}     //button[@type='submit']

*** Keywords ***
Get account
	[Arguments]         ${account_type}
    ${raw_data}=    Get File    resources/data/account/credentials.json
    ${json}=        Evaluate    json.loads('''${raw_data}''')
    ${account}=       Set Variable    ${EMPTY}
    FOR    ${account}    IN    @{json}
        FOR    ${credential}    IN    @{account}
            IF  "${credential}" == "${account_type}"
                ${account}=   Set Variable    ${account}[${credential}]
				RETURN  ${account}
            END
        END
    END

Environment Selector
    [Arguments]    ${enviro}
    ${env}=    Convert To Lower Case    ${enviro}
    ${selected_enviro}=    Run Keyword If    '${env}' == 'prod'    Return From Keyword    ${KL_PROD}
    ...    ELSE IF    '${env}' == 'staging'     Return From Keyword    ${KL_STAGING}
    ...    ELSE IF    '${env}' == 'dev-a'       Return From Keyword    ${KL_DEV_A}
    ...    ELSE IF    '${env}' == 'dev-b'       Return From Keyword    ${KL_DEV_B}
    ...    ELSE IF    '${env}' == 'dev-c'       Return From Keyword    ${KL_DEV_C}

Page Selector
    [Arguments]    ${base_url}
    ${page}=    Run Keyword If    '${base_url}' != 'None'    Convert To Lower Case    ${base_url}
    ${selected_page}=    Run Keyword If    '${page}' == 'None'    Return From Keyword    ${EMPTY}
    ...    ELSE IF    '${page}' == 'event'      Return From Keyword    /event
    ...    ELSE IF    '${page}' == 'job'        Return From Keyword    /job
    ...    ELSE IF    '${page}' == 'company'    Return From Keyword    /company
    ...    ELSE IF    '${page}' == 'signup'     Return From Keyword    /sign-up
    ...    ELSE IF    '${page}' == 'login'      Return From Keyword    /login

Mode Selector
    [Arguments]    ${mode}
    ${selected_mode}=    Run Keyword If    '${mode}' == 'False'    Return From Keyword    ${BROWSER}
    ...    ELSE IF    '${mode}' == 'True'       Return From Keyword    headless${BROWSER}

Account Selector
    [Arguments]        ${role_name}
    ${selected_account}=    Run Keyword If    '${role_name}' == 'normal'    Get account     normal
    ...    ELSE IF          '${role_name}' == 'admin'               Get account     admin
    ...    ELSE IF          '${role_name}' == 'super_admin'         Get account     super_admin
    ...    ELSE IF          '${role_name}' == 'job_applicant'       Get account     job_applicant
    [Return]            ${selected_account}

Open Page
    [Arguments]         ${environment}              ${page_name}=None      ${headless}=False
    ${base}=            Environment Selector        ${environment}
    ${path}=            Page Selector               ${page_name}
    ${used_browser}=    Mode Selector               ${headless}

    Open Browser    ${base}${path}    ${used_browser}
    Maximize Browser Window

Login with specific role
	[Documentation]     Executing login action with specific condition. 
    ...    role: contain the account type that executes the action (i.e: normal, admin, super_admin, etc). 
    ...    environment:contain the selected environment that will be used for testing. 
    ...    page_name: contain the redirection entry point that will be used (i,e: event, job, login, etc). 
    ...    headless: the browser mode that will be used for testing (False: show the process, True: hide the process)
	[Arguments]         ${role}="normal"            ${environment}="staging"       ${page_name}=None      ${headless}=False
	${base}=            Environment Selector        ${environment}
    ${path}=            Page Selector               ${page_name}
    ${used_browser}=    Mode Selector               ${headless}
    ${account}          Account Selector            ${role}

    Open Browser        ${base}${path}              ${used_browser}
    Maximize Browser Window
    Input Text          ${email_field}              ${account['email']}
    Input Text          ${password_field}           ${account['password']}
    Press Keys    ${None}    ENTER
    Wait Until Location Is      https://staging.karirlab.co/dashboard