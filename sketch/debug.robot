*** Settings ***
Library     String
Library     Process
Library     SeleniumLibrary
Library     RequestsLibrary
Library     OperatingSystem
Library     json
Library     Collections

*** Variables ***
${feature}    karirlab
${env}        staging
${type}       user
${page}       job


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
    [Documentation]    Returns the function as reading json data from the given json files

    [Arguments]        ${file_name}
    ${raw_data}=       Get File    resources/data/${file_name}
    ${json}=           Evaluate    json.loads('''${raw_data}''')
    [Return]           ${json}

Retrieve base URL
    [Documentation]    Returns the function as url string (https://staging.karirlab.co/admin)
    ...    "page": contain the main page you choose (karirlab, employers, etc),
    ...    "env": Selected environment (prod, staging, dev, etc),\n 
    ...    "type": only contain admin/user
    
    [Arguments]    ${feature}    ${env}    ${type}
    ${source}    Read JSON data     base_url_routing.json
    FOR    ${base_page}    IN    @{source}
        FOR    ${selected_page}    IN    ${base_page}
            ${page_name}    ${page_data}    Get Dictionary Items    ${selected_page}
            IF  '${page_name}' == '${feature}'
                FOR    ${item}    IN    ${base_page}[${feature}]
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

Retrieve path URL
    [Documentation]    Returns the url path based on declaration under path_routing.json
    [Arguments]    ${feature}    ${type}    ${page}
    ${source}        Read JSON data    path_routing.json
    FOR  ${item}  IN  @{source}
        ${feature_name}    ${feature_routes}    Get Dictionary Items    ${item}
        IF  '${feature_name}' == '${feature}'
            FOR  ${page_name}  IN  @{feature_routes}
                ${page_mode}    ${mode_value}    Get Dictionary Items    ${page_name}
                IF  '${page_mode}' == '${type}'
                    FOR  ${page_path}  IN  @{mode_value}
                        ${path_name}    ${path_value}    Get Dictionary Items    ${page_path}
                        IF  '${path_name}' == '${page}'
                            Log    ${path_value}
                            RETURN    ${path_value}
                            BREAK
                        END
                    END
                END
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
    ${stg_user}    Retrieve base URL    karirlab    staging    user
    Should Match    https://staging.karirlab.co/    ${stg_user}

    ${stg_admin}    Retrieve base URL    karirlab    staging    admin
    Should Match    https://staging.karirlab.co/admin    ${stg_admin}

Validate URL path
    Retrieve path URL    karirlab    admin    resume_builder

Validate URL combination
    ${base}    Retrieve base URL    ${feature}    ${env}    ${type}
    ${path}    Retrieve path URL    ${feature}    ${type}    ${page}
    Should Match   https://staging.karirlab.co/job         ${base}${path}
    