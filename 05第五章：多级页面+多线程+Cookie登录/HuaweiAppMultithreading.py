#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: HuaweiAppMultithreading.py
@Time    : 2022/3/20 18:49
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 多线程抓取华为应用市场社交类app
"""
import requests
import time
import random
from fake_useragent import UserAgent
from threading import Thread, Lock
from queue import Queue


class HuaweiAppMultithreading:
	""" 多线程抓取华为应用市场社交类app """
	
	def __init__(self):
		self.url = 'https://web-drcn.hispace.dbankcloud.cn/uowap/index?method=internal.getTabDetail&serviceType=20&reqPageNum={}&uri=79bd417da03d470287c0c7c2ef8f2c96&maxResults=25&zone=&locale=zh'
		self.headers = {'User-Agent': UserAgent().random}
		self.num = 0
		# 创建队列
		self.q = Queue()
		self.lock = Lock()
	
	def url_in(self):
		""" url地址入队列 """
		for page in range(1, 17):
			url = self.url.format(page)
			# 入队列
			self.q.put(url)
	
	def parse_html(self):
		""" 线程事件:获取URL,请求 解析 处理数据 """
		while True:
			# 上锁
			self.lock.acquire()
			if not self.q.empty():
				url = self.q.get()
				# 释放锁
				self.lock.release()
				html = requests.get(url=url, headers=self.headers).json()
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
			else:
				# 当队列为空时,已经上锁但未释放
				self.lock.release()
				break
	
	def run(self):
		# 先让url地址入队列
		self.url_in()
		# 创建多线程运行
		t_list = []
		for i in range(1):
			t = Thread(target=self.parse_html)
			t_list.append(t)
			t.start()
			
		for t in t_list:
			t.join()
			

if __name__ == '__main__':
	start_time = time.time()
	spider = HuaweiAppMultithreading()
	spider.run()
	end_time = time.time()
	print('time:%2.f' % (end_time - start_time))
	print('一共有{}个社交类app'.format(spider.num))