class LoginPage:
    # Login Page
    textbox_email_xpath = "//*[@id=root]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input"
    textbox_password_xpath = "//*[@id=root]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input"
    button_login_xpath = "//*[@id=root]/div/div/div[1]/div[2]/div/div[1]/form/button"
    button_logout_xpath = "//*[@id=root]/nav/div/div/div/div/button[2]"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()