from selenium.webdriver.common.by import By


TOTAL_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
TOTAL_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

IN_WORK_LIST = (
    By.XPATH,
    "//p[text()='В работе:']/following-sibling::ul[1]"
)
