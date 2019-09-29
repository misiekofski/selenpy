import behave_webdriver
import pyderman as driver


def before_all(context):
    path = driver.install(browser=driver.chrome)
    context.behave_driver = behave_webdriver.Chrome(path)
    context.behave_driver.implicitly_wait(5)
    context.behave_driver.maximize_window()


def after_all(context):
    context.behave_driver.quit()
