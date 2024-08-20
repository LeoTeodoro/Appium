import unittest
from appium.webdriver.common.appiumby import AppiumBy
from Conection.conection import Driver
from Actions.palmlog import Palmlog

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Driver()
        
    def tearDown(self):
        self.driver.instance.quit()

    def test_accept_permission(self) -> None:
        palmlog = Palmlog(self.driver)
        palmlog.clickByID('com.android.permissioncontroller:id/permission_allow_foreground_only_button')

if __name__ == '__main__':
    unittest.main()