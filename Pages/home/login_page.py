from selenium.webdriver.common.by import By
from Base.selenium_driver import SeleniumDriver
import time
from Base.basepage import BasePage
from Pages.home.navigation_page import navigationPage



class LoginPage(BasePage):

    #defice constructor to work on element
    #we want to provide driver instance  --> because we want to bring all driver.finde_element stuff
    def __init__(self, driver):
        super().__init__(driver)   #why ? because we inherit from SeleniumDriver and our super class which is SeleniumDriver also need driver to do actions on elements
        self.driver = driver
        self.nav = navigationPage(driver)


    # Locators       benefit of it is: when the locator change, we will just change here, not anywhere else. its kind of dynamic, not hardcoded in our code
    _login_navigate_button = "//a[contains(text(),'Login')]"
    _email_Textfield = "//input[@placeholder='Email, e.g. bilbo@example.com']"
    _password_Textfield = "//input[@placeholder='Password, e.g. •••••••••••••••••']"
    _login_confirmbutton = "//button[contains(text(),'LOGIN')]"
    _invalid_Login_message = "//p[text()='Invalid username or password']"

    """
    def getLoginNavigateButton(self):
        return self.driver.find_element(By.XPATH, self._login_navigate_button)
    def getEmainTextfield(self):
        return self.driver.find_element(By.XPATH, self._email_Textfield )
    def getPasswordTextfield(self):
        return self.driver.find_element(By.XPATH, self._password_Textfield)
    def getLoginConfirmbutton(self):
        return self.driver.find_element(By.XPATH, self._login_confirmbutton) """

    #actions
    def clickOnLoginLink(self):
        #elf.getLoginNavigateButton().click()
        self.elementClick(self._login_navigate_button, locatorType="xpath")
    def enterEmail(self, email):
        self.sendKeys(email, self._email_Textfield, locatorType="xpath")
    def enterPassword(self, password):
        self.sendKeys(password,self._password_Textfield, locatorType="xpath")
    def clickOnLoginConfirmButton(self):
        self.elementClick(self._login_confirmbutton, locatorType="xpath")

    #it is functionality, it wrapp all the actions
    def login(self, email="", password=""):  #by providing empty string " ", we will make email and pass as optional arguments
        # loginButton = self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        # loginButton.click()     into this ---> self.clickOnLoginLink
        self.clickOnLoginLink()
        #self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(3)
        self.clickOnLoginConfirmButton()

    def verifySuccessfulLogin(self):
        result = self.isElementPresent("//h3[text()='صفحه اصلی']", locatorType="xpath")
        return result

    def verifyFailedLogin(self):
        result = self.isElementPresent("//p[contains(text(),'Invalid username or password')]",locatorType="xpath")
        return result


    def clearFields(self):
        emailTextField = self.getElements(self._email_Textfield, locatorType="xpath")
        emailTextField.clear()

        passwordTextField = self.getElements(self._password_Textfield, locatorType="xpath")
        passwordTextField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("T")


    """ 
    we handle login in conftest, in order to not loging for each and every testSuite. but what if we want to check the login
    itself ? we have to be log out to be able to test the login. and while we handle login scenarion in conftest, we are always login. 
    
    so we should log out first , in order to test the login feature itself. 
    
    """
    def logOut(self):
        self.nav.navigateToLogOut()












