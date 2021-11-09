
class Screenshots:

    def __init__(self, driver):
        self.driver = driver

    def getScreenshot(self, name):
        return self.driver.get_screenshot_as_file(name)
