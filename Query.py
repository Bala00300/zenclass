import time
from selenium.webdriver.support.ui import Select

class AddQuery:

    lnkStudents_mainmenu_xpath = "//*[@id=root]/div[1]/nav"
    lnkStudents_Quries_xpath = "//*[@id=root]/div[1]/nav/ul/div[6]/li/span/div/div[2]"
    btnCreatequery_xpath = "//*[@id=root]/div[2]/div/div[1]/div[1]/button"
    btnCancel_xpath="//*[@id=WelcomeModal]/div/div/section[3]/div[2]/button[1]"
    txtQuerytitle_xpath="//*[@id=root]/div[2]/div/div[2]/div/div/form/div[5]/div[1]/input"
    txtQuerydescription_xpath="//*[@id=root]/div[2]/div/div[2]/div/div/form/div[5]/textarea"
    btnCreate_xpath="//*[@id=root]/div[2]/div/div[2]/div/div/form/div[13]/div/button"



    def __init__(self, driver):
        self.driver = driver

    def clickOnStudentsMainMenu(self):
        self.driver.find_element_by_xpath(self.lnkStudents_mainmenu_xpath).click()

    def clickOnStudentsQueies(self):
        self.driver.find_element_by_xpath(self.lnkStudents_Quries_xpath).click()

    def clickOnCreateQuery(self):
        self.driver.find_element_by_xpath(self.btnCreatequery_xpath).click()

    def clickOnCancel(self):
        self.driver.find_element_by_xpath(self.btnCancel_xpath).click()


    def setQuerytitle(self, name):
        self.driver.find_element_by_xpath(self.txtQuerytitle_xpath).send_keys(name)



    def setQuerydescription(self, content):
        self.driver.find_element_by_xpath(self.txtQuerydescription_xpath).send_keys(content)

    def clickOnCreate(self):
        self.driver.find_element_by_xpath(self.btnCreate_xpath).click()