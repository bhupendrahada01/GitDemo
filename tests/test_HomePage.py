import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PythonSelFramework.TestData.HomePageData import HomePageData
from PythonSelFramework.pageObjects.HomePage import HomePage
from PythonSelFramework.utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_PageSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["name"])
        log.info("Name is "+getData["name"])
        homepage.getEmail().send_keys(getData["email"])
        log.info("Email is "+getData["email"])
        homepage.getPass().send_keys(getData["pass"])
        homepage.selectCheckbox().click()
        self.selectDdOptionsByText(homepage.gotoDropdown(), getData["gender"])
        homepage.selectSubmit().click()

        message = homepage.msgSucces().text
        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self, request):
        return request.param
