*** Settings ***
Resource        ../../resources/job/apply_job.resource
Suite Setup     Login as normal user    staging       login      headless=True
Task Setup      Go To    ${URL_screening}
Suite Teardown  Close Browser

*** Test Cases ***
Validate header section
	${tag_elements}=    Locators to list        ${card_tag_index}
	Wait Until Element Is Visible               ${nav_back}
	Element Text Should Be                      ${nav_back}             Back to Job List
	Wait Until Element Is Visible               ${page_title}
	Element Text Should Be                      ${page_title}           Lamar Pekerjaan
	Click Element    ${nav_back}
	Wait Until Location Is Not    ${URL_screening}
	Go Back

Validate job card component: collapsed state
	FOR    ${element}    IN                     @{card_default_visual}
	    Wait Until Element Is Visible           ${element}
	END

	FOR    ${element}    IN                     @{card_default_text}
	    Element Text Should Not Be              ${element}              ${EMPTY}
	END

	Click Element    ${card_arrow_expand}

Validate job card component: expanded state
	Click Element    ${card_arrow_expand}
	Scroll down to the bottom page
	FOR    ${element}    IN                     @{card_expand_component}
	    Wait Until Element Is Visible           ${element}
	    Element Text Should Not Be              ${element}              ${EMPTY}
	END

	${tag_elements}     Locators to list    ${card_tag_index}
	FOR    ${element}    IN                     @{tag_elements}
        Wait Until Element Is Visible           ${element}
	END

	Wait Until Keyword Succeeds    2x    3s    Click Element           ${card_arrow_collapse}

Validate resume section
	Wait Until Element Is Visible               ${res_title}
	Element Should Contain                      ${res_description}      Pilih resume KarirLabmu
	Element Should Contain                      ${res_description}      Buat Resume Baru
	Wait Until Element Is Enabled               ${res_field}
	Wait Until Page Contains Element            ${res_create}
	Click Element                               ${res_field}

	${resume_contents}=     Locators to list    ${res_field_content}
	FOR    ${element}    IN                     @{resume_contents}
	    Wait Until Keyword Succeeds     2x  3s  Click Element           ${element}
	    Click Element                           ${res_field}
	END
	Press Keys                                  ${None}                 ESC
	Wait Until Keyword Succeeds     2x  3s      Click Element           ${res_create}
	Wait Until Location Is Not                  ${URL_screening}

Validate screening question: Existence
	${status}   Screening Questions Checker
	IF    ${status} == True
	    Wait Until Page Contains Element        ${scr_title}
	    Element Text Should Be                  ${scr_title}            Pertanyaan Seleksi Awal
	    ${scr_question_elements}=               Locators to list        ${scr_index}
	    FOR    ${element}    IN                 @{scr_question_elements}
	        Wait Until Element Is Visible       ${element}
		END
	ELSE
	    Element Should Not Be Visible           ${scr_index}
	    Pass Execution                          Screening Questions doesn't exist on the current page
	END

Validate screening questions: Multiple Choice
	${status}=      Screening Questions Checker
	IF    ${status} == True
	    ${elements_radio}=  Locators to list    ${scr_choices}
	    FOR    ${element}    IN                 @{elements_radio}
	        Wait Until Element Is Enabled       ${element}
	        Element Text Should Not Be          ${element}              ${EMPTY}
	        Wait Until Keyword Succeeds    3x    1s    Click Element    ${element}
		END
	ELSE
	    Element Should Not Be Visible   ${scr_index}
	    Pass Execution                          Screening questions with multiple choice doesn't exist on the current page
	END

Validate screening questions: Checkboxes
	${status}=      Screening Questions Checker
	IF    ${status} == True
	    ${elements_checkbox}=   Locators to list    ${scr_checkbox}
	    FOR    ${element}    IN                 @{elements_checkbox}
	        Wait Until Element Is Enabled       ${element}
	        Element Text Should Not Be          ${element}              ${EMPTY}
	        Wait Until Keyword Succeeds    3x    1s    Click Element    ${element}
		END
	ELSE
	    Element Should Not Be Visible           ${scr_index}
	    Pass Execution                          Screening questions with checkboxes doesn't exist on the current page
	END
Validate screening questions: Paragraph
	${status}=      Screening Questions Checker
	IF    ${status} == True
	    ${elements_pharagraph}=   Locators to list      ${scr_pharagraph}
	    FOR    ${element}    IN                 @{elements_pharagraph}
	        Wait Until Element Is Enabled       ${element}
	        Wait Until Keyword Succeeds    3x    1s    Click Element    ${element}
	        Input Text    ${element}            This text written from robotframework on the element: ${element}
		END
	ELSE
	    Element Should Not Be Visible           ${scr_index}
	    Pass Execution                          Screening questions with paragrapgh doesn't exist on the current page
	END

Validate screening questions: Upload File
	${status}=      Screening Questions Checker
	IF    ${status} == True
	    ${elements_upload_wrapper}=   Locators to list    ${scr_upload_wrapper}
	    FOR    ${element}    IN                 @{elements_upload_wrapper}
	        Wait Until Element Is Enabled       ${element}
	        ${type}=    Get Element Attribute   ${element}//input       accept
	        IF          '${type}'=='.pdf,.doc'
	            Element Should Contain          ${element}              Format file pdf, doc Max 2MB
	        ELSE IF     '${type}'=='.xlsx,.csv'
	            Element Should Contain          ${element}              Format file xlsx, csv Max 2MB
            ELSE IF     '${type}'=='.jpg,.jpeg,.png'
	            Element Should Contain          ${element}              Format file jpg, jpeg, png Max 2MB
            ELSE
                Fail    Unsupported file key detected
	        END
		END
	ELSE
	    Element Should Not Be Visible           ${scr_index}
	    Pass Execution  Screening questions with upload files doesn't exist on the current page
	END

Validate screening questions: Injecting File
	${status}=      Screening Questions Checker
	IF    ${status} == True
		${elements_doc}=    Locators to list        ${scr_upload_doc}
		FOR    ${element}    IN     @{elements_doc}
		    Inject file             ${element}      article.pdf
			Inject file             ${element}      article.doc
		END

		${elements_table}=    Locators to list      ${scr_upload_data_file}
		FOR    ${element}    IN     @{elements_table}
		    Inject file             ${element}      table.csv
			Inject file             ${element}      table.xlsx
		END

		${elements_image}=    Locators to list      ${scr_upload_image}
		FOR    ${element}    IN     @{elements_image}
		    Inject file             ${element}      images.jpg
			Inject file             ${element}      images.jpeg
			Inject file             ${element}      images.png
		END
	ELSE
	    Element Should Not Be Visible               ${scr_index}
	    Pass Execution              Screening questions with upload files doesn't exist on the current page
	END

Validate apply button
	[Setup]     Go To       ${URL_screening}
	Wait Until Element Is Enabled   ${apply_btn}
	Element Text Should Be          ${apply_btn}    Lamar Sekarang
	Wait Until Keyword Succeeds    2x    5s         Click Button        ${apply_btn}
#	Wait Until Location Is Not    ${URL_screening}
