import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExamplePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать заданные кнопки на калькуляторе")
    def fill_example(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='7']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='+']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='8']").click()
        self.driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning']").click()

    @allure.step("Подождать заданное время")
    def wait(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    @allure.step("Получить результат")
    def assert_response(self):
        div = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert div == "15"
 