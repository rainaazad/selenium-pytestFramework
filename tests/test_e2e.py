import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.mark.usefixtures("browserInvocation")
from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import CheckOutPage
from pageObjects.confirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.username().send_keys("standard_user")
        homePage.password().send_keys("secret_sauce")
        homePage.submit().click()
        checkout = CheckOutPage(self.driver)
        checkout.additem().click()
        checkout.cardlink().click()
        checkout.productcheckout().click()
        confirmation = ConfirmPage(self.driver)
        confirmation.firstname().send_keys("raina")
        confirmation.lastname().send_keys("azad")
        confirmation.postalcode().send_keys("1234567")
        confirmation.button().click()
        confirmation.finish().click()
        actual_str = confirmation.thankyou().text
        log.info("Text receive from application is " + actual_str)

        assert "THANK YOU" in actual_str
