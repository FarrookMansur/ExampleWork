from selenium import webdriver
import unittest
from driver.WorkMarket_Login_Page import WorkMarket_Login_Page
from driver.WorkMarket_Home_Page import WorkMarket_Home_Page


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver = self.driver

        driver.get('http://dev.workmarket.com/login')

        #Login_Page
        login = WorkMarket_Login_Page(driver)
        login.enter_username("qa+candidatetest@workmarket.com")
        login.enter_password("candidate123")
        login.select_checkbox()
        login.click_login_btn()

        #Home_Page
        homepage = WorkMarket_Home_Page(driver)
        homepage.click_find_talent()
        driver.implicitly_wait(5)
        homepage.search_worker("test")
