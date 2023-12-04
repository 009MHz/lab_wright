*** Settings ***

Resource    ../resources/setting.resource

*** Test Cases ***
Open Browser
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window
