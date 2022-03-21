#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumChromeMaoyanTop100.py
@Time    : 2022/3/21 21:51
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 使用selenium抓取猫眼电影top100
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(url='https://www.maoyan.com/films?showType=3')
driver.maximize_window()
time.sleep(3)
driver.quit()
