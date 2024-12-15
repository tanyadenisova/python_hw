import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys(45)

    driver.find_element(By.XPATH, "//span[normalize-space()='7']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='+']").click()
    driver.find_element(By.XPATH, "//span[normalize-space()='8']").click()
    driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning']").click()

    wait = WebDriverWait(driver, 50)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    div = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert div == "15"
    