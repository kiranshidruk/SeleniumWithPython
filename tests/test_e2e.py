import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pageObjModel.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        time.sleep(2)
        log = self.getlogger()
        log.info("Lets start with End-to-End Framework")
        homePage = HomePage(self.driver)
        checkout = homePage.shopItems()
        cards = checkout.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            print(card_text)
            log.info(card_text)
            if card_text == "Blackberry":
                selected_product = card_text
                log.info("The selected product is " + selected_product)
                time.sleep(2)
                checkout.getCardFooter()[i].click()
                time.sleep(2)

        checkout.clickOnCheckout().click()
        time.sleep(2)
        checkoutProduct = checkout.textCheck()
        confirmpage = checkout.clickOnCheckout2()
        time.sleep(2)
        countrySet = confirmpage.setCountry()
        countrySet.send_keys("ind")
        wait = self.getExpWait(10)
        confirmpage.getCountry(wait).click()
        confirmpage.selectCheckbox().click()
        final_screenshot = confirmpage.ClickOnPurchase()
        final_text = confirmpage.Finaltext().text
        log.info("The final text is " + final_text)
        final_screenshot.getScreenshot("test_e2e.png")
        time.sleep(5)
        assert selected_product == checkoutProduct
        assert "Success" in final_text
