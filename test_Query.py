import pytest
from pageObject.LoginPage import LoginPage
from pageObject.Query import AddQuery
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddQuery:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

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

        self.add = AddQuery(self.driver)
        self.add.StudentsMainMenu()

        self.add.clickOnStudentsQueries()

        self.add.clickOnCreateQuery()

        self.add.clickOnCancel()

        self.logger.info("************* Providing Query info **********")
        self.add.selectCategory()
        self.add.selectSubcategory()
        self.add.selectLanguage()
        self.add.setQuerytitle()
        self.add.setQuerydescription()
        self.add.clickOnCreate()

        self.logger.info("************* Create Query info **********")

        self.logger.info("********* Add Query validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'Query has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add Query Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_Query_scr.png")  # Screenshot
            self.logger.error("********* Add Query Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add Query test **********")


