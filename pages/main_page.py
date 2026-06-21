from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    def open_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    def close_modal(self):
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)

    def is_modal_opened(self):
        elements = self.driver.find_elements(*MainPageLocators.MODAL_CONTENT)
        return any(el.is_displayed() for el in elements)
    
    def wait_modal_closed(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                MainPageLocators.MODAL_CONTENT
            )
        )