from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(driver, timeout=10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal")))
print("Модальное окно открыто.")

close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//p[normalize-space()='Close'])[1]")))
close_button.click()
print("Модальное окно закрыто.")

driver.quit()