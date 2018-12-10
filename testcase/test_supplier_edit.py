import unittest
from selenium import webdriver

from page.loginpage import LoginPage
from page.suppliermange import SupplierMange


class TestEditSupplier(unittest.TestCase):
    """编辑供应商测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.lg = LoginPage(self.driver)
        self.lg.login()
        self.edit = SupplierMange(self.driver)

    def test_edit(self):
        """编辑供应商：test003"""
        self.edit.supplier_edit("test003", "test003456")
        t = self.edit.supplier_query("test003456")
        self.assertEqual(t, "test003456")

    def tearDown(self):
        self.driver.quit()