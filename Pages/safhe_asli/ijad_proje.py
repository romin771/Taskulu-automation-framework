from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.selenium_driver import SeleniumDriver
from Base.basepage import BasePage



class IjadProjePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    #locators
    _ijad_proje_button = "//h4[@class='titles-section-title'][text()='تسکولو']//following-sibling::button"
    _onvan_proje_textfield = "//input[@data-name='عنوان پروژه']"
    _create_button_new_project = "//button[text()='بساز']"
    _error_empty_onvan_project = "//div[contains(text(),'عنوان پروژه نمی‌تواند خالی باشد')]"
    _badan = "//button[text()='بعدا']"

    """ expose locator to webelement
    def getIjadProjeButton(self):
        return self.driver.find_element(By.XPATH, self._ijad_proje_button)"""

    #Actions on element
    def clickOnIjadProjeButton(self):
        # self.getIjadProjeButton.click()
        self.elementClick(self._ijad_proje_button,locatorType="xpath")

    def enterOnvanProje(self,onvan):
        self.sendKeys(onvan,self._onvan_proje_textfield,locatorType="xpath")

    def clickOnCreateProjeBUtton(self):
        self.elementClick(self._create_button_new_project,locatorType="xpath")

    def clickOnBadanButton(self):
        self.elementClick(self._badan,locatorType="xpath")



    #main functionality ( wrapp all actions )
    def ijad_proje(self, projectname):
        self.clickOnIjadProjeButton()
        self.enterOnvanProje(projectname)
        self.clickOnCreateProjeBUtton()

    def verifySuccessProjeCreated(self):
        result = self.isElementPresent("//span[text()='صفحه پیش‌فرض']",locatorType="xpath")
        return result


    def verifyUnsuccessfulProjectCreated(self):
        result = self.isElementPresent(self._error_empty_onvan_project, locatorType="xpath")
        return result

    def badan(self):
        result = self.isElementPresent(self._badan, locatorType="xpath")
        if result == True:
            self.clickOnBadanButton()











