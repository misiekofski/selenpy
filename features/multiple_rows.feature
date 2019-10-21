Feature: Table usage example for dynamic rows

  Scenario: Add multiple users for the table
    Given I open the site "https://bootsnipp.com/snippets/402bQ"
    When I add users for the table
        | name     | mail             | phone        |
        | Jan      | Kowalski         | +48666666666 |
        | Zbigniew | Woodecki         | +48123456789 |
        | King     | Of the Internetz | +48987654321 |


  Scenario: Add multiple users for the table
    Given I open the site "https://bootsnipp.com/snippets/402bQ"
    When I add user with name "Jan", surname "Kowalski" and phone "+48666666666"
    And I add user with name "Zbigniew", surname "Woodecki" and phone "+48123456789"
    And I add user with name "King", surname "Of the Internetz" and phone "+48987654321"