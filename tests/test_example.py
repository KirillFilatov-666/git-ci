import os
import allure
import pytest
from dotenv import load_dotenv

load_dotenv()


@allure.epic("Example")
@allure.feature("Example")
@pytest.mark.usefixtures("driver")   # фиксируем драйвер на класс
class TestExample:

    @pytest.mark.smoke
    @allure.title("Test Example")
    def test_example(self):          # ❌ убираем driver из аргументов
        with allure.step("Open page"):
            self.driver.get(os.environ["STAGE"])
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    @pytest.mark.regression
    @allure.title("Test Example 2")
    def test_example_2(self):        # ❌ убираем driver из аргументов
        with allure.step("Open page"):
            self.driver.get(os.environ["STAGE"])
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
