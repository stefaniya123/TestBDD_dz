Feature: Get a note by ID

  Scenario: Get a note by valid ID
    Given I have created a note
    When I request the note by its ID
    Then the response status code should be 200
    And the response should contain the correct note data

  Scenario: Fail to get a note by invalid ID
    When I request a note with ID 999999
    Then the response status code should be 404