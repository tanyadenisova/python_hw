import pytest
from selenium import webdriver

from FormPage import FormPage
from ValidatePage import ValidatePage


@pytest.fixture
def initial_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_fill_form():
    driver = webdriver.Chrome()
    form_page = FormPage(driver)
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
    validate_page.allert_color()
    validate_page.check()
