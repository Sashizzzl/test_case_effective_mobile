from selenium.webdriver.common.by import By
class Locators:
    ABOUT= [By.XPATH,".//a[contains(text(),'О нас') and contains(@class,'atom')]"] #блок "О нас"
    SERVICES = [By.XPATH, ".//a[contains(text(),'Услуги') and contains(@class,'atom')]"]  # блок "Услуги"
    CASES = [By.XPATH, ".//a[contains(text(),'Проекты') and contains(@class,'atom')]"]  # блок "Проекты"
    REVIEWS = [By.XPATH, ".//a[contains(text(),'Отзывы') and contains(@class,'atom')]"]  # блок "Отзывы"
    CONTACTS = [By.XPATH, ".//a[contains(text(),'Контакты') and contains(@class,'atom')]"]  # блок "Контакты"
    SPECIALISTS = [By.XPATH, ".//a[contains(text(),'Выбрать специалиста') and contains(@class,'atom')]"]  # блок "Выбрать специалиста"
    EFFECTIVE_MOBILE_TITLE = [By.XPATH, ".//div[contains(@id,'532')]//a[contains(text(),'Effective Mobile')]"]  # надпись "Effective Mobile" в шапке


