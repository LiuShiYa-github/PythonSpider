#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: run.py
@Time    : 2022/3/29 14:29
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 
"""

from scrapy import cmdline

cmdline.execute('scrapy crawl che168-middlewares'.split())
