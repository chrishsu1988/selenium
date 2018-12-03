import time


def add(driver, supplier):
    driver.find_element_by_xpath(".//*[@id='menu_accordion']/div[4]/div[1]/div[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='menu_accordion']/div[4]/div[2]/ul/li").click()
    time.sleep(1)
    driver.switch_to.frame("mainFrame_1")
    time.sleep(1)
    driver.find_element_by_css_selector("#button-add").click()
    time.sleep(1)
    driver.find_element_by_css_selector("#_easyui_textbox_input2").send_keys(supplier)
    time.sleep(1)
    driver.find_element_by_css_selector("#add_submit_form").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='opter_layout']/div[11]/div[3]/a").click()