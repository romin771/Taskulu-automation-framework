from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.home.login_page import LoginPage
import unittest
import pytest
from Utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    baseUrl = "https://taskulu.com/"
    """ we can add these to common location --> conftest.py
    baseUrl = "https://taskulu.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)  """


    """ i just need this for login classes not anywhere else,
    common plase where use for other classes also ,so i dont want to initialize and put it in so make it classLevel setup """
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseUrl)

        self.lp.login("romin@taskulu.com","Romin123456789")
        self.driver.implicitly_wait(5)

        result1 = self.lp.verifyLoginTitle()
        #assert result1 == True
        self.ts.mark(result1, "incorrect title ")

        result2 = self.lp.verifySuccessfulLogin()
        #assert result2 == False
        self.ts.markFinal("verifySuccessfullLogin", result2, "login was successful ")



        #self.driver.quit()


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.driver.get(self.baseUrl)

        self.lp.logOut()

        #create object and provide driver instance to it
        self.lp.login("romin@taskulu.com","Rom")
        self.driver.implicitly_wait(5)
        verifyLogin = self.lp.verifyFailedLogin()
        assert verifyLogin == True












