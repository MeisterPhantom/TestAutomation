# Created by meisterphantom at 28/8/23
Feature: Demoqa Books Functionality

  As a user of the demoqa portal
  I search for a book on the demoqa books page,
  validate that it is the book
  I am looking for and add it to my collection.

  Background:
    Given the demoqa page is displayed
    When I select the section "Book Store Application"
    And I select the option "Login"
    And I fill the login form with "ivanocampo", "Ivanocampo1!"

  Scenario Outline: Validate the nickname of user, after login
    Then I show the profile of user, with the "<username>"
    And logout account
    Examples:
      | username   |
      | ivanocampo |

  Scenario: Add a book to the list
    # When I select the section "Book Store Application"
    When I select the option "Profile"
    And I select the book "You Dont Know JS"
    Then I show the information of the book
    And Add to the collection

  Scenario: Validate the user contains a book list
    When I select the section "Book Store Application"
    And I select the option "Profile"
    Then I show the list of the books associated to the account

  Scenario: Delete a book from the list
    When I select the section "Book Store Application"
    And I select the option "Profile"
    Then I delete the book

  Scenario: Look for a book that doesn't exists
    When I select the section "Book Store Application"
    And I search ".."
    Then I show the list of the books that concord with the search