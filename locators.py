# locators.py
from selenium.webdriver.common.by import By

class HomePageLocators:
    COOKIE_POPUP_CLOSE = (By.XPATH, '//a[text()="Accept all cookies"]')
    MOBILE_MENU = (By.XPATH, '//span[text()="Mobile"]')

class MobilePhonesPageLocators:
    MOBILE_PHONES_LINK = (By.XPATH, '//ul[@class="bt-navbar-dropdown bt-navbar-products-menu"]//a[text()="Mobile phones"]')
    BANNER_IMAGES = (By.XPATH, '//div[contains(@class, "flexpay-card_card_wrapper__Antym")]')

class SIMDealsPageLocators:
    VIEW_SIM_DEALS = (By.XPATH, '//a[contains(text(),"View SIM only deals")]')
    NEW_PAGE_TITLE = (By.XPATH, '//h1[contains(text(), "SIM Only Deals")]')
    EXPECTED_TEXT = "30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month"
