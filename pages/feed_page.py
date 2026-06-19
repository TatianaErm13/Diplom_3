from pages.base_page import BasePage
from locators.feed_page_locators import *


class FeedPage(BasePage):

    def get_total_all_time(self):
        return self.get_text(TOTAL_ALL_TIME)

    def get_total_today(self):
        return self.get_text(TOTAL_TODAY)

    def get_orders_in_work(self):
        return self.get_text(IN_WORK_LIST)
    