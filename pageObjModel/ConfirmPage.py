from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from pageObjModel.Screenshots import Screenshots


class ConfirmPage:
    setcountry = (By.CSS_SELECTOR, 'input[id="country"]')
    getcountry = (By.LINK_TEXT, 'India')
    checkbox = (By.CSS_SELECTOR, 'div.checkbox-primary')
    purchase = (By.XPATH, '//input[@type="submit"]')
    finaltext = (By.CSS_SELECTOR, 'div[class*=alert-success]')

    def __init__(self, driver):
        self.driver = driver

    def setCountry(self):
        return self.driver.find_element(*ConfirmPage.setcountry)

    def getCountry(self, wait):
        return wait.until(ec.presence_of_element_located(ConfirmPage.getcountry))

    def selectCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def ClickOnPurchase(self):
        self.driver.find_element(*ConfirmPage.purchase).click()
        Screenshot = Screenshots(self.driver)
        return Screenshot

    def Finaltext(self):
        return self.driver.find_element(*ConfirmPage.finaltext)
