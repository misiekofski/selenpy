from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class GooglePage(BasePage):
    SEARCH_INPUT = (By.NAME, 'q')
    FEELING_LUCKY = (By.NAME, 'btnI')

    def feeling_lucky_search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        feeling_lucky = self.driver.find_element(*self.FEELING_LUCKY)
        feeling_lucky.click()
