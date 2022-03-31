#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: run.py
@Time    : 2022/3/31 10:59
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 17695691664@163.com
@Des     : 
"""
from scrapy import cmdline

cmdline.execute('scrapy crawl daomu'.split())