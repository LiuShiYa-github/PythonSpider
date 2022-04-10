#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: xpathdemo.py
@Time    : 2022/4/10 22:36
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : xpath抓取QQ音乐热歌榜
"""
import requests
from lxml import etree

url = 'https://y.qq.com/n/ryqq/toplist/26'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
html = requests.get(url=url, headers=headers).text
item = {}
p = etree.HTML(html)
for r in range(1, 21):
    dd_list = p.xpath('//*[@id="app"]/div/div[2]/div[2]/div[3]/ul[2]/li[{}]'.format(r))
    for i in dd_list:
        item['歌名'] = i.xpath('.//div/div[3]/span/a[2]/text()')[0].strip()
        item['歌手'] = i.xpath('.//div/div[4]/a/text()')[0].strip()
        item['时长'] = i.xpath('.//div/div[5]/text()')[0].strip()
        print(item)
