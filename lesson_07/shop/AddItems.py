from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddItems:

    def __init__(self, driver):
        self.driver = driver

    def add_items(self):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.url_contains("inventory.html"))
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
