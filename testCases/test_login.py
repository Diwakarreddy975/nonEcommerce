import time

import pytest

from selenium import webdriver
from pageObject.loginPage_POM import login_pom
from utilities import  Readconfiguration as RC
from utilities.GeneratingLogs import  log001
from  utilities import ExcelReader as EX


class Test_001_Login:
    baseURL=RC.read_configuration("basic info","url")
    password="admin"
    logger=log001.generate_log()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logger.info("login page test case started ")
        log001.generate_log().info("this is info of new log file")
        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        self.driver.close()
        if actual_title=="Your store. Login":
            assert True
        else:
            self.logger.error("login page test case failed")
            assert False
        self.logger.info("login page test case completed")

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("login page with credentials test case started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = login_pom(self.driver)

        rows= EX.get_row_count("C:\\Users\\91789\\OneDrive\\Desktop\\testdadata.xlsx","Sheet1")

        for r in range(2,rows+1):

            self.username=EX.get_cell_data("C:\\Users\\91789\\OneDrive\\Desktop\\testdadata.xlsx","Sheet1",r,1)
            self.password=EX.get_cell_data("C:\\Users\\91789\\OneDrive\\Desktop\\testdadata.xlsx","Sheet1",r,2)
            self.result=EX.get_cell_data("C:\\Users\\91789\\OneDrive\\Desktop\\testdadata.xlsx","Sheet1",r,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title

            if act_title == "Dashboard / nopCommerce administration":
                if self.result=="pass":
                    assert True
                    self.driver.back()
                    time.sleep(3)
            else:
                if self.result=="fail":
                   assert True
                   time.sleep(3)
        self.driver.close()






