Feature: Reserve frisco delivery

  Scenario: Reserve first time available for frisco
    Given I open the site "https://www.frisco.pl"
    When I close popup modal
    And Login to website
    Then I check nearest delivery date