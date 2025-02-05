import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from config import URL
from pages.main_page import MainPage

@pytest.fixture(params=["chrome","firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.maximize_window()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        browser.maximize_window()
    else:
        ValueError("Can't create instance for this browser params")
    yield browser
    browser.quit()
@pytest.fixture
def navigate(driver):
    driver.get(URL.URL_PAGE)
    yield driver
@pytest.fixture(autouse=True)
def setup_method(driver):
    main = MainPage(driver)
    return main

