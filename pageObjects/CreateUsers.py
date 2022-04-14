from selenium.webdriver.common.by import By


class CreateUsers:

    def __init__(self, driver):
        self.driver = driver

    Create_option = (By.XPATH, "//span[text()='Create']")
    Users = (By.XPATH, "(//span[text()='User'])[1]")
    first_name = (By.XPATH, "//input[@id='name_firstName']")
    last_name = (By.ID, "name_lastName")
    email_name = (By.ID, "Email")
    company_name = (By.ID, "CompanyName")
    country_name = (By.ID, "Addresscountry")

    def CreateOption(self):
        return self.driver.find_element(*CreateUsers.Create_option)

    def users(self):
        return self.driver.find_element(*CreateUsers.Users)

    def firstname(self):
        return self.driver.find_element(*CreateUsers.first_name)

    def lastname(self):
        return self.driver.find_element(*CreateUsers.last_name)

    def emailname(self):
        return self.driver.find_element(*CreateUsers.email_name)

    def companyname(self):
        return self.driver.find_element(*CreateUsers.company_name)

    def countryname(self):
        return self.driver.find_element(*CreateUsers.country_name)
