from selenium.webdriver.common.by import By
from Base.selenium_driver import SeleniumDriver
import time
from Base.basepage import BasePage



class navigationPage(BasePage):

    #defice constructor to work on element
    #we want to provide driver instance  --> because we want to bring all driver.finde_element stuff
    def __init__(self, driver):
        super().__init__(driver)   #why ? because we inherit from SeleniumDriver and our super class which is SeleniumDriver also need driver to do actions on elements
        self.driver = driver


    # Locators
    _Home_icon = "//div[@title='پروژه‌ها']"
    _search_textfield = "//input[@placeholder='Email, e.g. bilbo@example.com']"
    _closed_project_toggle = "//input[@placeholder='Password, e.g. •••••••••••••••••']"
    _hesab_karbari_man = "//a[@href='/a/account']"
    _avatar = "//div[@class='header-profile pull-right']"
    _log_out= "//i[@class='i i-logout']"





    #actions
    def navigateToSafheAsli(self):
        self.elementClick(self._Home_icon,locatorType="xpath")
    def navigateToHesabKarbariMan(self):
        self.elementClick(self._avatar,locatorType="xpath")
        self.elementClick(self._hesab_karbari_man, locatorType="xpath")
    def navigateToLogOut(self):
        self.elementClick(self._avatar, locatorType="xpath")
        self.elementClick(self._log_out, locatorType="xpath")











