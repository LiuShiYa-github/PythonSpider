#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: MouseSelenium.py
@Time    : 2022/3/24 23:46
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : selenium模拟鼠标操作
"""

from selenium import webdriver
from selenium.webdriver import ActionChains

# 1 打开浏览器,输入百度地址
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='https://www.baidu.com')
# 2 移动到设置节点
set_node = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(to_element=set_node).perform()
# 3 查找高级搜索节点并点击
driver.find_element_by_link_text('高级搜索').click()
