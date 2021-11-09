import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

desired_capability = DesiredCapabilities.FIREFOX.copy()
desired_capability['--headless'] = True
desired_capability['--no-sandbox'] = True
desired_capability['--disable-gpu'] = True
desired_capability['--window-size=1420,1080'] = True

profile = webdriver.FirefoxProfile()
profile.set_preference('--headless', True)
profile.set_preference('--no-sandbox', True)
profile.set_preference('--disable-gpu', True)

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.add_argument('--no-sandbox')
fireFoxOptions.add_argument('--window-size=1420,1080')
fireFoxOptions.add_argument('--headless')
fireFoxOptions.add_argument('--disable-gpu')

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # driver = webdriver.Chrome(executable_path=r'/home/kiran/Downloads/Selenium/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=fireFoxOptions)
    driver.maximize_window()
    # driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.quit()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outc
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)
