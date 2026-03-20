import allure
from core.driver import get_driver
from pages.mobile.app_page import AppPage


@allure.epic("APK Automation")
@allure.feature("Basic Testing")


def test_click_first_button():
    driver = get_driver()
    page = AppPage(driver)

    page.click_first_button()

    assert page.is_screen_loaded()

    driver.quit()


def test_click_second_button():
    driver = get_driver()
    page = AppPage(driver)

    page.enter_text("Hello")
    page.click_second_button()

    assert page.is_screen_loaded()

    driver.quit()
