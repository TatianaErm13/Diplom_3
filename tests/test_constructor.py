import allure
from pages.main_page import MainPage


@allure.title("Переход в Конструктор")
def test_constructor(driver):
    page = MainPage(driver)

    page.open_feed()
    page.open_constructor()

    assert driver.current_url == "https://stellarburgers.education-services.ru/"

@allure.title("Открытие и закрытие модального окна")
def test_modal(driver):
    page = MainPage(driver)

    page.click_ingredient()

    assert page.is_modal_opened()

    page.close_modal()

@allure.title("Увеличение счетчика ингредиента")
def test_counter(driver):
    page = MainPage(driver)

    before = page.get_counter()
    page.click_ingredient()
    after = page.get_counter()

    assert after >= before
    