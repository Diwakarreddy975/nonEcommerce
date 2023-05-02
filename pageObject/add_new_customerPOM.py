
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnkCustomers_menu_Xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuItem_xpath="(//p[contains(text(),' Customers')])[1]"
    btnAddNew_xpath="//*[@class='fas fa-plus-square']"
    txtEmail_xpath="//*[@id='Email']"
    txtPasswrd_xpath="//*[@id='Password']"
    txtFirstName_xpath="//*[@id='FirstName']"
    txtLastName="//*[@id='LastName']"
    Gender_male_xpath="//*[@id='Gender_Male']"
    Gender_Female_xpath="//*[@id='Gender_Female']"
    Date_of_Birth_xpath="//*[@id='DateOfBirth']"
    txtCompany_name_xpath="//*[@id='Company']"
    lstItem_Registerd_xpath="//li[contains(text(),'Registered')]"
    lstItem_Vendor_xpath="//li[contains(text(),'Vendor')]"
    drop_vendor_xpath="//*[@id='VendorId']"
    txtAdminContent_xpath="//*[@id='AdminComment']"
    btn_Save_xpath="//*[@name='save']"

    def __init__(self,driver):
        self.driver=driver


    def clickCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_Xpath).click()

    def clickCustomerItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuItem_xpath).click()

    def clickonAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,paswd):
        self.driver.find_element(By.XPATH,self.txtPasswrd_xpath).send_keys(paswd)

    def setFirstName(self,firstName):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(firstName)

    def setLasttName(self,lasttName):
        self.driver.find_element(By.XPATH,self.txtLastName).send_keys(lasttName)

    def setGender(self):
        self.driver.find_element(By.XPATH,self.Gender_male_xpath).click()

    def setDOB(self,DOB):
        self.driver.find_element(By.XPATH,self.Date_of_Birth_xpath).send_keys(DOB)

    def setCompanyName(self,Companyname):
        self.driver.find_element(By.XPATH,self.txtCompany_name_xpath).send_keys(Companyname)

    def setLstItem(self):

        self.driver.find_element(By.XPATH,self.lstItem_Registerd_xpath).click()

    def setLstItem1(self):
        self.driver.find_element(By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]").click()
        self.driver.find_element(By.XPATH, self.lstItem_Vendor_xpath).click()

    def dropVendor(self):
        ele=self.driver.find_element(By.XPATH,self.drop_vendor_xpath)
        select=Select(ele)
        select.select_by_index(1)
    def setAdmin_cmnt(self,txt):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(txt)

    def Click_Save_Btn(self):
        self.driver.find_element(By.XPATH,self.btn_Save_xpath).click()










