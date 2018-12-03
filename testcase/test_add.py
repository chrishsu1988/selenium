import time
import unittest
from selenium import webdriver
from common import add
from common import query
from common import login


class TestAddSupplier(unittest.TestCase):
    """添加供应商测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://47.97.160.167:8980/weibofenqi-manager/login/index.do")
        self.driver.maximize_window()

    def test_add(self):
        """添加供应商test003"""
        time.sleep(1)
        login.login(self.driver, "admin", "666666")
        add.add(self.driver, "test003")
        t = query.query(self.driver, "test003")
        self.assertEqual(t, "test003")

    def tearDown(self):
        self.driver.quit()