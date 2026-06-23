import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from constants import LOGIN_URL, EMAIL, PASSWORD
from locators.main_page_locators import MainPageLocators

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


    @allure.title("При создании заказа увеличивается счетчик за все время")
    def test_total_all_time_counter_increased(self, driver):

        feed = FeedPage(driver)

        feed.open_feed()
        feed.wait_feed_loaded()

        before = int(feed.get_total_all_time())

        driver.get(LOGIN_URL)
        LoginPage(driver).login(EMAIL, PASSWORD)

        main = MainPage(driver)

        main.add_ingredient_to_constructor()
        main.add_ingredient_to_constructor()

        main.create_order()

        main.wait_order_modal_opened()
        main.wait_order_success()
        main.wait_order_number_loaded()

        order_number = main.get_order_number()
        print("Номер заказа:", order_number)

        main.close_order_modal()

        feed.open_feed()
        feed.wait_feed_loaded()
        
        feed.wait_feed_updated(before)

        after = int(feed.get_total_all_time())

        assert after > before


    @allure.title("При создании заказа увеличивается счетчик за сегодня")
    def test_total_today_counter_increased(self, driver):

        feed = FeedPage(driver)

        feed.open_feed()
        feed.wait_feed_loaded()

        before = int(feed.get_total_today())

        driver.get(LOGIN_URL)
        LoginPage(driver).login(EMAIL, PASSWORD)

        main = MainPage(driver)

        main.open_constructor()
        main.add_ingredient_to_constructor()
        main.add_ingredient_to_constructor()

        main.create_order()

        main.wait_order_modal_opened()
        main.wait_order_success()
        main.wait_order_number_loaded()

        order_number = main.get_order_number()
        print("Номер заказа:", order_number)

        main.close_order_modal()

        feed.open_feed()
        feed.wait_feed_loaded()

        WebDriverWait(driver, 20).until(
            lambda d: int(feed.get_total_today()) > before
        )

        after = int(feed.get_total_today())

        assert after > before
    
    @allure.title("При создании заказа увеличивается счетчик за сегодня")
    def test_total_today_counter_increased(self, driver):

        feed = FeedPage(driver)

        feed.open_feed()
        feed.wait_feed_loaded()

        before = int(feed.get_total_today())

        driver.get(LOGIN_URL)
        LoginPage(driver).login(EMAIL, PASSWORD)

        main = MainPage(driver)

        main.open_constructor()
        main.add_ingredient_to_constructor()
        main.add_ingredient_to_constructor()

        main.create_order()

        main.wait_order_modal_opened()
        main.wait_order_success()
        main.wait_order_number_loaded()

        order_number = main.get_order_number()
        print("Номер заказа:", order_number)

        main.close_order_modal()

        feed.open_feed()
        feed.wait_feed_loaded()

        feed.wait_feed_updated(before)

        after = int(feed.get_total_today())

        assert after > before


    @allure.title("После оформления заказа номер появляется в разделе В работе")
    def test_order_appears_in_work(self, driver):

        driver.get(LOGIN_URL)
        LoginPage(driver).login(EMAIL, PASSWORD)

        main = MainPage(driver)

        main.open_constructor()
        main.add_ingredient_to_constructor()
        main.add_ingredient_to_constructor()

        main.create_order()

        main.wait_order_modal_opened()
        main.wait_order_number_loaded()

        order_number = main.get_order_number()
        main.close_order_modal()

        feed = FeedPage(driver)
        feed.open_feed()
        feed.wait_feed_loaded()

        orders_in_work = feed.get_orders_in_work()

        assert order_number in orders_in_work
