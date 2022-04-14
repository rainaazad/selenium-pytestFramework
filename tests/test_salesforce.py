from random import randint

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CreateUsers import CreateUsers
from pageObjects.HomePage import HomePage
from test_Data.homePageData import HomePageData
from utilities.BaseClass import BaseClass

num = randint(1, 1000)

option_to_be_selected = ""
# f_name = f'Raina{num}'
# l_name = f'Azad{num}'
# full_name = f"{f_name} {l_name}"


class TestThree(BaseClass):
    def test_salesforce(self, getData):
        f_name = f"{getData['firstname']}{num}"
        l_name = f"{getData['lastname']}{num}"
        email_from_excel_splitted = getData["email"].split("@")
        email = f"{email_from_excel_splitted[0]}{num}@{email_from_excel_splitted[1]}"

        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info(getData["emailID"])
        homepage.salesforce_email().send_keys(getData["emailID"])
        homepage.salesforce_password().send_keys(getData["password"])
        homepage.salesforce_loggin().click()

        # self.driver.switch_to.window()
        self.driver.implicitly_wait(10)
        createusers = CreateUsers(self.driver)
        createusers.CreateOption().click()
        createusers.users().click()
        self.driver.implicitly_wait(5)
        fr = self.driver.find_element(By.XPATH, "//iframe[contains(@name,'vfFrameId')]")
        self.driver.switch_to.frame(fr)
        self.driver.implicitly_wait(20)
        createusers.firstname().send_keys(f_name)
        createusers.lastname().send_keys(l_name)
        createusers.emailname().send_keys(email)
        createusers.companyname().send_keys(getData["company"])
        createusers.companyname().send_keys(getData["country"])
        options = self.driver.find_elements(By.XPATH, "//select[@name='Profile']//option")

        for option in options:
            option_to_be_selected = option.text
            break

        action = Select(self.driver.find_element_by_id("Profile"))
        action.select_by_visible_text(option_to_be_selected)
        self.driver.find_element_by_xpath("(//input[@name='save'])[2]").click()

        self.driver.switch_to.default_content()

        # driver.implicitly_wait(20)
        #
        # fr1 = driver.find_element(By.XPATH, "//iframe[contains(@name,'vfFrameId')]")
        #
        # driver.switch_to.frame(fr1)
        # print("upto")
        #
        # name = driver.find_element_by_xpath("//td[text()='Name']//following::td[1]").text
        # if name == full_name:
        #     print('matched')
        # else:
        #     print('unmatched')

    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self, request):
        return request.param
