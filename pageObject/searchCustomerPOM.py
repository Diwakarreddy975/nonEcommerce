import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail_ID="SearchEmail"
    txtFirstName_ID="SearchFirstName"
    txtLastName_ID="SearchLastName"
    btnSearch_ID="search-customers"

    table_xpath="//table[@id='customers-grid']"
    table_rows="//table[@id='customers-grid']//tbody/tr"
    table_columns="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver


    def get_No_rows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_rows))

    def get_No_Columns(self):
        return len(self.driver.find_elements(By.XPATH,self.table_columns))

    def clear_Email(self):
        self.driver.find_element(By.ID, self.txtEmail_ID).clear()

    def clearFname(self):
        self.driver.find_element(By.ID,self.txtFirstName_ID).clear()


    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_ID).clear()
        self.driver.find_element(By.ID, self.txtEmail_ID).send_keys(email)
        self.driver.find_element(By.ID, self.btnSearch_ID).click()

    def setFname(self,Fname):
        self.driver.find_element(By.ID,self.txtFirstName_ID).clear()
        self.driver.find_element(By.ID, self.txtFirstName_ID).send_keys(Fname)
        self.driver.find_element(By.ID, self.btnSearch_ID).click()

    def setLName(self,Lname):
        self.driver.find_element(By.ID,self.txtLastName_ID).clear()
        self.driver.find_element(By.ID,self.txtLastName_ID).send_keys(Lname)
        self.driver.find_element(By.ID, self.btnSearch_ID).click()

    def searchCustomerByEmail(self,email):

        flag=False
        for r in range(1,self.get_No_rows()+1):
            time.sleep(2)
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag


    def searchCustomerByfirstName(self,FirstName):

        flag=False
        for r in range(1,self.get_No_rows()+1):
            FName=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if FirstName in FName:
                flag=True
                break
        return flag

    def searchCustomerByLastName(self,LastName):

        flag=False
        for r in range(1,self.get_No_rows()+1):
            FName=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if LastName in FName:
                flag=True
                break
        return flag

    def Click_on_Search(self):
        self.driver.find_element(By.ID,self.btnSearch_ID).click()