from pages.base_page import BasePage
from locators.main_page_locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    def open_constructor(self):
        self.click(CONSTRUCTOR_TAB)

    def open_feed(self):
        self.click(FEED_TAB)

    def click_ingredient(self):
        self.click(INGREDIENT)

    def close_modal(self):
        self.click(MODAL_CLOSE)

    def is_modal_opened(self):
        return self.is_visible(MODAL)

    def wait_modal_closed(self):
        self.wait.until(
            EC.invisibility_of_element_located(MODAL)
        )

    def get_counter(self):
        return self.get_text(COUNTER)

    def create_order(self):
        self.click(ORDER_BUTTON)

    def open_feed(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
            )
        )
        self.click(FEED_TAB)