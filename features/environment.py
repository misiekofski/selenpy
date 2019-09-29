import behave_webdriver
import pyderman as driver

def before_all(context):
    path = driver.install(browser=driver.chrome)
    context.behave_driver = behave_webdriver.Chrome(path)


def after_all(context):
    context.behave_driver.quit()