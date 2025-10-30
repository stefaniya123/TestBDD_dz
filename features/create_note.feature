Feature: Create a note

  Scenario: Successfully create a note with valid data
    Given I have a valid note payload
    When I send a request to create the note
    Then the response status code should be 200
    And the response should contain the correct title and content

  Scenario: Fail to create a note with invalid data (missing title)
    Given I have an invalid note payload missing "title"
    When I send a request to create the note
    Then the response status code should be 422