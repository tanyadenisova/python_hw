from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, "award")))
print(driver.find_element(By.ID, "award").get_dom_attribute("src"))

driver.quit()
