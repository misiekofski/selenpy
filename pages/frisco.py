from time import sleep

from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FriscoPage(BasePage):
    POPUP_MODAL = (By.CSS_SELECTOR, 'div.fixed-popup a.close')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'div.buttons-group.higher a.cta')
    EMAIL_INPUT = (By.CSS_SELECTOR, '[name=username]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[name=password]')
    BIG_LOGIN_BUTTON = (By.CSS_SELECTOR, 'input.button.cta.login')
    DELIVERY_DATE = (By.CSS_SELECTOR, 'div.date')

    CORONA_INFO = (By.CSS_SELECTOR, 'a.close')

    RESERVATION_MODAL = (By.CSS_SELECTOR, 'div.reservation-selector.checkout_box')

    DELIVERY_BUTTON = (By.CSS_SELECTOR, 'div.header_delivery-inner')
    NEW_RESERVATION = (By.CSS_SELECTOR, 'div.button.with-chevron')
    FREE_DATES = (By.CSS_SELECTOR, 'div.calendar_column-day.available')
    SWITCH_TO_ENGLISH = (By.CSS_SELECTOR, 'div.ribbon-message.ribbon-__language button')
    SAVE_DATE = (By.CSS_SELECTOR, 'div.button.higher.cta')

    def close_modal(self):
        popup = self.driver.find_element(*self.POPUP_MODAL)
        popup.click()

    def login(self, user, password):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        email = self.driver.find_element(*self.EMAIL_INPUT)
        email.send_keys(user)
        password_element = self.driver.find_element(*self.PASSWORD_INPUT)
        password_element.send_keys(password)
        finish_login = self.driver.find_element(*self.BIG_LOGIN_BUTTON)
        finish_login.click()
        sleep(5)

        try:
            english = self.driver.find_element(*self.SWITCH_TO_ENGLISH)
            english.click()
        except:
            print("No switch to english button")

        try:
            corona = self.driver.find_element(*self.CORONA_INFO)
            corona.click()
        except:
            print("No coronavirus modal present")

    def check_delivery_date(self):
        sleep(5)
        delivery = self.driver.find_element(*self.DELIVERY_DATE)
        return delivery.text

    def reserve_delivery(self):
        self.driver.find_element(*self.DELIVERY_BUTTON).click()
        sleep(2)
        self.driver.find_element(*self.NEW_RESERVATION).click()
        sleep(2)

        first_free_date = self.driver.find_element(*self.FREE_DATES)
        self.driver.execute_script("arguments[0].scrollIntoView();", first_free_date)
        first_free_date.click()

        save_date = self.driver.find_element(*self.SAVE_DATE)
        self.driver.execute_script("arguments[0].scrollIntoView();", save_date)
        save_date.click()

        sleep(5)
