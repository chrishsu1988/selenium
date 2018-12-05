from selenium import webdriver
from page.loginpage import LoginPage
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.stg = LoginPage(self.driver)

    def test_login_1(self):
        self.stg.login("admin", "666666")
        result = self.stg.get_login_result()
        if result == "admin":
            return True
        else:
            return False

    def test_login_2(self):
        self.stg.login("admin", "123456")
        result = self.stg.get_login_result()
        if result == "admin":
            return True
        else:
            return False

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()