*** Keywords ***
Enter Username
    [Arguments]     ${USERNAME}
    Input Text      ${FIELD_USERNAME}       ${USERNAME}

Enter Password
    [Arguments]     ${PASSWORD}
    Input Text      ${FIELD_PASSWORD}       ${PASSWORD}

Submit The Form
    Click Button        ${BTN_SUBMIT}

Fill Login Form
    [Arguments]    ${USERNAME}    ${PASSWORD}
    Enter Username    ${USERNAME}
    Enter Password    ${PASSWORD}
    Submit The Form



*** Variables ***
${FIELD_USERNAME}       xpath=//*[@id='username']
${FIELD_PASSWORD}       xpath=//*[@id='password']
${BTN_SUBMIT}       xpath=//*[@id='submit']

