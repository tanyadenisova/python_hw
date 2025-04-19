import allure
from selenium.webdriver.common.by import By


class CheckoutInfo:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверка информации о заказчике")
    def checkout(self, first_name, last_name, code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(code)
        self.driver.find_element(By.ID, "continue").click()
