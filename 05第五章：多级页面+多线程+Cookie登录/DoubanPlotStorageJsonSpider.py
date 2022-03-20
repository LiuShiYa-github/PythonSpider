#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: DoubanPlotStorageJsonSpider.py
@Time    : 2022/3/20 16:28
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 根据用户指定的类型抓取豆瓣全站的电影
"""
import requests
import json
import time
import random
import re
from fake_useragent import UserAgent


class DoubanPlotStorageJsonSpider:
	""" 根据用户指定的类型抓取豆瓣全站的电影 """
	
	def __init__(self):
		self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
		self.num = 0
		self.f = open('douban.json', 'w', encoding='utf-8')
		self.itme_list = []
	
	def get_agent(self):
		""" 功能函数1 - 获取随机User-Agent """
		return UserAgent().random
	
	def get_html(self, url):
		""" 功能函数2 - 获取html """
		html = requests.get(url=url, headers={'User-Agent': self.get_agent()}).text
		
		return html
	
	def parse_html(self, url):
		""" 功能函数3 - 解析html """
		# json.loads() 把json格式的字符串转为python数据类型
		html = json.loads(self.get_html(url=url))
		itme = {}
		for one_file in html:
			itme['名称'] = '《{}》'.format(one_file['title'])
			itme['主演'] = one_file['actors']
			itme['上映时间'] = one_file['release_date']
			itme['评分'] = one_file['score']
			itme['排名'] = one_file['rank']
			itme['国家'] = one_file['regions']
			itme['链接'] = one_file['url']
			print(itme)
			self.num += 1
			self.itme_list.append(itme)
			json.dump(self.itme_list, self.f, ensure_ascii=False)
			
	
	def get_total(self, type):
		""" 获取电影的总数量 """
		page_url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type)
		html = json.loads(self.get_html(url=page_url))
		
		return html['total']
	
	def get_type_dict(self):
		""" 获取电影的类别 """
		url = 'https://movie.douban.com/chart'
		html = self.get_html(url=url)
		regex = '<span><a href=".*?type_name=(.*?)&type=(.*?)&interval_id=100:90&action=">.*?</a></span>'
		pattern = re.compile(regex, re.S)
		r_lsit = pattern.findall(html)
		type_dict = {}
		for r in r_lsit:
			type_dict[r[0]] = r[1]
		return type_dict
	
	def run(self):
		""" 获取电影类别的字典 """
		type_dict = self.get_type_dict()
		menu = ''
		for t in type_dict:
			menu = menu + t + '|'
		print(menu)
		choice = input('请输入电影的类型: ')
		type = type_dict[choice]
		
		""" 运行逻辑 """
		total = self.get_total(type=type)
		for start in range(0, total, 20):
			url = self.url.format(type, start)
			self.parse_html(url=url)
			time.sleep(random.randint(1, 2))
		self.f.close()


if __name__ == '__main__':
	spider = DoubanPlotStorageJsonSpider()
	spider.run()
	print('电影的个数:{}'.format(spider.num))
