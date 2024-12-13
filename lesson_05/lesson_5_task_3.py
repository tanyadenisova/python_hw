from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

wait = WebDriverWait(driver, timeout=10)
alert = wait.until(EC.alert_is_present())
alert_text = alert.text
print(f"Текст алерта: {alert_text}")
alert.accept()

driver.quit()

# код одинаково отработал 3 раза
