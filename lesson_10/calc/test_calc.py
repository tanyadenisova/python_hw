import allure
import pytest
from selenium import webdriver

from LocatorPage import LocatorPage
from ExamplePage import ExamplePage


@pytest.fixture
def initial_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тест на проверку работы калькулятора")
@allure.feature("Calculator")
@allure.description("Проверка работы калькулятора, сравнение полученного результата вычисления с действительным значением")
@allure.severity("critical")
def test_calc():
    with allure.step("Открыть страницу калькулятора по ссылке"):
        driver = webdriver.Chrome()
    with allure.step("Очистить поле ввода"):
        locator_page = LocatorPage(driver)
        locator_page.clear()
    with allure.step("Ввести значение в поле ввода"):
        locator_page.fill_locator(45)

    example_page = ExamplePage(driver)
    with allure.step("Заполнить пример"):
        example_page.fill_example()
    with allure.step("Ожидание результата"):
        example_page.wait()
    with allure.step("Проверка полученного результата"):
        example_page.assert_response()
