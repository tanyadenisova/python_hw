import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    e_mail = driver.find_element(By.NAME, "e-mail")
    e_mail.send_keys("test@skypro.com")

    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("+7985899998787")

    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    driver.find_element(By.TAG_NAME, "form").submit()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-success")))

    zip_code = driver.find_element(By.ID, "zip-code")
    allert_color = zip_code.value_of_css_property('border-color')
    assert allert_color == 'rgb(245, 194, 199)'

    to_check = [
        "first_name", "last_name", "address", "e-mail", "phone", "city",
        "country", "job-position", "company"
        ]
    for field_id in to_check:
        try:
            field = driver.find_element(By.ID, field_id)
            border_color = field.value_of_css_property('border-color')
            assert border_color == "rgb(186, 219, 204)", f"Поле {field_id} имеет неправильный цвет границы: {border_color}"
        except NoSuchElementException:
            print(f"Элемент с ID '{field_id}' не найден.")

    driver.quit()
