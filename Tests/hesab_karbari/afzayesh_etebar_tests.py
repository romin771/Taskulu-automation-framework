from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.home.login_page import LoginPage
import unittest
import pytest
from Utilities.teststatus import TestStatus


class afzayeshEtebarTests(unittest.TestCase):
    baseUrl = "https://taskulu.com/"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)