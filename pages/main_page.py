from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    def open_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_modal_closed()

    def is_modal_opened(self):
        elements = self.find_elements(MainPageLocators.MODAL_CONTENT)
        return any(e.is_displayed() for e in elements)

    def wait_modal_closed(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.MODAL_CONTENT
            )
        )

    def add_ingredient_to_constructor(self):
        ingredient = self.find(MainPageLocators.INGREDIENT)
        constructor = self.find(MainPageLocators.CONSTRUCTOR_AREA)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            const dragStartEvent = new DragEvent('dragstart', {
                dataTransfer: dataTransfer,
                bubbles: true
            });

            const dropEvent = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true
            });

            source.dispatchEvent(dragStartEvent);
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', {
                dataTransfer: dataTransfer,
                bubbles: true
            });

            source.dispatchEvent(dragEndEvent);
        """, ingredient, constructor)

    def create_order(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    def get_order_number(self):
        return self.wait.until(
            lambda d: self.get_text(MainPageLocators.ORDER_NUMBER).strip()
        )

    def close_order_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_overlay_disappear()

    def wait_order_success(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'Ваш заказ начали готовить')]")
            )
        )

    def wait_order_modal_opened(self):
        self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )

    def wait_order_number_loaded(self):
        self.wait.until(
            lambda d: self.get_text(MainPageLocators.ORDER_NUMBER).strip() not in ("", "9999")
        )

    def is_order_button_enabled(self):
        return self.find(
            MainPageLocators.CREATE_ORDER_BUTTON
        ).is_enabled()
    
