*** Settings ***
Resource    ../resources/setting.resource
Library    String
Library    Process
Library    SeleniumLibrary

*** Keywords ***
Selector Enviro
    [Arguments]    ${enviro}
    ${env}=    Convert To Lower Case    ${enviro}
    ${selected_enviro}=    Run Keyword If    '${env}' == 'prod'    Return From Keyword    ${KL_PROD}
    ...    ELSE IF    '${env}' == 'staging'    Return From Keyword    ${KL_STAGING}
    ...    ELSE IF    '${env}' == 'dev-a'    Return From Keyword    ${KL_DEV_A}
    ...    ELSE IF    '${env}' == 'dev-b'    Return From Keyword    ${KL_DEV_B}
    ...    ELSE IF    '${env}' == 'dev-c'    Return From Keyword    ${KL_DEV_C}

Selector Page
    [Arguments]    ${base_url}
    ${page}=    Convert To Lower Case    ${base_url}
    ${selected_page}=    Run Keyword If    '${page}' == 'event'    Return From Keyword    ${page}/event
    ...    ELSE IF    '${page}' == 'job'    Return From Keyword    /job
    ...    ELSE IF    '${page}' == 'company'    Return From Keyword    /company
    ...    ELSE IF    '${page}' == 'signup'    Return From Keyword    /sign-up
    ...    ELSE IF    '${page}' == 'login'    Return From Keyword    /login

Mode Selector
    [Arguments]    ${mode}
    ${selected_mode}=    Run Keyword If    '${mode}' == 'False'    Return From Keyword    ${BROWSER}
    ...    ELSE IF    '${mode}' == 'True'    Return From Keyword    headless${BROWSER}

Open Page
    [Arguments]    ${page_name}    ${environment}    ${headless}=False
    ${base}=    Selector Enviro    ${environment}
    ${path}=    Selector Page    ${page_name}
    ${used_browser}=    Mode Selector    ${headless}

    Open Browser    ${base}${path}    ${used_browser}
    Maximize Browser Window
