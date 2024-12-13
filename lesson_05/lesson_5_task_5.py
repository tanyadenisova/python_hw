from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_box = driver.find_element(By.XPATH, "//input[@type='number']")
search_box.send_keys(1000)
search_box.clear()
search_box.send_keys(999)

driver.quit()
