import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    user_name = driver.find_element(By.NAME, "user-name")
    user_name.send_keys("standard_user")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    driver.find_element(By.NAME, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    driver.find_element(By.ID, "checkout").click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Анастасия")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Ковалева")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("666671")

    driver.find_element(By.ID, "continue").click()

    total_price = driver.find_element(By.XPATH, "//div[@class='summary_total_label']").text

    driver.quit()

    assert total_price == "Total: $58.29"
