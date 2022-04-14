from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    add_item = (By.CSS_SELECTOR, "button[name*='sauce-labs-backpack']")
    card_link = (By.XPATH, "//a[@class='shopping_cart_link']")
    Product_checkout = (By.XPATH, "//button[@id='checkout']")
    burger_menu = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    click_about = (By.XPATH, "//a[@id='about_sidebar_link']")

    def additem(self):
        return self.driver.find_element(*CheckOutPage.add_item)

    def cardlink(self):
        return self.driver.find_element(*CheckOutPage.card_link)

    def productcheckout(self):
        return self.driver.find_element(*CheckOutPage.Product_checkout)

    def burgermenu(self):
        return self.driver.find_element(*CheckOutPage.burger_menu)

    def clickonAbout(self):
        return self.driver.find_element(*CheckOutPage.click_about)
