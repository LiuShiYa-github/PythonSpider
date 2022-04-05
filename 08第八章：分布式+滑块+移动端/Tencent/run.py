#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: run.py
@Time    : 2022/4/5 15:31
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : docker run -d -it   -v /root/Tencent:/home/ --name python  python bash
"""
from scrapy import cmdline

cmdline.execute('scrapy crawl tencent'.split())