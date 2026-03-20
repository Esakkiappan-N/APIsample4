from appium.webdriver.common.appiumby import AppiumBy


class AppLocators:
    FIRST_BUTTON = (AppiumBy.XPATH, "(//android.widget.Button)[1]")
    SECOND_BUTTON = (AppiumBy.XPATH, "(//android.widget.Button)[2]")
    TEXT_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    ANY_TEXT = (AppiumBy.CLASS_NAME, "android.widget.TextView")
