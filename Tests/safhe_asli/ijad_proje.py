from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.home.login_page import LoginPage
from Pages.safhe_asli.ijad_proje import IjadProjePage
from Utilities.teststatus import TestStatus   #assertion
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class IjadProje(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectClass(self, oneTimeSetUp):
        self.Ip = IjadProjePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validIjadProjeJaddid(self):

        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[text()='بعدا']").click()
        self.driver.implicitly_wait(4)

        self.Ip.ijad_proje("profesional try")
        result = self.Ip.verifySuccessProjeCreated()
        self.ts.markFinal("verify new khafan project", result,"i did it ")


""" 
    def test_ijadProjeJadid(self):
        baseURL = "https://taskulu.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

    #first login to safhe asli
        lp = LoginPage(driver)
        lp.login("romin@taskulu.com","Romin123456789")
        driver.implicitly_wait(5)
        assertsuccessLogin = lp.verifySuccessfulLogin()
        assert assertsuccessLogin == True


        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//button[text()='بعدا']").click()
        driver.implicitly_wait(4)

    #then create new project and verify it
        ij = IjadProjePage(driver)
        ij.ijad_proje("taskuluFramework2")
        successNewProjectCreated = ij.verifySuccessProjeCreated()
        assert successNewProjectCreated == True  """




"""
    
        titleOfThePage = driver.title
        if titleOfThePage == new_project_name:
            print("project created")
        else:
            print("project NOOOT created")"""


               













