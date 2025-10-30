Feature: Delete a note

  Scenario: Successfully delete a note by valid ID
    Given I have created a note
    When I send a request to delete the note by its ID
    Then the response status code should be 200
    And the response should confirm deletion

  Scenario: Fail to delete a note by invalid ID
    When I send a request to delete a note with ID 999999
    Then the response status code should be 404