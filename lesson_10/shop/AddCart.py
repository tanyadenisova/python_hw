import allure
from selenium.webdriver.common.by import By


class AddCart:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход в корзину")
    def cart(self):
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        self.driver.find_element(By.ID, "checkout").click()
