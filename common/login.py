import time


def login(driver, usr="admin", pwd="123456"):
    driver.find_element_by_css_selector(".formBox>form>input:nth-child(1)").send_keys(usr)
    time.sleep(1)
    driver.find_element_by_css_selector(".formBox>form>input:nth-child(3)").send_keys(pwd)
    time.sleep(1)
    driver.find_element_by_css_selector(".formBox>form>input:nth-child(5)").click()