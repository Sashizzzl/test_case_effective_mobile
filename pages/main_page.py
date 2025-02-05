import allure
from pages.base_page import BasePage
from locators import Locators

class MainPage(BasePage):
    @allure.step('Кликаем на блок "О нас"')
    def click_about(self):
        self.click_element(Locators.ABOUT)

    @allure.step('Кликаем на блок "Услуги"')
    def click_services(self):
        self.click_element(Locators.SERVICES)

    @allure.step('Кликаем на блок "Проекты"')
    def click_cases(self):
        self.click_element(Locators.CASES)

    @allure.step('Кликаем на блок "Отзывы"')
    def click_reviews(self):
        self.click_element(Locators.REVIEWS)

    @allure.step('Кликаем на блок "Контакты"')
    def click_contacts(self):
        self.click_element(Locators.CONTACTS)

    @allure.step('Кликаем на блок "Выбрать специалиста"')
    def click_specialists(self):
        self.click_element(Locators.SPECIALISTS)

    @allure.step('Кликаем на надпись "Effective Mobile" в шапке')
    def click_effective_mobile_title(self):
        self.click_element(Locators.EFFECTIVE_MOBILE_TITLE)
    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url