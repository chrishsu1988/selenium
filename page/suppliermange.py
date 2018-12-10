from selenium import webdriver
from time import sleep
from common.base import Base


# 供应商管理页面类
class SupplierMange():
    def __init__(self, driver):
        self.driver = driver
        self.b = Base(self.driver)

    # 添加供应商
    def supplier_add(self, supplier):
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[4]/div[1]/div[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[4]/div[2]/ul/li"))
        sleep(1)
        self.b.switch_frame(("id", "mainFrame_1"))
        sleep(1)
        self.b.click(("css selector", "#button-add"))
        sleep(1)
        self.b.send(("css selector", "#_easyui_textbox_input2"), supplier)
        sleep(1)
        self.b.click(("css selector", "#add_submit_form"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[11]/div[3]/a"))

    # 编辑供应商
    def supplier_edit(self,supplier, supplier1):
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[4]/div[1]/div[1]"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='menu_accordion']/div[4]/div[2]/ul/li"))
        sleep(1)
        self.b.switch_frame(("id", "mainFrame_1"))
        sleep(1)
        self.b.clear(("xpath", "#_easyui_textbox_input1"))
        sleep(1)
        self.b.send(("css selector", "#_easyui_textbox_input1"), supplier)
        sleep(1)
        self.b.click(("css selector", "#button_search"))
        sleep(1)
        self.b.click(("css selector", ".datagrid-cell-check>input"))
        sleep(1)
        self.b.click(("css selector", "#button-view"))
        sleep(1)
        self.b.clear(("css selector", "#_easyui_textbox_input3"))
        sleep(1)
        self.b.send(("css selector", "#_easyui_textbox_input3"), supplier1)
        sleep(1)
        self.b.click(("css selector", "#edit_submit_form"))
        sleep(1)
        self.b.click(("xpath", ".//*[@id='opter_layout']/div[11]/div[3]/a"))

    # 查询供应商
    def supplier_query(self, supplier):
        # self.b.click(("xpath", ".//*[@id='menu_accordion']/div[4]/div[1]/div[1]"))
        # sleep(1)
        # self.b.click(("xpath", ".//*[@id='menu_accordion']/div[4]/div[2]/ul/li"))
        # sleep(1)
        # self.b.switch_frame(("id", "mainFrame_1"))
        # sleep(1)
        self.b.clear(("css selector", "#_easyui_textbox_input1"))
        sleep(1)
        self.b.send(("css selector", "#_easyui_textbox_input1"), supplier)
        sleep(1)
        self.b.click(("css selector", "#button_search"))
        sleep(1)
        try:
            a = self.b.get_text(("xpath", ".//*[@class='datagrid-btable']/tbody/tr/td[3]/div"))
            return a
        except:
            return ""


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    sm = SupplierMange(driver)

    from page.loginpage import LoginPage
    lg = LoginPage(driver)
    lg.login()
    # sm.supplier_add("test003")
    # sm.supplier_edit("test003", "test003456")
    sm.supplier_query("test003")
    driver.quit()