# *** Settings ***

# Resource    ../resources/setting.resource
# Resource    ../resources/persona/customer/public/landing_page.resource
# Resource    ../resources/persona/customer/login/login.resource
# Library    DateTime

# *** Keywords ***
# ${DATE}=    Get Current Date

# *** Test Cases ***

# Landing Page
#     Open Browser
#     Wait Until Element Is Visible    xpath:/html/body/div[2]/div/div[2]/div/div[2]/div
#     Wait Until Element Is Enabled    xpath:/html/body/div[2]/div/div[2]/div/div[2]/button
#     Click Element   xpath:/html/body/div[2]/div/div[2]/div/div[2]/button
#     Wait Until Element Is Visible    ${BUTTON_LOGIN}    5
#     Click Element    ${BUTTON_LOGIN}

# Login Page
#     Wait Until Element Is Visible    ${USERNAME_USER}
#     Click Element    ${USERNAME_USER}
#     Input Text    ${USERNAME_USER}    ${USERNAME}
#     Wait Until Element Is Visible    ${PASSWORD_USER}
#     Click Element   ${PASSWORD_USER}
#     Input Text    ${PASSWORD_USER}    ${PASSWORD}
#     Press Keys    ${PASSWORD_USER}    ENTER
#     # Sleep    2s
#     # Wait Until Element Is Enabled    ${BUTTON_LOGIN_USER}
#     # Sleep    2s
#     # Click Element    ${BUTTON_LOGIN_USER}
#     # Sleep    2s

# Dashboard
#     Wait Until Element Is Visible    //*[@id="__next"]/section/main/div/div/section/section/div/div[1]/div/a/button
#     Click Element   //*[@id="__next"]/section/main/div/div/section/section/div/div[1]/div/a/button
#     Sleep    3s

# Resume Builder - Modal
#     Wait Until Page Contains Element    xpath:/html/body
#     Click Element   xpath:/html/body
#     Sleep    2s
#     Wait Until Page Contains Element    xpath:/html/body/div[3]/div/div[2]/div
#     Set Focus To Element    xpath:/html/body/div[3]/div/div[2]/div
#     Sleep    2s
#     Wait Until Page Contains    Isi Otomatis
#     Sleep   2s
#     Wait Until Element Is Visible    xpath:/html/body/div[3]/div/div[2]/div/div[2]/button
#     Sleep    2s
#     Click Element   xpath:/html/body/div[3]/div/div[2]/div/div[2]/button
#     Sleep    2s

# Resume Builder - Step 1
#     Wait Until Page Contains Element    xpath:/html/body
#     Click Element   xpath:/html/body
#     Sleep    2s
#     Wait Until Element Is Visible    //*[@id="title"]
#     Click Element    //*[@id="title"]
#     Input Text    //*[@id="title"]    Fardilah Test Automation

#     Wait Until Page Contains Element    xpath://*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[2]/div
#     Click Element   xpath://*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[2]/div

# Resume Builder - Step 2
#     Wait Until Element Is Visible    id:first_name
#     Click Element    id:first_name
#     Input Text  id:first_name    Fardilah
#     Wait Until Element Is Visible    id:last_name
#     Click element   id:last_name
#     Input Text    id:last_name    Test Automation
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[3]/div
#     Click Element    //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[3]/div

# Resume Builder - Step 3
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[4]/div
#     Click Element   //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[4]/div

# Resume Builder - Step 4
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[5]/div
#     Click Element   //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[5]/div

# Resume Builder - Step 5
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[6]/div
#     Click Element   //*[@id="__next"]/section/main/div/div/form/div/div[1]/div/div/div[6]/div
#     Sleep    5s

# Resume Builder - Step 6 (Preview)
#     Wait Until Page Contains Element    xpath:/html/body
#     Click Element   xpath:/html/body
#     Sleep    2s
#     Wait Until Page Contains    Pratinjau
#     Wait Until Page Contains Element   xpath://*[@id="__next"]/section/main/div/div/form/div/div[2]/div[1]/div/main/h3
#     Sleep    2s
#     Execute Javascript    window.scrollTo(-500,500)
#     Wait Until Page Contains Element    xpath://*[@id="__next"]/section/main/div/div/form/div/div[3]/div/main/button
#     Sleep   2s
#     Wait Until Page Contains    Pastikan resume kamu sudah sesuai standar industri dan terlihat profesional!
#     Wait Until Page Contains Element    xpath://*[@id="__next"]/section/main/div/div/form/div/div[3]/div/main/button
#     Sleep    2s
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/main/div/div/form/div/div[3]/div/main/button
#     Sleep    2s
#     Click Element   //*[@id="__next"]/section/main/div/div/form/div/div[3]/div/main/button
#     Sleep    10s
# Resume Builder - Success Build
#     Wait Until Element Is Visible    //*[@id="__next"]/section/header/div[2]/ul/li[6]/span/a
#     Click Element    //*[@id="__next"]/section/header/div[2]/ul/li[6]/span/a
#     Sleep    3s

# Dashboard
#     Wait Until Element Is Visible    //*[@id="__next"]/section/main/div/div/section/aside/div/ul/li[3]/span[2]/a
#     Click Element    //*[@id="__next"]/section/main/div/div/section/aside/div/ul/li[3]/span[2]/a
#     Sleep    3s

# Dashboard - Resume Saya
#     Wait Until Page Contains    My Resume
#     #JOBS
#     Wait Until Element Is Visible    //*[@id="__next"]/section/header/div[2]/ul/li[3]/span/a
#     Click Element    //*[@id="__next"]/section/header/div[2]/ul/li[3]/span/a

# Jobs - List
#     #FIND job
#     Wait Until Element Is Visible    //*[@id="keyword"]
#     Click Element    //*[@id="keyword"]
#     Input Text    //*[@id="keyword"]    QA GMT 2
#     Press Keys    //*[@id="keyword"]    ENTER
#     #FILTERED
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/main/div/div/div/div[3]/div[2]/div[1]/div[1]/button
#     Click Element   //*[@id="__next"]/section/main/div/div/div/div[3]/div[2]/div[1]/div[1]/button
#     Sleep    5s
#     #MODAL RESUME
#     Wait Until Page Contains Element    xpath:/html/body
#     Click Element   xpath:/html/body
#     Wait Until Element Is Enabled    xpath:/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/span
#     Click Element   xpath:/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/span
#     Wait Until Element Is Visible    /html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div
#     Click Element   /html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]/div
#     Click Element    /html/body/div[4]/div/div[2]/div/div[2]/div[2]/div[3]/button[1]
#     #MODAL SUCCESS
#     Wait Until Element Is Visible    /html/body/div[6]/div/div[2]/div/div[2]
#     Click Element    /html/body/div[6]/div/div[2]/div/div[2]/div/main/div/div[4]/button
#     #BACK TO DASHBOARD
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/header/div[2]/ul/li[6]/span/a
#     Click Element    //*[@id="__next"]/section/header/div[2]/ul/li[6]/span/a

# Dashboard
#     #CHECK JOBS APPLIED
#     Wait Until Element Is Enabled    //*[@id="__next"]/section/main/div/div/section/aside/div/ul/li[5]/span/a
#     Click Element   //*[@id="__next"]/section/main/div/div/section/aside/div/ul/li[5]/span/a

# Dashboard - Lowongan
#     Wait Until Page Contains    Daftar Lamaran

# Close Browser
#     Close Browser
    