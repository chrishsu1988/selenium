import unittest
from selenium import webdriver
import time
from common import edit
from common import query
from common import login


class TestEditSupplier(unittest.TestCase):
    """编辑供应商测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://47.97.160.167:8980/weibofenqi-manager/login/index.do")
        self.driver.maximize_window()

    def test_edit(self):
        """编辑供应商test003"""
        time.sleep(1)
        login.login(self.driver, "admin", "666666")
        time.sleep(1)
        edit.edit(self.driver, "test003", "test003456")
        time.sleep(1)
        t = query.query(self.driver, "test003456")
        time.sleep(1)
        self.assertEqual(t, "test003456")

    def tearDown(self):
        self.driver.quit()