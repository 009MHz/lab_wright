*** Settings ***

Resource    ../../resources/setting.resource
Resource    ../../resources/admin/variable_admin.resource
Resource    ../../resources/admin/element_admin.resource

*** Test Cases ***
Open Login page
    Wait Until Element Contains    xpath://*[@id="__next"]/div/div[2]/div/div/h3    ${ADMIN_TEXT_PAGE}
    # Page Should Contain    ${ADMIN_TEXT_PAGE}
    Wait Until Element Is Enabled    ${ADMIN_FIELD_EMAIL}
    Wait Until Element Is Enabled    ${ADMIN_FIELD_PASSWORD}
    Wait Until Element Is Enabled    ${ADMIN_BUTTON_LOGIN}
    # Element Text Should Be    ${ADMIN_TEXT_EMAIL}    ${LOGIN_TEXT_EMAIL}
    # Element Text Should Be    ${ADMIN_TEXT_PASSWORD}    ${LOGIN_TEXT_PASSWORD}
    Click Element    ${ADMIN_FIELD_EMAIL}
    Input Text    ${ADMIN_FIELD_EMAIL}   ${LOGIN_ADMIN_EMAIL}
    Click Element    ${ADMIN_FIELD_PASSWORD}
    Input Text    ${ADMIN_FIELD_PASSWORD}    ${LOGIN_ADMIN_EMAIL}
    Click Element    ${ADMIN_BUTTON_LOGIN}
Close Browser
    Close Browser