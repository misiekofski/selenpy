import time

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GooglePage(BasePage):
    SEARCH_INPUT = (By.NAME, 'q')
    FEELING_LUCKY = (By.NAME, 'btnI')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    RESULTS_LIST = (By.XPATH, '//h3[contains(@class, "LC20lb")]')
    AGREE_POPUP = (By.XPATH, '//*[@id="introAgreeButton"]/span/span')
    IFRAME = (By.XPATH, '//iframe')
    ACCEPT_ALL = (By.ID, 'L2AGLb')

    def accept_agreement(self):
        try:
            self.driver.find_element(*self.ACCEPT_ALL).click()
        except NoSuchElementException:
            pass

    def feeling_lucky_search(self, phrase):
        self.accept_agreement()
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_input.send_keys(Keys.ESCAPE)
        feeling_lucky = self.driver.find_elements(*self.FEELING_LUCKY)
        feeling_lucky[1].click()

    def normal_search(self, phrase):
        self.accept_agreement()
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_input.send_keys(Keys.ENTER)

    def return_results_count(self):
        try:
            results_list = self.driver.find_elements(*self.RESULTS_LIST)
            return len(results_list)
        except:
            return 0