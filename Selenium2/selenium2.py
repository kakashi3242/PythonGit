# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

'''
打开浏览器登录
'''
driver = webdriver.Firefox()
driver.get('http://test3.100jit.com')

driver.find_element_by_id('contact').click()
# driver.find_element_by_id('username').send_keys('15757870527')
driver.find_element_by_id('username').send_keys('15267854116')
driver.find_element_by_id('password').send_keys('111111.')
driver.find_element_by_class_name('login-btn').click()

# 查询目的港为DUBAI的整箱运价
driver.find_element_by_id('dischargeport').send_keys('DUBAI')
driver.find_element_by_id('search_home').click()
# above = driver.find_element_by_xpath(".//*[@id='menu']/ul/li[3]/a")
# ActionChains(driver).move_to_element(above).perform()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='advancedSearch']/div/s").click()
# elem = driver.find_element_by_xpath(".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[1]/a")
# elem = driver.find_element_by_xpath(".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[1]/a")
# elem = driver.find_element_by_id("js-result-data-table")
# elem = driver.find_element_by_tag_name('tbody')
# print(elem)
"""
遍历运价查询
"""
#
#
# def yunjia_search(xpath, close_path):
#     above = driver.find_element_by_xpath(".//*[@id='menu']/ul/li[2]/a")
#     ActionChains(driver).move_to_element(above).perform()
#     time.sleep(3)
#     driver.find_element_by_xpath(xpath).click()
#     time.sleep(3)
#     driver.find_element_by_xpath(close_path).click()
#
# xpath1 = ".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[1]/a"
# xpath2 = ".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[2]/a"
# xpath3 = ".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[3]/a"
# xpath4 = ".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[4]/a"
# close_path = "html/body/div[4]/div/div[1]/a[2]"
# yunjia_search(xpath1, close_path)
# yunjia_search(xpath2, close_path)
# yunjia_search(xpath3, close_path)
# yunjia_search(xpath4, close_path)

# xpath2 = ".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[2]/a"
# yunjia(xpath2)
# above = driver.find_element_by_xpath(".//*[@id='menu']/ul/li[2]/a")
# ActionChains(driver).move_to_element(above).perform()
# time.sleep(1)
# driver.find_element_by_xpath(
#     ".//*[@id='menu']/ul/li[2]/div/table/tbody/tr/td[1]/ol/li[3]/a").click()
# time.sleep(1)
# checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
# for checkbox in checkboxes:
#    checkbox.click()
# driver.find_element_by_xpath(".//*[@id='j-tableMenu']/a[6]/span").click()
# check_box = driver.find_element_by_xpath(
#     ".//*[@id='fclmaintain_home1']/tbody/tr[1]/td[2]/input").click()
# check_box.click()
#
# driver.find_element_by_xpath(".//*[@id='j-tableMenu']/a[6]/span").click()
