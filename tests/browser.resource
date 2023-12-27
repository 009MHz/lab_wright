*** Settings ***
Resource    ../resources/setting.resource
Resource    ../resources/persona/admin/variable_admin.resource
Library     String
Library     Process
Library     SeleniumLibrary
Library     RequestsLibrary
Library     OperatingSystem
Library     json

*** Variables ***
${email_field}      id:username
${password_field}   id:password
${button_masuk}     xpath://button[@type='submit']

*** Keywords ***
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

Open Page
    [Arguments]         ${environment}              ${page_name}=None      ${headless}=False
    ${base}=            Environment Selector        ${environment}
    ${path}=            Page Selector               ${page_name}
    ${used_browser}=    Mode Selector               ${headless}

    Open Browser    ${base}${path}    ${used_browser}
    Maximize Browser Window

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

Login as super admin
	[Arguments]         ${environment}              ${page_name}=None      ${headless}=True
	${base}=            Environment Selector        ${environment}
    ${path}=            Page Selector               ${page_name}
    ${used_browser}=    Mode Selector               ${headless}
    ${account}         Get account         super_admin

    Open Browser        ${base}${path}              ${used_browser}
    Maximize Browser Window
    Input Text          ${email_field}              ${account["email"]}
    Input Text          ${password_field}           ${account["password"]}
    Click Element       ${button_masuk}
    Wait Until Location Is      https://staging.karirlab.co/dashboard

Login as admin
	[Arguments]         ${environment}              ${page_name}=None      ${headless}=False
	${base}=            Environment Selector        ${environment}
    ${path}=            Page Selector               ${page_name}
    ${used_browser}=    Mode Selector               ${headless}
    ${account}          Get account                 admin

    Open Browser        ${base}${path}              ${used_browser}
    Maximize Browser Window
    Input Text          ${email_field}              ${account["email"]}
    Input Text          ${password_field}           ${account["password"]}
    Click Element       ${button_masuk}
    Wait Until Location Is      https://staging.karirlab.co/dashboard

Login as normal user
	[Arguments]         ${environment}              ${page_name}=None      ${headless}=False
	${base}=            Environment Selector        ${environment}
    ${path}=            Page Selector               ${page_name}
    ${used_browser}=    Mode Selector               ${headless}
    ${account}          Get account                 normal

    Open Browser        ${base}${path}              ${used_browser}
    Maximize Browser Window
    Input Text          ${email_field}              ${account['email']}
    Input Text          ${password_field}           ${account['password']}
    Click Element       ${button_masuk}
    Wait Until Location Is      https://staging.karirlab.co/dashboard

Login as job applicant
	[Arguments]         ${environment}              ${page_name}=None      ${headless}=False
	${base}=            Environment Selector        ${environment}
    ${path}=            Page Selector               ${page_name}
    ${used_browser}=    Mode Selector               ${headless}
    ${account}          Get account                 normal

    Open Browser        ${base}${path}              ${used_browser}
    Maximize Browser Window
    Input Text          ${email_field}              siapaboleh5@gmail.com
    Input Text          ${password_field}           123456
    Click Element       ${button_masuk}
    Wait Until Location Is      https://staging.karirlab.co/dashboard