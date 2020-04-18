import datetime
import random
from time import sleep

from behave_webdriver.steps import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    while "jutro" not in termin or "kwi" not in termin:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"{now} : fucking {termin}")
        context.behave_driver.refresh()
        tout = random.randint(63,92)
        sleep(tout)
        termin = frisco.check_delivery_date()

    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{now} : Success - reserved delivery date!")

    frisco.reserve_delivery()

    context.behave_driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    play_button = (By.CSS_SELECTOR, 'button.ytp-large-play-button.ytp-button')
    context.behave_driver.get("https://www.youtube.com/watch?v=w0AOGeqOnFY")
    context.behave_driver.find_element(*play_button).click()
    sleep(300)
