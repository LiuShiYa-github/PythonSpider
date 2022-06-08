#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: Myflask.py
@Time    : 2022/6/8 10:42
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 初识Flask
"""

from flask import Flask, render_template

import random
import time
import requests
from fake_useragent import UserAgent

url = "https://weibo.com/ajax/statuses/hot_band"
headers = {'User-Agent': UserAgent().random}
html = requests.get(url=url, headers=headers, timeout=3).json()
list_info = []

time.sleep(random.uniform(0, 3))
for i in range(10):
    try:
        lt = []
        lt = [html['data']['band_list'][i]['note'], html['data']['band_list'][i]['raw_hot']]
        list_info.append(lt)
    except Exception as e:
        pass
print(list_info)
app = Flask(__name__)


@app.route("/")
def index():
    data = list_info
    return render_template('show.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
