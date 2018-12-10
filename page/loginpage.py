from selenium import webdriver
from time import sleep
from common.base import Base


# 登录页面类
class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.b = Base(self.driver)

    def login(self, usr="admin", psw="666666"):
        self.driver.get("http://47.97.160.167:8980/weibofenqi-manager/login/index.do")
        self.driver.maximize_window()
        sleep(3)
        self.b.clear(("css selector", ".formBox>form>input:nth-child(1)"))
        self.b.send(("css selector", ".formBox>form>input:nth-child(1)"), usr)
        self.b.clear(("css selector", ".formBox>form>input:nth-child(3)"))
        self.b.send(("css selector", ".formBox>form>input:nth-child(3)"), psw)
        self.b.click(("css selector", ".formBox>form>input:nth-child(5)"))
        # self.driver.find_element_by_css_selector(".formBox>form>input:nth-child(1)").send_keys(usr)
        # self.driver.find_element_by_css_selector(".formBox>form>input:nth-child(3)").send_keys(psw)
        # self.driver.find_element_by_css_selector(".formBox>form>input:nth-child(5)").click()

    def get_login_result(self):
        try:
            r = self.b.get_text(("css selector", "#sessionInfoDiv>strong"))
            return r
        except:
            r = ""
            return r


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    stage = LoginPage(driver)
    stage.login(usr="admin", psw="666666")
    driver.quit()
