#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: MultilevelPageMultithreading.py
@Time    : 2022/3/20 19:32
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 多线程抓取多级页面 --- 腾讯招聘
"""
import requests
import time
from threading import Thread, Lock
from queue import Queue
from urllib import parse
from fake_useragent import UserAgent


class MultilevelPageMultithreading:
	""" 多线程抓取多级页面 --- 腾讯招聘 """
	
	def __init__(self):
		self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1647777009701&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
		self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1647777072080&postId={}&language=zh-cn'
		self.num = 0
		# 2个队列
		self.one_q = Queue()
		self.two_q = Queue()
		# 2把锁
		self.lock1 = Lock()
		self.lock2 = Lock()
	
	def get_html(self, url):
		""" 功能函数1 - 获取响应内容 """
		headers = {'User-Agent': UserAgent().random}
		html = requests.get(url=url, headers=headers).json()
		
		return html
	
	def url_in(self):
		""" 一级页面url地址入队列 """
		keyword = input('请输入要要查询的岗位类别:')
		keyword = parse.quote(keyword)
		# 获取总页数
		total = self.get_total(keyword=keyword)
		for page in range(1, total + 1):
			url = self.one_url.format(keyword, page)
			self.one_q.put(url)
	
	def get_total(self, keyword):
		""" 获取某个列表的总页数 """
		url = self.one_url.format(keyword, 1)
		html = self.get_html(url=url)
		count = html['Data']['Count']
		total = count // 10 if count % 10 == 0 else count // 10 + 1
		
		return total
	
	def parse_one_page(self):
		""" 一级页面解析函数: 提取postid,并拼接二级页面url地址,入队列 """
		while True:
			# 上锁
			self.lock1.acquire()
			if not self.one_q.empty():
				one_url = self.one_q.get()
				# 释放锁
				self.lock1.release()
				one_html = self.get_html(url=one_url)
				# one_html中有10个postid
				for one_job in one_html['Data']['Posts']:
					postid = one_job['PostId']
					job_url = self.two_url.format(postid)
					# 将职位信息入队列
					self.two_q.put(job_url)
			else:
				self.lock1.release()
				break
				
	
	def parse_two_page(self):
		""" 二级页面解析函数:提取具体的职位信息 """
		while True:
			try:
				self.lock2.acquire()
				two_url = self.two_q.get(timeout=1)
				self.lock2.release()
				two_html = self.get_html(url=two_url)
				item = {'名称': two_html['Data']['RecruitPostName'], '类型': two_html['Data']['CategoryName'],
				        '要求': two_html['Data']['Requirement'], '职责': two_html['Data']['Responsibility'],
				        '地址': two_html['Data']['LocationName'], '发布时间': two_html['Data']['LastUpdateTime']}
				self.lock2.acquire()
				self.num += 1
				self.lock2.release()
				print(item)
			except Exception as e:
				self.lock2.release()
				break
				
	def run(self):
		""" 程序的入口函数 """
		self.url_in()
		# 创建多线程
		t1_list = []
		t2_list = []
		for i in range(10):
			t1 = Thread(target=self.parse_one_page)
			t1_list.append(t1)
			t1.start()
			
		for i in range(10):
			t2 = Thread(target=self.parse_two_page)
			t2_list.append(t2)
			t2.start()
		
		for t1 in t1_list:
			t1.join()
		
		for t2 in t2_list:
			t2.join()


if __name__ == '__main__':
	start_time = time.time()
	spider = MultilevelPageMultithreading()
	spider.run()
	end_time = time.time()
	print('time:%2.f' % (end_time - start_time))
	print('一共有{}个职位信息'.format(spider.num))
