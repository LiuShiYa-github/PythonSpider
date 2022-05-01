#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: PostYoudaoTranslate.py
@Time    : 2022/3/19 20:11
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 有道翻译结果抓取
"""
import requests
import time
import random
from hashlib import md5


class PostYoudaoTranslate:
	def __init__(self):
		# post_url:浏览器F12抓取到的POST地址
		self.post_url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
		self.headers = {
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Connection': 'keep-alive',
			'Content-Length': '252',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie': 'OUTFOX_SEARCH_USER_ID=-2011095651@10.110.96.157; JSESSIONID=aaa3D7ZIRV27NfAOoPH_x; OUTFOX_SEARCH_USER_ID_NCOO=859081232.0887973; fanyi-ad-id=305110; fanyi-ad-closed=1; ___rl__test__cookies=1647690518973',
			'Host': 'fanyi.youdao.com',
			'Origin': 'https://fanyi.youdao.com',
			'Referer': 'https://fanyi.youdao.com/',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest',
		}
	
	def md5_string(self, string):
		""" 功能函数:对字符串进行md5的加密 """
		s = md5()
		s.update(string.encode())
		
		return s.hexdigest()
	
	def get_ts_salt_sign(self, word):
		""" 获取ts salt sign """
		ts = str(int(time.time() * 1000))
		salt = ts + str(random.randint(0, 9))
		string = "fanyideskweb" + word + salt + "Ygy_4c=r#e#4EX^NUGUc5"
		sign = self.md5_string(string)
		
		return ts, salt, sign
	
	def attack_yd(self, word):
		ts, salt, sign = self.get_ts_salt_sign(word)
		data = {
			'i': word,
			'from': 'AUTO',
			'to': 'AUTO',
			'smartresult': 'dict',
			'client': 'fanyideskweb',
			'salt': salt,
			'sign': sign,
			'lts': ts,
			'bv': '75adedb929794295187b046da37b1fc1',
			'doctype': 'json',
			'version': '2.1',
			'keyfrom': 'fanyi.web',
			'action': 'FY_BY_REALTlME'
		}
		# .json():作用是把一个json格式的字符串转为python数据类型
		html = requests.post(url=self.post_url, data=data, headers=self.headers).json()
		print(html['translateResult'][0][0]['tgt'])
	
	def run(self):
		word = input('请输入要翻译的单词:')
		self.attack_yd(word)


if __name__ == '__main__':
	spider = PostYoudaoTranslate()
	spider.run()
