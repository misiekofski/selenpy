Feature: Check search functionality on google home page
    
  Scenario Outline: Check that google search shows some results
    Given I open the site "https://www.google.com"
    When I search with normal search for phrase <search_phrase>
    Then Results count is more than <results_count>

    Examples:
    | search_phrase|results_count |
    | Selenium               | 7  |
    | Piwko                  | 3  |
    | pinasdgoinasdgoinasdg  | -1 |