Feature: Check search functionality on google home page

  Scenario: Check I'm feeling lucky search functionality
    Given I open the site "https://www.google.com"
    When I search by feeling lucky for phrase "Selenium"
    Then I am redirected to other site than "https://www.google.com"