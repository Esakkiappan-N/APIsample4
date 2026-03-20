from locators.mobile.app_locators import AppLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_first_button(self):
        element = self.wait.until(
            EC.element_to_be_clickable(AppLocators.FIRST_BUTTON)
        )
        element.click()

    def click_second_button(self):
        element = self.wait.until(
            EC.element_to_be_clickable(AppLocators.SECOND_BUTTON)
        )
        element.click()

    def enter_text(self, text):
        field = self.wait.until(
            EC.presence_of_element_located(AppLocators.TEXT_FIELD)
        )
        field.send_keys(text)

    def is_screen_loaded(self):
        elements = self.driver.find_elements(*AppLocators.ANY_TEXT)
        return len(elements) > 0
