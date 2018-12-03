from selenium import webdriver


class QueryWeather():
    def __init__(self, driver):
        self.driver = driver

    def query_weather(self, city):
        self.driver.find_element_by_css_selector("#index_serch>input").send_keys(city)
        self.driver.find_element_by_css_selector(".tianqi_search_btn").click()
        try:
            t = self.driver.find_element_by_css_selector(".name>h2").text
            return t
        except:
            return ""


