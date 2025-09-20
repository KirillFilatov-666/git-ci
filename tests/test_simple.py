import allure
import pytest


@allure.epic("Simple Test")
@allure.feature("Basic")
@pytest.mark.regression
def test_simple():
    """Простой тест для проверки Allure"""
    with allure.step("Step 1: Assert True"):
        assert True
    
    with allure.step("Step 2: Check number"):
        result = 2 + 2
        assert result == 4
        
    allure.attach("Test data", name="Simple attachment", attachment_type=allure.attachment_type.TEXT)
