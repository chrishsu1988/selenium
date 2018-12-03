import unittest
from selenium import webdriver
from common.query_weather import QueryWeather


class TestQueryWeather(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = 'http://www.tianqi.com'
        self.driver.get(url)
        self.driver.maximize_window()

    def test_query_weather(self):
        t = QueryWeather(self.driver).query_weather("郑州")
        print(t)

    def tearDown(self):
        self.driver.quit()

















if __name__ == "__main__":
    unittest.main()
