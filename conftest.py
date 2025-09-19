import pytest
import requests
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    options.add_argument(
        "--disable-dev-shm-usage"
    )

    driver = webdriver.Chrome(options=options)
    requests.cls.driver = driver
    yield driver
    driver.quit()

