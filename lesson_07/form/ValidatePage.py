from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class ValidatePage:

    def __init__(self, driver):
        self.driver = driver

    def allert_color(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))
        allert_color = self.driver.find_element(By.ID, "zip-code").value_of_css_property('border-color')
        assert allert_color == 'rgb(245, 194, 199)'

    def check(self):
        to_check = [
            "first_name", "last_name", "address", "e-mail", "phone", "city",
            "country", "job-position", "company"
        ]
        for field_id in to_check:
            try:
                border_color = self.driver.find_element(By.ID, field_id).value_of_css_property('border-color')
                assert border_color == "rgb(186, 219, 204)", f"Поле {field_id} имеет неправильный цвет границы: {border_color}"
            except NoSuchElementException:
                print(f"Элемент с ID '{field_id}' не найден.")
