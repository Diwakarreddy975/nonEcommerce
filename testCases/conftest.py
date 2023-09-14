import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
    elif browser == 'edge':
        driver = webdriver.Edge()
        driver.implicitly_wait(10)

    else:
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configer(config):
#     config._metadata['company name']='non e-commerce'
#     config._metadata['module']='customer'
#     config._metadata['tester mname']='diwakar'
#
# @pytest.mark
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("plugins", None)
