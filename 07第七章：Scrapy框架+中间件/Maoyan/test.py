# -*- coding: utf-8 -*-
"""
@FileName: test.py
@Time    : 2022/3/27 13:12
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 猫眼电影经典影片 按照热门排序
"""

import random
import re
import time
import requests


class MaoyanSpider_Classic_Film:
	def __init__(self):
		# self.url = 'https://www.maoyan.com/films?showType=3&sortId=1&offset={}'
		self.url = 'https://www.maoyan.com/films?sortId=0&showType=3&requestCode=12e952b5da08da3a591c9940dd807f5cqkvmp&offset={}'
		print(self.url)
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
			'Cookie': '_lxsdk_cuid=17f16596927c8-0466fea13319f6-576153e-144000-17f16596927c8; uuid_n_v=v1; uuid=24C0B070AD8B11EC88953B756A5CE0494251FCC185FA4D9DA4C13E9CE72F5ECE; _csrf=8d4b89a143266ce8e9037d8ce1c94c92e03d8e50a82f318bdb69ce997edcdbd8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1647870387,1648357368; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=24C0B070AD8B11EC88953B756A5CE0494251FCC185FA4D9DA4C13E9CE72F5ECE; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1648358950; __mta=150960649.1645347489665.1648358149258.1648358950325.25; _lxsdk_s=17fc9c16146-265-a54-e46%7C%7C20'
		}
		self.i = 0
	
	def get_html(self, url):
		"""获取HTML内容"""
		html = requests.get(url=url, headers=self.headers)
		html.encoding = "utf-8"
		# print(html.text)
		# 直接调用解析函数
		self.parse_html(html.text)
	
	def parse_html(self, html):
		"""提取HTML内容"""
		regex = '<div class="movie-hover-info">.*?<span class="name ">(.*?)</span>.*?<span class="score channel-detail-orange"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></span>.*?<span class="hover-tag">类型:</span>(.*?)</div>.*?<span class="hover-tag">主演:</span>(.*?)</div>.*?<span class="hover-tag">上映时间:</span>(.*?)</div>.*?</div>'
		pattern = re.compile(regex, re.S)
		r_list = pattern.findall(html)
		# 调用数据处理函数
		self.save_html(r_list)
	
	def save_html(self, r_list):
		"""数据处理函数"""
		for r in r_list:
			item = {}
			try:
				item['name'] = r[0].strip()
				item['score'] = r[1].strip() + r[2].strip()
				item['type'] = r[3].strip()
				item['star'] = r[4].strip()
				item['time'] = r[5].strip()
				print(item)
				self.i += 1
			except UnicodeError as e:
				print(e)
	
	def run(self):
		"""程序运行调配"""
		for page in range(0, 91, 10):
			self.get_html(url=self.url.format(page * 30))
			time.sleep(random.randint(1, 2))


if __name__ == '__main__':
	spider = MaoyanSpider_Classic_Film()
	spider.run()
	print('电影数量：', spider.i)
