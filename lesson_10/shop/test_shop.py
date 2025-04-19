import allure
import pytest
from selenium import webdriver


from AutorizationPage import AutorizationPage
from AddItems import AddItems
from AddCart import AddCart
from CheckoutInfo import CheckoutInfo
from AssertTotal import AssertTotal


@allure.title("Тест на проверку работы интернет-магазина")
@allure.feature("Shop")
@allure.description("Проверка работы интернет-магазина на авторизацию, добавление товаров в корзину, оформление заказа и итоговую стоимость")
@allure.severity("critical")
@pytest.fixture
def initial_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_fill_shop():
    driver = webdriver.Chrome()
    autorization_page = AutorizationPage(driver)
    with allure.step("Авторизоваться на сайте"):
        autorization_page.fill_login(
        user_name="standard_user",
        password="secret_sauce"
    )
    with allure.step("Добавить товары в корзину"):
        add_items = AddItems(driver)
        add_items.add_items()
    with allure.step("Перейти в корзину"):
        add_cart = AddCart(driver)
        add_cart.cart()
    with allure.step("Заполнить своими данными страницу оформления заказа"):
        checkout_info = CheckoutInfo(driver)
        checkout_info.checkout(
        first_name="Татьяна",
        last_name="Денисова",
        code="603123"
    )
    with allure.step("Получить и проверить итоговую стоимость"):
        assert_total = AssertTotal(driver)
        assert_total.total()
