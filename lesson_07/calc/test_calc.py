import pytest
from selenium import webdriver

from LocatorPage import LocatorPage
from ExamplePage import ExamplePage


@pytest.fixture
def initial_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calc():
    driver = webdriver.Chrome()
    locator_page = LocatorPage(driver)
    locator_page.clear()
    locator_page.fill_locator(45)

    example_page = ExamplePage(driver)
    example_page.fill_example()
    example_page.wait()
    example_page.assert_response()
