from selenium.webdriver.common.by import By


class LocatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def clear(self):
        self.driver.find_element(By.ID, "delay").clear()

    def fill_locator(self, keys):
        self.driver.find_element(By.ID, "delay").send_keys(keys)
  