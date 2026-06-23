from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait

class FeedPage(BasePage):

    def open_feed(self):
        self.click(FeedPageLocators.FEED_BUTTON)

    def wait_feed_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(FeedPageLocators.FEED_CONTAINER)
        )

    def is_feed_opened(self):
        return self.driver.current_url.endswith("/feed")

    def get_total_all_time(self):
        return self.get_text(FeedPageLocators.TOTAL_ALL_TIME)

    def get_total_today(self):
        return self.get_text(FeedPageLocators.TOTAL_TODAY)

    def get_orders_in_work(self):
        return self.get_text(FeedPageLocators.IN_WORK_LIST)
    
    def wait_feed_updated(self, before_value):
        self.wait.until(
            lambda d: int(self.get_total_all_time()) > before_value
        )
    
    def wait_feed_updated(self, previous_value: int, timeout: int = 15):
        
        WebDriverWait(self.driver, timeout).until(
            lambda d: int(self.get_total_all_time()) > previous_value
        )