from selenium import webdriver
from page.loginpage import LoginPage
import unittest
import ddt
from common.read_excel import ExcelUtil

# d1 = [
#     {"usr": "admin", "psw": "666666", "except": True},
#     {"usr": "admin", "psw": "123456", "except": False}
# ]

file_path = "testdata.xlsx"
sheet_name = "Sheet1"
data = ExcelUtil(file_path, sheet_name)
d1 = data.dict_data()


@ddt.ddt
class TestLogin(unittest.TestCase):
    """登录测试用例"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.stg = LoginPage(self.driver)

    @ddt.data(*d1)
    def test_login(self, test_data):
        """不同条件下的登录"""
        usr = test_data["usr"]
        psw = test_data["psw"]
        exp = test_data["except"]
        self.stg.login(usr, psw)
        result = self.stg.get_login_result()
        if result == "admin":
            print("登录成功")
            actual = True
        else:
            print("登录失败")
            actual = False
        self.assertTrue(exp == actual)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()