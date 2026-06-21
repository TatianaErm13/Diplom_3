import allure
from pages.main_page import MainPage


class TestConstructor:

    @allure.title("Переход в конструктор")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.open_constructor()

        assert page.get_current_url() == "https://stellarburgers.education-services.ru/"

    @allure.title("Открытие модального окна ингредиента")
    def test_open_modal(self, driver):
        page = MainPage(driver)
        page.wait_overlay_disappear()
        page.open_ingredient()
        assert page.is_modal_opened()

    @allure.title("Закрытие модального окна")
    def test_close_modal(self, driver):
        page = MainPage(driver)

        page.open_ingredient()
        page.close_modal()
        page.wait_modal_closed()

        assert not page.is_modal_opened()
        