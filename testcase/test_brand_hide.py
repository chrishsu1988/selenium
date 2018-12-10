import unittest
from selenium import webdriver

from page.loginpage import LoginPage
from page.brandmange import BrandMange


class TestEditSupplier(unittest.TestCase):
    """隐藏品牌测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.lg = LoginPage(self.driver)
        self.lg.login()
        self.edit = BrandMange(self.driver)

    def test_edit(self):
        """隐藏品牌：test锤子001"""
        self.edit.brand_hide("test锤子001")
        t = self.edit.brand_query("test锤子001", 6)
        self.assertEqual(t, "无效")

    def tearDown(self):
        self.driver.quit()