import allure
import pytest
from selenium import webdriver

from FormPage import FormPage
from ValidatePage import ValidatePage


@allure.title("Тест на проверку заполнения формы")
@allure.feature("FORM")
@allure.description("Проверка заполнения всех ячеек формы, подсвечивание красным, если не заполнено")
@allure.severity("critical")

@pytest.fixture
def initial_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_fill_form():
    with allure.step("Открыть страницу формы по ссылке"):
        driver = webdriver.Chrome()
    """Создание объекта страницы формы"""
    form_page = FormPage(driver)
    with allure.step("Заполнение фоормы данными"):
        form_page.fill_form(
            first_name="Иван",
            last_name="Петров",
            address="Ленина, 55-3",
            email="test@skypro.com",
            phone="+7985899998787",
            city="Москва",
            country="Россия",
            job="QA",
            company="SkyPro")

    validate_page = ValidatePage(driver)
    with allure.step("Проверка цвета границ полей"):
        validate_page.allert_color()
        validate_page.check()
