import pytest
from selenium import webdriver


from AutorizationPage import AutorizationPage
from AddItems import AddItems
from AddCart import AddCart
from CheckoutInfo import CheckoutInfo
from AssertTotal import AssertTotal


@pytest.fixture
def initial_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_fill_shop():
    driver = webdriver.Chrome()
    autorization_page = AutorizationPage(driver)
    autorization_page.fill_login(
        user_name="standard_user",
        password="secret_sauce"
    )
    add_items = AddItems(driver)
    add_items.add_items()
    add_cart = AddCart(driver)
    add_cart.cart()
    checkout_info = CheckoutInfo(driver)
    checkout_info.checkout(
        first_name="Анастасия",
        last_name="Ковалева",
        code="666671"
    )
    assert_total = AssertTotal(driver)
    assert_total.total()
