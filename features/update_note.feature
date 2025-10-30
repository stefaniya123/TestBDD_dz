Feature: Update a note

  Scenario: Successfully update a note by valid ID
    Given I have created a note
    And I have an updated note payload
    When I send a request to update the note by its ID
    Then the response status code should be 200
    And the response should contain the updated title and content

  Scenario: Fail to update a note by invalid ID
    Given I have an updated note payload
    When I send a request to update a note with ID 999999
    Then the response status code should be 404