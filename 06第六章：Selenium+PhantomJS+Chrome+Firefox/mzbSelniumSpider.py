#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: mzbSelniumSpider.py
@Time    : 2022/3/25 0:02
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 使用selenium来抓取xxx最新行政区化代码
"""
from selenium import webdriver
import time


class MzbSpider:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get(url='http://www.mca.gov.cn/article/sj/xzqh/2020/')
		self.i = 0
	
	def parse_html(self):
		self.driver.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[5]/td[2]/a').click()
		time.sleep(2)
		# 切换句柄
		li = self.driver.window_handles
		self.driver.switch_to.window(li[1])
		# 提取数据
		tr_list = self.driver.find_elements_by_xpath('//table//tr')
		try:
			for tr in tr_list[3:]:
				one_city_list = tr.text.split()
				item = {}
				item['name'] = one_city_list[1].strip()
				item['code'] = one_city_list[0].strip()
				self.i += 1
				print(item)
		except Exception as e:
			print(e)
	
	def run(self):
		self.parse_html()


if __name__ == '__main__':
	spider = MzbSpider()
	spider.run()
	print('个数:{}'.format(spider.i))
