from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions

class Driver:
    def __init__(self):
        desired_cap = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "avd": "Appium",
            "app": "C:\\PalmLog_Release_2_0_21.apk",
            "deviceName": "emulator-5554",
            "platformVersion": "15"
        }
        url = 'http://localhost:4723'
        options = AppiumOptions().load_capabilities(desired_cap)
        self.instance = webdriver.Remote(url, options=options)
        print("Conectado")
