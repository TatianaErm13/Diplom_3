from selenium.webdriver.common.by import By


CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']")

INGREDIENT = (By.CLASS_NAME, "BurgerIngredient_ingredient__1TVf6")
MODAL = (By.CLASS_NAME, "Modal_modal__P3_V5")
MODAL_CLOSE = (By.CLASS_NAME, "Modal_modal__close__TnseK")

COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")

ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
