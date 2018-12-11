import unittest
from selenium import webdriver

from page.loginpage import LoginPage
from page.brandmange import BrandMange


class TestEditBrand(unittest.TestCase):
    """编辑品牌测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.lg = LoginPage(self.driver)
        self.lg.login()
        self.edit = BrandMange(self.driver)

    def test_brand_edit(self):
        """编辑品牌：test锤子"""
        self.edit.brand_edit("test锤子", "test锤子001")
        t = self.edit.brand_query("test锤子001", 2)
        self.assertEqual(t, "test锤子001")

    def tearDown(self):
        self.driver.quit()