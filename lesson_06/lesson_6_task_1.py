from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()
wait = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))
print(wait.text)


driver.quit()
