from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HomePageLocators, MobilePhonesPageLocators, SIMDealsPageLocators
import time



class BTWebsiteAutomation:
    def __init__(self):
        self.driver = None

    def setup(self):
        # Create a WebDriver instance (you should set the path to your driver)
        self.service_obj = Service("C:/Users/KDQ2KOR/Downloads/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service_obj)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        if self.driver:
            self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)

    def close_cookie_popup(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.COOKIE_POPUP_CLOSE)).click()
            
        except Exception as e:
            print("Cookie pop-up not found or could not be closed.")

    def hover_to_mobile_menu(self):
        mobile_menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.MOBILE_MENU))
        )
        ActionChains(self.driver).move_to_element(mobile_menu).perform()

    def click_mobile_phones(self):
        mobile_phones = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, MobilePhonesPageLocators.MOBILE_PHONES_LINK))
        )
        mobile_phones.click()

    def verify_banners_count(self, min_count):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MobilePhonesPageLocators.BANNER_IMAGES)
        )
        banners = self.driver.find_elements(MobilePhonesPageLocators.BANNER_IMAGES)
        return len(banners) >= min_count

    def scroll_and_click_sim_deals(self):
        view_sim_deals = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SIMDealsPageLocators.VIEW_SIM_DEALS)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", view_sim_deals)
        view_sim_deals.click()

    def validate_new_page_title(self, expected_title):
        new_page_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//h1[contains(text(), "{expected_title}")]'))
        )
        return new_page_title.text == expected_title

    def validate_text_on_new_page(self, expected_text):
        return expected_text in self.driver.page_source

if __name__ == "__main__":
    bt_automation = BTWebsiteAutomation()
    try:
        bt_automation.setup()
        bt_automation.open_url('https://www.bt.com/')
        bt_automation.close_cookie_popup()
        bt_automation.hover_to_mobile_menu()
        bt_automation.click_mobile_phones()
        assert bt_automation.verify_banners_count(3), "There are fewer than 3 banners present."
        bt_automation.scroll_and_click_sim_deals()
        assert bt_automation.validate_new_page_title("SIM Only Deals"), "New page title is not valid."
        expected_text = "30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month"
        assert bt_automation.validate_text_on_new_page(expected_text), "Expected text not found on the page."
    except AssertionError as e:
        print("Automation failed:", e)
    finally:
        bt_automation.teardown()
