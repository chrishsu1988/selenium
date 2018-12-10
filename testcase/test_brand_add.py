import unittest
from selenium import webdriver
from page.loginpage import LoginPage
from page.brandmange import BrandMange


class TestAddBrand(unittest.TestCase):
    """添加品牌测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.stg = LoginPage(self.driver)
        self.stg.login()
        self.add = BrandMange(self.driver)

    def test_add_brand(self):
        """添加品牌：test锤子"""
        self.add.brand_add("test锤子", "10086", r"D:\ppoh75.png")
        q = self.add.brand_query("test锤子", 2)
        self.assertEqual(q, "test锤子")

    def tearDown(self):
        self.driver.quit()