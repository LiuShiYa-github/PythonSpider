#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumChromeMaoyanTop100.py
@Time    : 2022/3/21 21:51
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 使用selenium抓取好友的所有博客
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://hz.lianjia.com/ershoufang/pg1/')
driver.maximize_window()
dd_list = driver.find_elements_by_xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]')
for dd in dd_list:
	print(dd.text)
	print('*' * 50)
	# one_film_list = dd.text.split('\n')
	# item = {}
# 	item['文章名'] = one_film_list[0]
# 	item['文章简介'] = one_film_list[1]
# 	item['作者'] = one_film_list[2]
# 	item['日期'] = one_film_list[3]
# 	print(item)


driver.quit()
