import time


def query(driver, supplier):
    driver.find_element_by_css_selector("#_easyui_textbox_input1").clear()
    driver.find_element_by_css_selector("#_easyui_textbox_input1").send_keys(supplier)
    time.sleep(1)
    driver.find_element_by_css_selector("#button_search").click()
    time.sleep(1)
    try:
        a = driver.find_element_by_xpath(".//*[@class='datagrid-btable']/tbody/tr/td[3]/div").text
        print("查询到供应商：%s" % a)
        return a
    except:
        print("查询供应商失败")
        return ""