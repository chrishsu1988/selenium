import unittest
from selenium import webdriver

from page.loginpage import LoginPage
from page.brandmange import BrandMange


class TestEditSupplier(unittest.TestCase):
    """显示品牌测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.lg = LoginPage(self.driver)
        self.lg.login()
        self.edit = BrandMange(self.driver)

    def test_edit(self):
        """显示品牌：test锤子001"""
        self.edit.brand_display("test锤子001")
        t = self.edit.brand_query("test锤子001", 6)
        self.assertEqual(t, "有效")

    def tearDown(self):
        self.driver.quit()