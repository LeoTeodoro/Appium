from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

class Palmlog:
    def __init__(self, driver):
        self.driver = driver
        self.permission = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'))
        )
        
    def clickByID(self, id):
        button = self.driver.instance.find_element(by=AppiumBy.ID, value=id)
        button.click()
