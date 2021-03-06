#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: JdSeleniumSpider.py
@Time    : 2022/3/24 22:35
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 使用selenium抓取京东商城爬虫类的图书
"""

from selenium import webdriver
import time


class JdSpider:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get(url='https://www.jd.com')
		# 搜索框发送:爬虫书 点击搜索按钮
		self.driver.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
		self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
		# 应该要给页面加载元素预留时间
		time.sleep(1)
	
	def parse_html(self):
		""" 具体提取数据 """
		# 先把滚动条拉到最底部,等待所有商品加载完成再进行数据提取
		self.driver.execute_script(
			'window.scrollTo(0,document.body.scrollHeight)'
		)
		time.sleep(3)
		# 2 提取具体的数据
		li_list = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
		for li in li_list:
			try:
				item = {}
				item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]/strong').text.strip()
				item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
				item['commit'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
				item['shop'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]/a').text.strip()
				print(item)
			except Exception as e:
				print(e)
	
	def run(self):
		while True:
			self.parse_html()
			# 判断是否到最后一页
			if self.driver.page_source.find('pn-next disabled') == -1:
				self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
				time.sleep(1)
			else:
				self.driver.quit()
				break
		self.parse_html()


if __name__ == '__main__':
	spider = JdSpider()
	spider.run()
