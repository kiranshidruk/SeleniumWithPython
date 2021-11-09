import time

from selenium.webdriver.common.by import By

from pageObjModel.Login_Page2 import LoginPage2


class LoginPage:
    Firstname = (By.NAME, "FirstName")
    Lastname = (By.ID, "Form_submitForm_LastName")
    Email = (By.XPATH, "//input[@id='Form_submitForm_Email']")
    Contact = (By.NAME, "Contact")
    Country = (By.NAME, "Country")
    Submit = (By.XPATH, "// input[ @ name = 'action_request']")

    def __init__(self, driver):
        self.driver = driver

    def getFirstName(self, firstname):
        return self.driver.find_element(*LoginPage.Firstname).send_keys(firstname)

    def getLastName(self, lastname):
        return self.driver.find_element(*LoginPage.Lastname).send_keys(lastname)

    def getEmail(self, email):
        return self.driver.find_element(*LoginPage.Email).send_keys(email)

    def getContact(self, contact):
        return self.driver.find_element(*LoginPage.Contact).send_keys(contact)

    def getCountry(self):
        return self.driver.find_element(*LoginPage.Country)

    def clickOnSubmit(self):
        self.driver.find_element(*LoginPage.Submit).click()
        loginPage2Obj = LoginPage2(self.driver)
        return loginPage2Obj

