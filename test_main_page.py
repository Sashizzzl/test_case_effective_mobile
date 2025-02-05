import allure
from config import URL
import pytest
from pages.main_page import MainPage
class TestMainPage:
    @allure.title('Проверка успешного перехода по клику на блоки')
    @pytest.mark.parametrize("click,expected_url", [(MainPage.click_about,URL.URL_ABOUT), (MainPage.click_services,URL.URL_SERVICES),(MainPage.click_cases,URL.URL_CASES),(MainPage.click_reviews,URL.URL_REVIEWS),(MainPage.click_contacts,URL.URL_CONTACTS),(MainPage.click_specialists,URL.URL_SPECIALISTS),(MainPage.click_effective_mobile_title,URL.URL_EFFECTIVE_MOBILE_MAIN)])
    def test_click_about_redirects_to_about_page(self, driver, navigate,setup_method,click,expected_url):
        main= setup_method
        click(main)
        current_url = main.get_current_url()
        assert current_url == expected_url

