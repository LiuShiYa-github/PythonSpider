#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumLoginDouban.py
@Time    : 2022/3/25 11:07
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 17695691664@163.com
@Des     : 使用selenium模拟登陆豆瓣网
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://www.douban.com/')
driver.maximize_window()
# 1、切换到iframe
iframe_node = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame(iframe_node)
# 2、找到密码登录并点击
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
# 3、用户名、密码、登录豆瓣
driver.find_element_by_id('username').send_keys('17695691664')
driver.find_element_by_id('password').send_keys('liushiya111')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
driver.quit()
