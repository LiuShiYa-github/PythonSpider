#!/usr/bin/env python3.8.8
# -*- encoding: utf-8 -*-
'''
@File    :   spider-test.py
@Time    :   2022/02/07 16:49:51
@Author  :   热气球
@Version :   1.0
@Contact :   17695691664@163.com
'''

"""
猫眼电影经典影片 按照热门排序
"""

from urllib import request
import random
import time
import re
import pymongo


class MaoyanSpider_Classic_Film:
	def __init__(self):
		self.url = 'https://www.maoyan.com/films?showType=3&sortId=1&offset={}'
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
			'Cookie': 'uuid_n_v=v1; uuid=3AE37E108CA611EC8FDC8396A0F7AFFCD945C250A076432C8AFD89FCB0E193D7; _csrf=ebdd97cd428809914f8919dcfe0c1031f72c3caf9b01aa03d9c831fae4dffd7f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1644740619; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1644765969; _lxsdk_cuid=17ef22e2f1fc8-0bb075b44e2f43-4c3e237c-144000-17ef22e2f1f27; _lxsdk=3AE37E108CA611EC8FDC8396A0F7AFFCD945C250A076432C8AFD89FCB0E193D7; __mta=150189705.1644740620254.1644765647349.1644765969306.80; _lxsdk_s=17ef39966be-c29-c61-4a0%7C%7C43'
		}
		self.i = 0
		self.conn = pymongo.MongoClient(host='10.0.0.101', port=27017)
		self.db = self.conn['maoyandb']
		self.myset = self.db['maoyanset']
	
	def get_html(self, url):
		"获取HTML内容"
		req = request.Request(url=url, headers=self.headers)
		res = request.urlopen(req)
		html = res.read().decode()
		# print(html)
		# 直接调用解析函数
		self.parse_html(html)
	
	def parse_html(self, html):
		"提取HTML内容"
		regex = '<div class="movie-hover-info">.*?<span class="name ">(.*?)</span>.*?<span class="score channel-detail-orange"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></span>.*?<span class="hover-tag">类型:</span>(.*?)</div>.*?<span class="hover-tag">主演:</span>(.*?)</div>.*?<span class="hover-tag">上映时间:</span>(.*?)</div>.*?</div>'
		pattern = re.compile(regex, re.S)
		r_list = pattern.findall(html)
		# 调用数据处理函数
		self.save_html(r_list)
	
	def save_html(self, r_list):
		"数据处理函数"
		for r in r_list:
			item = {}
			item['name'] = r[0].strip()
			item['score'] = r[1].strip() + r[2].strip()
			item['type'] = r[3].strip()
			item['star'] = r[4].strip()
			item['time'] = r[5].strip()
			print(item)
			self.myset.insert_one(item)
			self.i += 1
	
	def run(self):
		"程序运行调配"
		for page in range(0, 91, 10):
			self.get_html(url=self.url.format(page * 30))
			time.sleep(random.randint(1, 2))


if __name__ == '__main__':
	spider = MaoyanSpider_Classic_Film()
	spider.run()
	print('电影数量：', spider.i)
