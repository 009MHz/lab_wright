*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}      chrome        # Define the browser selection, (Chrome, Firefox, Edge, Safari, headlesschrome, headlessfirefox)

# Karirlab URL
${KL_PROD}      https://karirlab.co/       # turning off Prod ENV
${KL_STAGING}   https://staging.karirlab.co
${KL_DEV}       https://dev.karirlab.co/
${KL_DEV_A}     https://dev-a.karirlab.co/
${KL_DEV_B}     https://dev-b.karirlab.co/
${KL_DEV_C}     https://dev-c.karirlab.co/