#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: demo.py
@Time    : 2022/4/28 21:39
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : demo演示
"""
from urllib import request

# 1、定义常用变量
url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
# 2、包装请求
req = request.Request(url=url, headers=headers)
# 3、发送请求
res = request.urlopen(req)
# 4、获取响应内容
html = res.read().decode()
print(html)
