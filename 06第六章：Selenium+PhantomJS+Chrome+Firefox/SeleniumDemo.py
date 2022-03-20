#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumDemo.py
@Time    : 2022/3/21 20:27
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : SeleniumDemo
"""
from selenium import webdriver

# 火狐浏览器
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')

# 谷歌浏览器
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
