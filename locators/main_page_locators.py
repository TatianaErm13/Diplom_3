from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TAB = (By.LINK_TEXT, "Конструктор")

    INGREDIENT = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6")

    MODAL_CONTENT = (By.CSS_SELECTOR, "[class*='Modal_modal__content']")

    MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "button[class*='Modal_modal__close']"
    )
    
    CREATE_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Оформить заказ']"
    )

    CONSTRUCTOR_AREA = (
        By.CSS_SELECTOR,
        "ul.BurgerConstructor_basket__list__l9dp_"
    )
    ORDER_MODAL = (By.XPATH, "//*[contains(text(),'Ваш заказ начали готовить')]")

    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")

    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")

    ORDER_SUCCESS_LOCATOR = (By.XPATH, "//*[contains(text(),'Ваш заказ начали готовить')]")