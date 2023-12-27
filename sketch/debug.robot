*** Settings ***
Library     String
Library     Process
Library     SeleniumLibrary
Library     RequestsLibrary
Library     OperatingSystem
Library     json
Library     Collections

*** Keywords ***
Get account
    [Documentation]    Returns the function as dictionary from reading the json file from credentials.json
    ...    The returned data will having value like this: {'email':'test@email.com', 'password': 'account password'}
	
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

Read JSON data
    [Documentation]    Returns the function as reading json file from the url_routing data
    
    ${raw_data}=       Get File    resources/data/base_url_routing.json
    ${json}=           Evaluate    json.loads('''${raw_data}''')
    [Return]           ${json}

Retrieve base URL
    [Documentation]    Returns the function as url string (https://staging.karirlab.co/admin)
    ...    "page": contain the main page you choose (karirlab, employers, etc),
    ...    "env": Selected environment (prod, staging, dev, etc),\n 
    ...    "type": only contain admin/user
    
    [Arguments]    ${page}    ${env}    ${type}
    ${source}    Read JSON data
    FOR    ${base_page}    IN    @{source}
        FOR    ${selected_page}    IN    ${base_page}
            ${page_name}    ${page_data}    Get Dictionary Items    ${selected_page}
            IF  '${page_name}' == '${page}'
                FOR    ${item}    IN    ${base_page}[${page}]
                    FOR    ${comps}    IN    @{item}
                        ${env_keyword}    ${env_content}        Get Dictionary Items   ${comps}
                        IF  '${env_keyword}' == '${env}'
                            ${selected_env}=    Set Variable       ${comps}[${env_keyword}]
                            FOR  ${page_type}  IN  @{selected_env}
                                ${url_type}    ${url_value}    Get Dictionary Items    ${page_type}
                                IF  '${url_type}' == '${type}'
                                    RETURN    ${url_value}
                                ELSE
                                    Continue For Loop
                                END
                            END
                            BREAK
                        ELSE
                            Continue For Loop
                        END
                    END
                END
            ELSE
                Exit For Loop
            END
        END
    END




*** Test Cases ***
Validate retrieved account
    ${account_super}    Get account    super_admin
    ${account_admin}    Get account    admin
    ${account_normal}   Get account    normal
    Log        ${account_super}
    Log        ${account_admin}
    Log        ${account_normal}

Validate URL routing
    ${result}    Retrieve base URL    karirlab    staging    user
    Should Match    https://staging.karirlab.co/    ${result}
    