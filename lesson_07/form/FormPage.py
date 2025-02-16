from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_form(self, first_name, last_name, address, email, phone, city, country, job, company):
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "e-mail").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "country").send_keys(country)
        self.driver.find_element(By.NAME, "job-position").send_keys(job)
        self.driver.find_element(By.NAME, "company").send_keys(company)
        self.driver.find_element(By.TAG_NAME, "form").submit()
