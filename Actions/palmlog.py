from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

class Palmlog:
    def __init__(self, driver):
        self.driver = driver
        
    def assertEqualsTextById(self, id, message):
        element = self.driver.instance.find_element(by=AppiumBy.ID, value=id)
        assert element.text == message
        return True
    
    def assertEqualsTextByXpath(self, xpath, message):
        element = self.driver.instance.find_element(by=AppiumBy.XPATH, value=xpath)
        assert element.text == message
        return True
        
    def waitElementById(self, id):
        self.permission = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, id))
        )
        
    def waitElementByXpath(self, xpath):
        self.permission = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
        
    def clickByID(self, id):
        button = self.driver.instance.find_element(by=AppiumBy.ID, value=id)
        button.click()
        
    def clickByXpath(self, xpath):
        button = self.driver.instance.find_element(by=AppiumBy.XPATH, value=xpath)
        button.click()
        
    def typeFieldByXpath(self, xpath, message):
        field = self.driver.instance.find_element(by=AppiumBy.XPATH, value=xpath)
        field.send_keys(message)
  
