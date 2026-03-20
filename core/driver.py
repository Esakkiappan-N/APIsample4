import os
from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver():
    options = UiAutomator2Options()

    # ✅ APK path (local + GitHub)
    local_apk = os.path.expanduser("~/Downloads/app-release-4-3-26.apk")
    repo_apk = os.path.abspath("app.apk")

    options.app = local_apk if os.path.exists(local_apk) else repo_apk

    # ✅ Emulator capabilities
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("deviceName", "emulator-5554")

    options.set_capability("autoGrantPermissions", True)
    options.set_capability("noReset", False)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
