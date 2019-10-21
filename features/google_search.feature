Feature: Check search functionality on google home page
    
  Scenario Outline: Check that google search shows some results
    Given I open the site "https://www.google.com"
    When I search with normal search for phrase <search_phrase>
    Then Results count is more than <results_count>
    Examples:
    | search_phrase|results_count |
    | Selenium               | 9  |
    | NU@#%(*DGNS%#SFDIUBW#% | 3  |
    | pinasdgoinasdgoinasdg  | -1 |


  Scenario: Check that google search shows some results
    Given I open the site "https://www.google.com"
    When I search with normal search for phrase Selenium
    Then Results count is more than 9
    When I search with normal search for phrase NU@#%(*DGNS%#SFDIUBW#%
    Then Results count is more than 3
    When I search with normal search for phrase pinasdgoinasdgoinasdg
    Then Results count is more than -1