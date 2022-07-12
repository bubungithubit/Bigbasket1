from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from SampleProject.PomProject.page.login_page import Logintest


class logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\\Users\\malli\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        print("1")
        self.driver.get(Logintest.url)
        self.driver.find_element(by=By.NAME, value=Logintest.num).send_keys("9938574997")

        self.driver.find_element(by=By.XPATH, value=Logintest.continue1).click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(by=By.NAME, value=Logintest.num1).click()
        time.sleep(10)

        self.driver.find_element(by=By.XPATH, value=Logintest.continue2).click()
        time.sleep(10)
        print("welcome to Bigbasket")

    def test_j_screenshot(self):
        print("2")
        self.driver.get_screenshot_as_file("C:\\Screenshot\\add1.png")
        print("screenshot take successfully")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
