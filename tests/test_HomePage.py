import time

import pytest
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import Select

from pageObjModel.LoginPage import LoginPage

from testData.LoginPageData import LoginPageData


class TestHomePage(BaseClass):

    def test_login(self, getData):
        log = self.getlogger()
        loginPage = LoginPage(self.driver)
        log.info("login page opened")
        log.info("fill the data below")
        print(LoginPageData.test_loginPagedata2)
        loginPage.getFirstName(getData["firstname"])
        log.info("firstname is " + getData["firstname"])
        time.sleep(2)
        loginPage.getLastName(getData["lastname"])
        log.info("lastname is " + getData["lastname"])
        loginPage.getEmail(getData["email"])
        loginPage.getContact(getData["mobileNo"])
        country = loginPage.getCountry()
        Select_Country = Select(country)
        Select_Country.select_by_visible_text(getData["country"])
        time.sleep(25)
        loginPage2 = loginPage.clickOnSubmit()
        time.sleep(2)
        final_text = loginPage2.getFinalText()
        log.info(final_text)

        assert final_text == "Thank you."

        self.driver.back()
        self.driver.refresh()

        time.sleep(2)

    @pytest.fixture(params=LoginPageData.test_loginPagedata2)
    def getData(self, request):
        return request.param
