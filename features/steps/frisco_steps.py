from behave_webdriver.steps import *
from pages.frisco import FriscoPage
from behave import *


@step('I close popup modal')
def close_popup_modal(context):
    frisco = FriscoPage(context.behave_driver)
    frisco.close_modal()
