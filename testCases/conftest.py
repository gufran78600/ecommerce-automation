import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Driver\\chromedriver.exe")
        print("Launching the chrome browser")
    else:
        driver = webdriver.Firefox(executable_path="C:\\Users\\user\\Driver\\geckodriver.exe")
        print("Launching the Firefox ")
    return driver


def pytest_addoption(parser):    #this will get the value from the cli/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):             #this will return the value to the setup method
    return request.config.getoption("--browser")


#directly generate the html report
# def pytest_configure(config):
#     config._metadata["Tester Name"] = "Gufran"
#     config._metadata["Application name"] = "nop-ecommerce"
#     config._metadata["Module Name"] = "Login page"
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)




