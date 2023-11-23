*** Keywords ***
Navigate To Practice
    Click Element       ${PRACTICE_LINK}

The Page Are Loaded
    Log To Console      Start The Test

*** Variables ***
${PRACTICE_LINK}        xpath=//li[@id="menu-item-20"]/a