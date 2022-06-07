#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: Web_Hot_Search.py
@Time    : 2022/6/7 21:03
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 微博热搜
"""
import random
import time
import requests
from fake_useragent import UserAgent
import urllib.parse


class WebHotSearch:
    def __init__(self):
        self.url = "https://weibo.com/ajax/statuses/hot_band"
        self.headers = {'User-Agent': UserAgent().random}

    def get_html(self):
        html = requests.get(url=self.url, headers=self.headers, timeout=3).json()
        return html

    def parse_html(self, html, i):
        list = {}
        try:
            list['热搜榜'] = html['data']['band_list'][i]['realpos']
            list['标题'] = html['data']['band_list'][i]['note']
            list['链接'] = "https://s.weibo.com/weibo?q=%23{}%23".format(
                urllib.parse.quote(html['data']['band_list'][i]['note']))
            print(list)
        except Exception as e:
            pass

    def run(self):
        html = self.get_html()
        for rank in range(51):
            self.parse_html(html=html, i=rank)
            time.sleep(random.uniform(0, 3))


if __name__ == '__main__':
    spider = WebHotSearch()
    spider.run()
