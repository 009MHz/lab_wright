*** Settings ***
Library    SeleniumLibrary
# Library  chromedriversync.py


*** Variables ***

# URL
${LOGIN_URL}    https://dev.karirlab.co

#BROWSER
${BROWSER}    Chrome

# ${chromedriver_path}=   chromedriversync.Get Chromedriver Path
# Create Webdriver    chrome   executable_path=${chromedriver_path}
# Go to  www.google.com