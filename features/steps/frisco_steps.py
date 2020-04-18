from behave_webdriver.steps import *
from pages.frisco import FriscoPage
from behave import *


@step('I close popup modal')
def close_popup_modal(context):
    frisco = FriscoPage(context.behave_driver)
    frisco.close_modal()


@step('Login to website')
def login_to_website(context):
    frisco = FriscoPage(context.behave_driver)



@step('I check nearest delivery date')
def check_delivery_date(context):
    frisco = FriscoPage(context.behave_driver)
    termin = frisco.check_delivery_date()
    if "cze" in termin:
        print("Fucking czerwiec")
    if "kwi" in termin or "jutro" in termin:
        print("Success!")
        frisco.reserve_delivery()

