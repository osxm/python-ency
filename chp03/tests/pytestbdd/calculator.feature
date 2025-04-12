Feature: Calculator Feature

  Scenario: Adding two numbers
    Given I have a calculator
    When I add 2 and 5
    Then the result should be 7