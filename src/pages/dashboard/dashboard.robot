*** Keywords ***
Show The Login Success
    [Arguments]     ${MESSAGE_SUCCESS_LOGIN}
    ${GET_MESSAGE}=     Get Text    ${LABEL_SUCCESS}
    BuiltIn.Should Be Equal As Strings      ${GET_MESSAGE}       ${MESSAGE_SUCCESS_LOGIN}
*** Variables ***
${LABEL_SUCCESS}        xpath=*//h1[@class='post-title']