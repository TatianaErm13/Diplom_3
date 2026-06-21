from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TAB = (By.LINK_TEXT, "Конструктор")

    INGREDIENT = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__1TVf6")

    MODAL_CONTENT = (By.CSS_SELECTOR, "[class*='Modal_modal__content']")

    MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "button[class*='Modal_modal__close']"
    )
    