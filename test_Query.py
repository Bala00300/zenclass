import pytest
import time
from pageObject.LoginPage import LoginPage
from pageObject.Query import AddQuery
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddQuery:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addQuery(self,setup):
        self.logger.info("************* Test_003_AddQuery **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Query Test **********")

        self.addcust = AddQuery(self.driver)
        self.addcust.clickOnStudentsMainMenu()
        self.addcust.clickOnStudentsQueies()

        self.addcust.clickOnCancel()

        self.logger.info("************* Providing Query info **********")



        self.addcust.setQuerytitle("Guvi Python AT – 1 &2 Automation Project")
        self.addcust.setQuerydescription("This is a Project Test Code Running for the Python Automation 1&2 Project Given by mentor Mr. Suman Gangopadhyay")

        self.addcust.clickOnCreate()

        self.logger.info("************* Create Query info **********")

        self.logger.info("********* Add Query validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'Query has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add Query Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Query_scr.png")  # Screenshot
            self.logger.error("********* Add Query Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Query test **********")


