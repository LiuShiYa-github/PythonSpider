#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: HuaweiApp.py
@Time    : 2022/3/20 11:53
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 抓取华为应用市场社交类app
"""

import requests
import time
import random
from fake_useragent import UserAgent


class HuaweiApp:
	""" 抓取华为应用市场社交类app """
	
	def __init__(self):
		self.url = 'https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum={}&uri=79bd417da03d470287c0c7c2ef8f2c96&maxResults=25&zone=&locale=zh'
		self.headers = {'User-Agent': UserAgent().random}
		self.num = 0
	
	def get_html(self, url):
		""" 请求获取响应内容 """
		# 此处使用JSON直接获取python数据类型
		html = requests.get(url=url, headers=self.headers).json()
		self.parse_html(html=html)
	
	def parse_html(self, html):
		""" 解析函数 """
		item = {}
		for app_dict in html['layoutData']:
			for app_info in app_dict['dataList']:
				item['名称'] = app_info['name']
				item['类型'] = app_info['kindName']
				item['代言词'] = app_info['memo']
				item['下载次数'] = app_info['downCountDesc']
				item['下载链接'] = 'https://appstore.huawei.com/app/{}'.format(
					app_info['downloadRecommendUri'].split('|')[1])
				self.num += 1
				print(item)
			exit(1)
	
	def run(self):
		for page in range(1, 17):
			url = self.url.format(page)
			self.get_html(url=url)
			time.sleep(random.randint(1, 2))


if __name__ == '__main__':
	spider = HuaweiApp()
	spider.run()
	print('一共有{}个社交类app'.format(spider.num))