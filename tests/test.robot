*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  Collections

Resource    ${CURDIR}/../src/pages/dashboard/dashboard.robot
Resource    ${CURDIR}/../src/pages/home/home.robot
Resource    ${CURDIR}/../src/pages/login/login.robot
Resource    ${CURDIR}/../src/pages/practice/practice.robot
Resource    ${CURDIR}/../configurations/config.robot

Suite Setup  Run Keywords   Initialize Test Data    Configure Selenium   Navigate To Homepage
Suite Teardown  Exit Selenium

*** Test Cases ***
Login Success
    Given The Page Are Loaded
    And Navigate To Practice
    And Navigate To Login
    When Fill Login Form    student     Password123
    Then Show The Login Success    Logged In Successfully

