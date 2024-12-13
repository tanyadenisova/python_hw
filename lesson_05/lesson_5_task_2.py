from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")

driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']").click()

driver.quit()

# код одинаково отработал 3 раза