Feature: Check search functionality on google home page

  Scenario: Check I'm feeling lucky search functionality
    Given I open the site "https://www.google.com"
    When I search by feeling lucky for phrase "Selenium"
    Then I am redirected to other site than "https://www.google.com"
    
    
  Scenario Outline: Check that google search shows some results
    Given I open the site "https://www.google.com"
    When I search with normal search for phrase <search_phrase>
    Then Results count is more than <results_count>
    Examples:
    | search_phrase|results_count |
    | Selenium               | 10 |
    | NU@#%(*DGNS%#SFDIUBW#% | 3  |
    | pinasdgoinasdgoinasdg  | -1 |