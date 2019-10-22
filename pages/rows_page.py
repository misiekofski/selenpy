from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RowsPage(BasePage):
    ADD_ROW_BUTTON = (By.ID, 'addrow')
    NAME_INPUT = (By.XPATH, '//input[contains(@name, "name")]')
    MAIL_INPUT = (By.XPATH, '//input[contains(@name, "mail")]')
    PHONE_INPUT = (By.XPATH, '//input[contains(@name, "phone")]')
    IFRAME_LOCATOR = (By.ID, 'snippet-preview')

    def switch_to_iframe(self):
        iframe = self.driver.find_element(*self.IFRAME_LOCATOR)
        self.driver.switch_to.frame(iframe)

    def enter_user(self, name, mail, phone):
        self.driver.find_elements(*self.NAME_INPUT)[-1].send_keys(name)
        self.driver.find_elements(*self.MAIL_INPUT)[-1].send_keys(mail)
        self.driver.find_elements(*self.PHONE_INPUT)[-1].send_keys(phone)

    def add_row(self):
        self.driver.find_element(*self.ADD_ROW_BUTTON).click()
