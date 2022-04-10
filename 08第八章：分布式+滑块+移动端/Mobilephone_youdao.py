#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: Mobilephone_youdao.py
@Time    : 2022/4/9 20:01
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 17695691664@163.com
@Des     : 手机端有道翻译结果抓取
"""
import requests
from lxml import etree

url = 'http://m.youdao.com/translate'
word = input("请输入要翻译的单词:")
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}

data = {
    'inputtext': word,
    'type': 'AUTO'
}
html = requests.post(url=url, headers=headers, data=data).text
p = etree.HTML(html)
result = p.xpath('//ul[@id="translateResult"]/li/text()')[0].strip()
print(result)
