#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: MultithreadingDemo.py
@Time    : 2022/3/20 18:05
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 多线程Demo
"""

from threading import Thread


def spider():
	print('你爱我呀我爱你,蜜雪冰城甜蜜蜜~')


t_list = []
for i in range(5):
	t = Thread(target=spider)
	t_list.append(t)
	t.start()

for i in t_list:
	t.join()
