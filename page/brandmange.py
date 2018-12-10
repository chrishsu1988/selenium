from selenium import webdriver
from time import sleep
from common.base import Base


# 品牌管理页面类
class BrandMange():
    def __init__(self, driver):
        self.driver = driver
        self.b = Base(self.driver)

    def brand_add(self, name, sort_no, icon_path):
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[1]/div[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[2]/ul/li[3]"))
        sleep(1)
        self.b.switch_frame(("id", "mainFrame_1"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button-add']"))
        sleep(1)
        self.b.send(("xpath", ".//*[@id='_easyui_textbox_input2']"), name)
        sleep(1)
        self.b.send(("xpath", ".//*[@id='_easyui_textbox_input12']"), sort_no)
        sleep(1)
        self.b.send(("xpath", ".//*[@id='upBox']/div/input[2]"), icon_path)
        sleep(1)
        self.b.click(("xpath", ".//*[@id='add_submit_form']"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[15]/div[3]/a"))
        sleep(1)

    def brand_query(self, name, n):
        self.b.clear(("xpath", ".//*[@id='_easyui_textbox_input1']"))
        sleep(1)
        self.b.send(("xpath", ".//*[@id='_easyui_textbox_input1']"), name)
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button_search']"))
        sleep(1)
        try:
            a = self.b.get_text(("xpath", (".//tr[contains(@id,'2-0')]/td[%s]/div" % n)))
            return a
        except:
            return ""

    def brand_edit(self, name, name1):
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[1]/div[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[2]/ul/li[3]"))
        sleep(1)
        self.b.switch_frame(("id", "mainFrame_1"))
        sleep(1)
        self.b.clear(("xpath", ".//*[@id='_easyui_textbox_input1']"))
        sleep(1)
        self.b.send(("xpath", ".//*[@id='_easyui_textbox_input1']"), name)
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button_search']"))
        sleep(1)
        self.b.click(("xpath", ".//tr[contains(@id,'2-0')]/td[1]/div/input"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button-view']"))
        sleep(1)
        self.b.clear(("xpath", ".//*[@id='_easyui_textbox_input5']"))
        sleep(1)
        self.b.send(("xpath", ".//*[@id='_easyui_textbox_input5']"), name1)
        sleep(1)
        self.b.click(("xpath", ".//*[@id='edit_submit_form']"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[15]/div[3]/a"))
        sleep(1)

    def brand_display(self, name):
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[1]/div[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[2]/ul/li[3]"))
        sleep(1)
        self.b.switch_frame(("id", "mainFrame_1"))
        sleep(1)
        self.b.clear(("xpath", ".//*[@id='_easyui_textbox_input1']"))
        sleep(1)
        self.b.send(("xpath", ".//*[@id='_easyui_textbox_input1']"), name)
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button_search']"))
        sleep(1)
        self.b.click(("xpath", ".//tr[contains(@id,'2-0')]/td[1]/div/input"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button-disBlock']"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[15]/div[3]/a[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[15]/div[3]/a"))
        sleep(1)

    def brand_hide(self, name):
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[1]/div[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[2]/div[2]/ul/li[3]"))
        sleep(1)
        self.b.switch_frame(("id", "mainFrame_1"))
        sleep(1)
        self.b.clear(("xpath", ".//*[@id='_easyui_textbox_input1']"))
        sleep(1)
        self.b.send(("xpath", ".//*[@id='_easyui_textbox_input1']"), name)
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button_search']"))
        sleep(1)
        self.b.click(("xpath", ".//tr[contains(@id,'2-0')]/td[1]/div/input"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='button-block']"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[15]/div[3]/a[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[15]/div[3]/a"))
        sleep(1)



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    bd = BrandMange(driver)
    from page.loginpage import LoginPage
    lg = LoginPage(driver)
    lg.login("admin", "666666")
    # bd.brand_add("test锤子", "10086", r"D:\ppoh75.png")
    # q = bd.brand_query("test锤子")
    bd.brand_hide("test锤子001")
    q = bd.brand_query("test锤子001", 6)
    print(q)
    driver.quit()
