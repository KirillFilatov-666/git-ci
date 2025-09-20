import os
import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()