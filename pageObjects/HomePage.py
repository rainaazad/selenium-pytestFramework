from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.CSS_SELECTOR, "input[name='user-name']")
    password_ = (By.CSS_SELECTOR, "#password")
    submit_click = (By.XPATH, "//input[@type='submit']")
    email_salesforce = (By.XPATH, "//input[@name='username']")
    password_salesforce = (By.XPATH, "//input[@type='password']")
    loggin_salesfoce = (By.XPATH, "//input[@type='submit']")

    def username(self):
        return self.driver.find_element(*HomePage.user_name)
        # basically if we put * then it will recognize as tuple
    def password(self):
        return self.driver.find_element(*HomePage.password_)
    def submit(self):
        return self.driver.find_element(*HomePage.submit_click)

    def salesforce_email(self):
        return self.driver.find_element(*HomePage.email_salesforce)
    def salesforce_password(self):
        return self.driver.find_element(*HomePage.password_salesforce)
    def salesforce_loggin(self):
        return self.driver.find_element(*HomePage.loggin_salesfoce)
