from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.home.login_page import LoginPage
from Pages.safhe_asli.ijad_proje import IjadProjePage
from Utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class IjadMultipleProje1(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectClass(self, oneTimeSetUp):
        self.Ip = IjadProjePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(["csv manualllls"],["csv manual3"],["csv manual4"])
    @unpack
    def test_validIjadProjeJaddid(self,courseName):
        """
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//button[text()='بعدا']").click()
        self.driver.implicitly_wait(4) """


        self.Ip.badan()

        self.Ip.ijad_proje(courseName)
        result = self.Ip.verifySuccessProjeCreated()
        self.ts.markFinal("verify new khafan project", result,"i did it ")

        self.driver.find_element(By.XPATH, "//div[@title='پروژه‌ها']").click()









