# Created by ivan at 28/5/23
Feature: Google search
  As a user
  I want to search anything into the browser

  Scenario: Search in google
    # Enter steps here
  Given the browser has in "google.com"
    When search "Any word"
    Then the browser show all results
    And validate the results be maior than zero