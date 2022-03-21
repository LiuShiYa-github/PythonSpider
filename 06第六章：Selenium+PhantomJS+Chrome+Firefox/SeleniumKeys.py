#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumKeys.py
@Time    : 2022/3/24 23:35
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : selenium模拟键盘行为
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
# 1 在搜索框中输入赵丽颖
browser.find_element_by_id('kw').send_keys('赵丽颖')
# 2 输入空格
browser.find_element_by_id('kw').send_keys(Keys.SPACE)
# 3 ctrl+a 模拟全选
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# 4 ctrl+c 模拟复制
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')
# 5 ctrl+v 模拟粘贴
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
# 6 输入回车代替搜索按钮
browser.find_element_by_id('kw').send_keys(Keys.ENTER)


