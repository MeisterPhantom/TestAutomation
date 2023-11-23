*** Keywords ***
Read Config Json
    ${json_data}=     Get File    ${EXECDIR}/config.json
    ${json}=    evaluate    json.loads('''${json_data}''')    json
    [return]  ${json}

Initialize Test Data
    ${json}=    Read Config Json
    set global variable  ${data}    ${json}

Configure Selenium
     Set Selenium Speed    .5 Seconds

Navigate To Homepage
    Open Browser    ${data['url_remote']}    ${data['browser']}
    Maximize Browser Window

Exit Selenium
    Capture Page Screenshot
    Close Browser
