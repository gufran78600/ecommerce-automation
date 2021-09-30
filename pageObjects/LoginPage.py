from selenium.webdriver.common.keys import Keys
class LoginPage:
    # add all the locator here present on the LoginPage
    user_name_by_id = "Email"
    user_password_by_id = "Password"
    user_login_by_xpath = "//button[contains(text(),'Log in')]"
    user_logout_by_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def login_username(self, username):
        self.driver.find_element_by_id(self.user_name_by_id).clear()
        self.driver.find_element_by_id(self.user_name_by_id).send_keys(username)

    def login_password(self, password):
        self.driver.find_element_by_id(self.user_password_by_id).clear()
        self.driver.find_element_by_id(self.user_password_by_id).send_keys(password)

    def getLogin(self):
        self.driver.find_element_by_xpath(self.user_login_by_xpath).click()

    def getLogout(self):
        self.driver.find_element_by_link_text(self.user_logout_by_link_text).click()
