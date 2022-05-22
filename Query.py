import time

from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains

class AddQuery:

    def __init__(self, driver):
        self.driver = driver

    def StudentsMainMenu(self):

        Student=self.driver.find_element(by=By.XPATH,value='/html/body/div/div[1]/nav/ul')

        actions=ActionChains(self.driver)
        actions.move_to_element(Student).perform()


    def clickOnStudentsQueries(self):
        Queries = self.driver.find_element_by_xpath("/html/body/div/div[1]/nav/ul/div[6]/li/span/div/div[2]")
        actions=ActionChains(self.driver)
        actions.move_to_element(Queries).click()


    def clickOnCreateQuery(self):
        createquery=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select")
        createquery.clik()

    def clickOnCancel(self):
        cancel=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]")
        cancel.click()

    def selectCategory(self):
        category=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select")
        category.click()
        drp=select(category)
        drp.select_by_visible_text("Zen-Class Doubt")

    def selectSubcategory(self):
        subcategory=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select")
        subcategory.click()
        drp=select(subcategory)
        drp.select_by_value("101")

    def selectLanguage(self):
        language=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select")
        language.click()
        drp=select(language)
        drp.select_by_index("0")
        self.driver.execute_script("argument[0].scroll into view();",scroll)

    def setQuerytitle(self):
        Querytitle=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input")
        Querytitle.send_keys("Guvi Python AT – 1 &2 Automation Project")


    def setQuerydescription(self):
        Querydescription= self.driver.find_element(by=By.XPATH,
                                              value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea")
        Querydescription.send_keys("This is a Project Test Code Running for the Python Automation 1&2 Project Given by mentor Mr. Suman Gangopadhyay")


    def clickOnCreate(self):
       create=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button")
       create.click()
