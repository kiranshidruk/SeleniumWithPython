from selenium.webdriver.common.by import By
from pageObjModel.ConfirmPage import ConfirmPage

class CheckOutPage:
    items = (By.CSS_SELECTOR, '.card-title a')
    productFooter = (By.CSS_SELECTOR, '.card-footer button')
    checkout = (By.CSS_SELECTOR, 'a[class*="btn-primary"]')
    checkout2 = (By.CSS_SELECTOR, 'button[class*="btn-success"]')
    textcheck = (By.CSS_SELECTOR, ' h4 a')

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.items)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.productFooter)

    def clickOnCheckout(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def textCheck(self):
        return self.driver.find_element(*CheckOutPage.textcheck).text

    def clickOnCheckout2(self):
        self.driver.find_element(*CheckOutPage.checkout2).click()
        Confirmpage = ConfirmPage(self.driver)
        return Confirmpage
