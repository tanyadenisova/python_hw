from selenium.webdriver.common.by import By


class AssertTotal:

    def __init__(self, driver):
        self.driver = driver

    def total(self):
        total_price = self.driver.find_element(By.XPATH, "//div[@class='summary_total_label']").text
        assert total_price == "Total: $58.29"
