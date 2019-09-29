from behave_webdriver.steps import *
from pages.google_page import GooglePage


@when('I search by feeling lucky for phrase "{phrase}"')
def feeling_lucky_search(context, phrase):
    google = GooglePage(context.behave_driver)
    google.feeling_lucky_search(phrase)


@then('I am redirected to other site than "{expected_url}"')
def check_that_url_is_other_than_expected(context, expected_url):
    assert context.behave_driver.current_url != expected_url
