from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    button_ = (By.CSS_SELECTOR, "input[type='submit']")
    finish_ = (By.CSS_SELECTOR, "#finish")
    complete_header = (By.XPATH, "//h2[@class='complete-header']")
    pass_or_fail = (By.XPATH, "//h2[@class ='title is-1']")

    def firstname(self):
        return self.driver.find_element(*ConfirmPage.first_name)

    def lastname(self):
        return self.driver.find_element(*ConfirmPage.last_name)

    def postalcode(self):
        return self.driver.find_element(*ConfirmPage.postal_code)

    def button(self):
        return self.driver.find_element(*ConfirmPage.button_)

    def finish(self):
        return self.driver.find_element(*ConfirmPage.finish_)

    def thankyou(self):
        return self.driver.find_element(*ConfirmPage.complete_header)

    def passOrFail(self):
        return self.driver.find_element(*ConfirmPage.pass_or_fail)

