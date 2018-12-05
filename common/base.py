from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 基类
class Base():
    def __init__(self, driver):
        self.driver = driver

# 查找单元素的方法
    def find(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(locator))
        return element

# 查找多个元素的方法
    def finds(self, locator, timeout=30):
        elements = WebDriverWait(self.driver, timeout, 0.5).until(EC.presence_of_element_located(locator))
        return elements

# 输入文本的方法
    def send(self, locator, text):
        element = self.find(locator)
        element.send_keys(text)

# 模拟鼠标点击的方法
    def click(self, locator):
        element = self.find(locator)
        element.click()

# 清空输入框的方法
    def clear(self, locator):
        element = self.find(locator)
        element.clear()

# 获取文本的方法
    def get_text(self, locator):
        try:
            element = self.find(locator)
            t = element.text
            return t
        except:
            return ""