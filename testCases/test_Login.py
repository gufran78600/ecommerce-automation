from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.custom_Logger import LogGen


class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getApplicationUsername()
    password = Readconfig.getApplicationPassword()
    logger = LogGen.loggen()

    def test_homePage_titile(self, setup):
        self.logger.info("******** Test 001 ***************** ")
        self.logger.info('************ Verify Home page title ******************')
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("***********Passed ***********")
        else:
            self.driver.save_screenshot(".//Screenshots//Home_page_title")
            self.logger.info("********** Failed ***********")
            assert False

        self.driver.close()

    def test_text_validation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        text_msg = self.driver.find_element_by_xpath("//div[@class='title']").text
        if text_msg == "Welcome, please sign in!":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_text_validation.png")
            assert False
        self.driver.close()
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.login_username(self.username)
        self.lp.login_password(self.password)
        self.lp.getLogin()
        act_titile = self.driver.title
        if act_titile == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
        self.driver.close()