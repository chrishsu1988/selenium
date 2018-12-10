import time
import unittest
from selenium import webdriver
from page.loginpage import LoginPage
from page.suppliermange import SupplierMange


class TestAddSupplier(unittest.TestCase):
    """添加供应商测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://47.97.160.167:8980/weibofenqi-manager/login/index.do")
        self.driver.maximize_window()
        self.stg = LoginPage(self.driver)
        self.stg.login()
        self.add = SupplierMange(self.driver)

    def test_add_supplier(self):
        """添加供应商：test003"""
        self.add.supplier_add("test003")
        t = self.add.supplier_query( "test003")
        self.assertEqual(t, "test003")

    def tearDown(self):
        self.driver.quit()