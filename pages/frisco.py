from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FriscoPage(BasePage):
    POPUP_MODAL = (By.CSS_SELECTOR, 'div.fixed-popup a.close')

    def close_modal(self):
        popup = self.driver.find_element(*self.POPUP_MODAL)
        popup.click()
