from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.home.navigation_page import navigationPage
from Pages.home.login_page import LoginPage
from Pages.safhe_asli.ijad_proje import IjadProjePage
from Utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from Utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class IjadMultipleProje2_csv(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.Ip = IjadProjePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = navigationPage(self.driver)


    def setUp(self):
        self.Ip.badan()  # for first time there will be a permission ask, this is for handling it


    @pytest.mark.run(order=1)
    @data(*getCSVData("myDataSetsForIjadProje.csv"))
    @unpack
    def test_validIjadProjeJaddid(self,courseName):
        """
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[text()='بعدا']").click()
        self.driver.implicitly_wait(4) """




        self.Ip.ijad_proje(courseName)
        result = self.Ip.verifySuccessProjeCreated()
        self.ts.markFinal("verify new khafan project", result,"i did it ")

        self.nav.navigateToSafheAsli()

        #self.driver.find_element(By.XPATH, "//div[@title='پروژه‌ها']").click()










