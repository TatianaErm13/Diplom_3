from selenium.webdriver.common.by import By


class FeedPageLocators:

    FEED_BUTTON = (
        By.XPATH,
        "//a[contains(@href, '/feed')]"
    )

    FEED_CONTAINER = (
        By.CSS_SELECTOR,
        ".OrderFeed_ordersData__1L6Iv"
    )
    
    TOTAL_ALL_TIME = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )

    TOTAL_TODAY = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )