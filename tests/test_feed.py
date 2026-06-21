import allure
from pages.feed_page import FeedPage


class TestFeed:

    @allure.title("Открытие ленты заказов")
    def test_open_feed(self, driver):
        page = FeedPage(driver)
        page.open_feed()
        assert page.is_feed_opened()

    @allure.title("Проверка счетчиков заказов")
    def test_counters(self, driver):
        page = FeedPage(driver)

        page.open_feed()
        page.wait_feed_loaded()

        assert int(page.get_total_all_time()) > 0
        assert int(page.get_total_today()) > 0