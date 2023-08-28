# Created by ivan at 15/6/23
Feature: demoqa portal

  As a user of the demoqa portal
  I want to review all sections and validate their correct operation

  Background:
    Given the demoqa page is displayed

  Scenario Outline: Validate and interact with the Elements section.
    When I select the section "Elements"
    And I select the option "Text Box"
    Then I fill the form with "<full_name>", "<email>", "<current_address>", and "<permanent_address>"
    And send the information

    Examples:
    | full_name        | email                        | current_address           | permanent_address         |
    | Pedrito Oscarin  | p.oscarin@fakemail.io        | calle soledad # 10 - 0    | calle soledad # 10 - 0    |

  Scenario: Validate the download file in the Elements section.
    When I select the section "Elements"
    And I select the option "Upload and Download"
    Then I download the file

  Scenario Outline: Validate and interact with the Forms section.
    When I select the section "Forms"
    And I select the option "Practice Form"
    Then I fill the form with "<first_name>", "<last_name>", "<email>", "<mobile>", "<date_of_birth>", "<subjects>", and "<current_address>"
    And I select the option gender "<gender>"
    And I select the option hobbies "<hobbies>"
    And save the data

    Examples:
    | first_name  | last_name  | email                     | gender | mobile       | date_of_birth | subjects             | current_address | hobbies |
    | Pedro       | Pascal     | Pascal.fake@email.com     | Male   | 3009990000   | 01/05/1990    | Aplicando a Pragma   | current_address | Sports  |

  Scenario: Validate the new tab in the Alerts, Frame & Windows section
    When I select the section "Alerts, Frame & Windows"
    And I select the option "Browser Windows"
    And I create a new tab
    Then the system shows the new tab with the message "This is a sample page"

  Scenario: Validate the modal dialogs in the Alerts, Frame & Windows section
    When I select the section "Alerts, Frame & Windows"
    And I select the option "Modal Dialogs"
    Then the system shows the new dialog with the message "This is a small modal. It has very less content"

  Scenario Outline: Validate incorrect login in the Book Store Application section
    When I select the section "Book Store Application"
    And I select the option "Login"
    And I fill the form with "<username>", "<password>"
    Then the system shows an error message "Invalid username or password!"

    Examples:
    | username  | password      |
    | sinpepito | sinpepinillos |