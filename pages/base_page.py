from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def fill_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def wait_overlay_disappear(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                (By.CSS_SELECTOR, "[class*='Modal_modal__overlay']")
            )
        )

    def press_escape(self):
        self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
    
