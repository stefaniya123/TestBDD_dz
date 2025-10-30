Feature: Get all notes

  Scenario: Get all notes when none exist
    When I request all notes
    Then the response status code should be 200
    And the response should be an empty list

  Scenario: Get all notes when some exist
    Given I have created a note
    When I request all notes
    Then the response status code should be 200
    And the response should contain at least one note