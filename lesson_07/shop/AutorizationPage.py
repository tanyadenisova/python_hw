from selenium.webdriver.common.by import By


class AutorizationPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def fill_login(self, user_name, password):
        self.driver.find_element(By.NAME, "user-name").send_keys(user_name)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "login-button").click()
