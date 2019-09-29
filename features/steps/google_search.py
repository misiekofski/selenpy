from behave_webdriver.steps import *
from pages.google_page import GooglePage
from behave import *


@step('I search by feeling lucky for phrase "{phrase}"')
def feeling_lucky_search(context, phrase):
    google = GooglePage(context.behave_driver)
    google.feeling_lucky_search(phrase)


@step('I am redirected to other site than "{expected_url}"')
def check_that_url_is_other_than_expected(context, expected_url):
    assert context.behave_driver.current_url != expected_url


@step('I search with normal search for phrase {search_phrase}')
def normal_search(context, search_phrase):
    google = GooglePage(context.behave_driver)
    google.normal_search(search_phrase)


@step('Results count is more than {results_count:n}')
def check_results_count(context, results_count):
    google = GooglePage(context.behave_driver)
    print ('results count: ' + str(google.return_results_count()))
    assert google.return_results_count() > results_count
