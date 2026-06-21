import pytest
from selenium import webdriver
from constants import BASE_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.get(BASE_URL)

    yield driver

    driver.quit()
    