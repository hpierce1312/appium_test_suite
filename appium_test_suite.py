import unittest
import xmlrunner
import os
from appium import webdriver

class AppiumTest(unittest.TestCase):
    dc = {}

    def setUp(self):
        self.dc['platformName'] = 'Android'
        self.dc['platformVersion'] = '11'
        self.dc['deviceName'] = 'Nexus_6_API_30'
        self.dc['automationName'] = 'UiAutomator2'
        self.dc['appPackage'] = 'io.scanbot.hiring.qademo'
        self.dc['appActivity'] = 'io.scanbot.hiring.qademo.MainActivity'

        self.driver = webdriver.Remote("host.docker.internal:4723/wd/hub", self.dc)

    def test(self):
        for i in range(1, 10):
            self.driver.find_element_by_id('io.scanbot.hiring.qademo:id/counter_button').click()
            label = self.driver.find_element_by_id('io.scanbot.hiring.qademo:id/counter_label').text
            assert label == str(i)
            i += 1

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    with open(os.getcwd() + '/appium_test_results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)