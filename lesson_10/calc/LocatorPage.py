import allure
from selenium.webdriver.common.by import By


class LocatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Очистить поле ввода") 
    def clear(self):
        self.driver.find_element(By.ID, "delay").clear()

    @allure.step("Ввести значение в поле ввода")
    def fill_locator(self, keys):
        self.driver.find_element(By.ID, "delay").send_keys(keys)
  