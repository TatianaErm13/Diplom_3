import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.title("Переход в Ленту заказов")
def test_feed_navigation(driver):
    page = MainPage(driver)

    page.open_feed()
    assert "feed" in driver.current_url


@allure.title("Проверка счетчиков в ленте")
def test_feed_counters(driver):
    main_page = MainPage(driver)
    main_page.open_feed()

    page = FeedPage(driver)

    assert int(page.get_total_all_time()) > 0
    assert int(page.get_total_today()) > 0


@allure.title("Заказ появляется в работе")
def test_order_in_work(driver):
    main_page = MainPage(driver)
    main_page.open_feed()

    page = FeedPage(driver)

    orders = page.get_orders_in_work()
    assert len(orders.split()) > 0
