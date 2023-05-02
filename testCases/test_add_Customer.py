import random
import string
import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObject.add_new_customerPOM import AddCustomer
from pageObject.loginPage_POM import login_pom
from utilities import  Readconfiguration as RC
from utilities.GeneratingLogs import  log001
from  utilities import ExcelReader as EX


class Test_003_addCustomer:
    baseURL = RC.read_configuration("basic info", "url")
    password =RC.read_configuration("basic info","password")
    userName=RC.read_configuration("basic info","username")


    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        logger = log001.generate_log()
        logger.info("+++++++started+++++++++")
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = login_pom(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        logger.info("++++++++login succesful+++++++++")
        logger.info("+++++++starting AddCustomer++++++++")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()
        self.addcust.clickonAddNew()
        self.email=rand_generate()
        self.addcust.setEmail(self.email+"@gmail.com")
        self.addcust.setPassword(RC.read_configuration("inputData","password"))
        self.addcust.setFirstName(RC.read_configuration("inputData","firstName"))
        self.addcust.setLasttName(RC.read_configuration("inputData","lastName"))
        self.addcust.setGender()
        self.addcust.setDOB(RC.read_configuration("inputData","DOB"))
        self.addcust.setCompanyName(RC.read_configuration("inputData","company"))
        self.addcust.setLstItem1()

        self.addcust.dropVendor()
        self.addcust.setAdmin_cmnt(RC.read_configuration("inputData","adminComment"))
        self.addcust.Click_Save_Btn()
        logger.info("succesfully enterd required data in input fields")
        time.sleep(5)
        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True==True
            logger.info("***********customer added succesfully***********")
        else:
            assert  True==False

        self.driver.close()


def rand_generate(size=8,chars=string.ascii_letters+string.digits):
    return "".join(random.choice(chars) for x in range(size))
        