"""
this file gonna generate webdriver instance based on browser configurations

exapmles :
    wdf = WebDriverFactory(browser)
    wdf = getWebDriverInstance()
"""
from selenium import webdriver


class WebDriverFactory():

    def __init__(self,browser):
        self.browser = browser

    """
    set chrome driver and ieplorer environment based on OS 
    
    chromedriver = "C:/.../chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    self.driver = webdriver.Chrome(chromedriver)
    
    PREFERED : set the path on the machine where browser will be exacuted 
    """

    def getWebdriverInstance(self):
        """
        Get Webdriver Instance based on the broswer configuration

        :return:
            'Webdriver Instance'
        """

        baseUrl = "https://taskulu.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()
        #setting driver implicit time out for an element
        driver.implicitly_wait(3)
        #maximize the  window
        driver.maximize_window()
        driver.get(baseUrl)

        return driver