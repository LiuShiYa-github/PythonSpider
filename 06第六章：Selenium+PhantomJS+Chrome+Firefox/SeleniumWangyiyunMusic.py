#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SeleniumWangyiyunMusic.py
@Time    : 2022/3/25 12:24
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 17695691664@163.com
@Des     : 抓取网易云音乐排行榜
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://music.163.com/#/discover/toplist')
driver.switch_to.frame('contentFrame')
tr_list = driver.find_elements_by_xpath('//table/tbody/tr')
for tr in tr_list:
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text.strip()
    item['name'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').strip().replace('\xa0', ' ')
    item['time'] = tr.find_element_by_xpath('.//span[@class="u-dur "]').text.strip()
    item['star'] = tr.find_element_by_xpath('.//div[@class="text"]/span').get_attribute('title').strip()
    print(item)



