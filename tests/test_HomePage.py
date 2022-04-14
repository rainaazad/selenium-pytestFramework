import pytest

from pageObjects.HomePage import HomePage
from pageObjects.checkoutPage import CheckOutPage
from pageObjects.confirmPage import ConfirmPage
from test_Data.homePageData import HomePageData
from utilities.BaseClass import BaseClass

expected_string = "Pass or fail."


class TestTwo(BaseClass):

    def test_logginpage(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("full Name is "+getData["full_name"])
        homepage.username().send_keys(getData["full_name"])
        homepage.password().send_keys(getData["password"])
        homepage.submit().click()
        checkout = CheckOutPage(self.driver)
        checkout.burgermenu().click()
        self.driver.implicitly_wait(10)
        checkout.clickonAbout().click()
        confirmpage = ConfirmPage(self.driver)
        actual_string = confirmpage.passOrFail().text
        assert expected_string in actual_string
        self.driver.refresh()

    # @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param
