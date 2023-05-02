import pytest

from pageObject.add_new_customerPOM import AddCustomer
from pageObject.loginPage_POM import login_pom
from pageObject.searchCustomerPOM import SearchCustomer
from utilities import  Readconfiguration as RC
from utilities.GeneratingLogs import  log001
from  utilities import ExcelReader as EX

class Test_searchCustomer:
    baseURL = RC.read_configuration("basic info", "url")
    password = RC.read_configuration("basic info", "password")
    userName = RC.read_configuration("basic info", "username")
    logger=log001.generate_log()

    @pytest.mark.regression
    def test_searchBYEmail(self,setup):
        self.logger.info("******search customer by email ID***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=login_pom(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("++++++++login succesful+++++++++")
        self.logger.info("+++++++starting AddCustomer++++++++")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()

        SearchCu=SearchCustomer(self.driver)
        SearchCu.setEmail("steve_gates@nopCommerce.com")
        status=SearchCu.searchCustomerByEmail("steve_gates@nopCommerce.com")

        assert True==status
        self.logger.info("***********   Test004 search customer by email finished   ************")
        SearchCu.clear_Email()
        self.driver.close()

    @pytest.mark.regression
    def test_searchByFname(self, setup):
        self.logger.info("******search customer by email ID***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login_pom(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("++++++++login succesful+++++++++")
        self.logger.info("+++++++starting AddCustomer++++++++")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()

        SearchCu = SearchCustomer(self.driver)
        SearchCu.setFname("John")
        status = SearchCu.searchCustomerByfirstName("John")

        assert True == status
        self.logger.info("***********   Test004 search customer by email finished   ************")
        SearchCu.clearFname()
        self.driver.close()

    @pytest.mark.regression
    def test_searchByLname(self, setup):
        self.logger.info("******search customer by email ID***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login_pom(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("++++++++login succesful+++++++++")
        self.logger.info("+++++++starting AddCustomer++++++++")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomerMenu()
        self.addcust.clickCustomerItem()

        SearchCu = SearchCustomer(self.driver)
        SearchCu.setLName("Gates")
        status = SearchCu.searchCustomerByLastName("Gates")

        assert True == status
        self.logger.info("***********   Test004 search customer by email finished   ************")
        self.driver.close()






