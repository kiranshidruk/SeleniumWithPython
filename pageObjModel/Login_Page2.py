from selenium.webdriver.common.by import By


class LoginPage2:
    getText = (By.CSS_SELECTOR, ".default-page__content h1")

    def __init__(self, driver):
        self.driver = driver

    def getFinalText(self):
        return self.driver.find_element(*LoginPage2.getText).text
