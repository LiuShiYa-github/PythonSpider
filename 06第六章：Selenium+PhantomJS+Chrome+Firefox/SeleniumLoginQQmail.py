#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumLoginQQmail.py
@Time    : 2022/3/25 11:26
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 使用selenium模拟登录QQ邮箱
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://mail.qq.com/')
driver.maximize_window()
# 1 切换iframe子页面
driver.switch_to.frame('login_frame')
# 2 用户名密码登录
driver.find_element_by_id('u').send_keys('xxx')
time.sleep(2)
driver.find_element_by_id('p').send_keys('xxx')
time.sleep(2)
driver.find_element_by_id('login_button').click()
# driver.quit()