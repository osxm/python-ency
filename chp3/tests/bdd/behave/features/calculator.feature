Feature: Addition
  Scenario: Add two numbers
    Given I have a calculator
    When I enter "1" and "2"
    Then the result should be "3"