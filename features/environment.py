import behave_webdriver
import pyderman as driver
import os

def before_all(context):
    context.path = driver.install(browser=driver.chrome)

def before_feature(context, feature):
    context.behave_driver = behave_webdriver.Chrome(executable_path = context.path)
    context.behave_driver.implicitly_wait(5)
    context.behave_driver.maximize_window()


def after_feature(context, feature):
    context.behave_driver.quit()
