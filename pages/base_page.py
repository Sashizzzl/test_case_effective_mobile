import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    @allure.step('Находим элемент')
    def find_element(self, locator,timeout=10):
        try:
            return WebDriverWait(self.driver,timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден за {timeout} секунд.')
            return None
    @allure.step('Находим элементы')
    def find_elements(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))
        except TimeoutException:
            print(f'Элемент с локатором {locator} не найден за {timeout} секунд.')
            return None
    @allure.step('Кликаем на элемент')
    def click_element(self, locator,timeout=10):
        element = self.find_element(locator,timeout)
        if element:
            element.click()
        else:
            pytest.fail(f'Не получилось кликнуть на элемент с локатором {locator}')

