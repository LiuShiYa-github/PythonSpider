#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: WeiboFlask.py
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


def show_hot():
    url = "https://weibo.com/ajax/statuses/hot_band"
    headers = {'User-Agent': UserAgent().random}
    html = requests.get(url=url, headers=headers, timeout=3).json()
    list_info_hot = []

    time.sleep(random.uniform(0, 3))
    for i in range(20):
        try:
            lt = []
            lt = [html['data']['band_list'][i]['raw_hot'], html['data']['band_list'][i]['note']]
            list_info_hot.append(lt)
        except Exception as e:
            pass
    print(list_info_hot)
    return list_info_hot


def show_type():
    url = "https://weibo.com/ajax/statuses/hot_band"
    headers = {'User-Agent': UserAgent().random}
    html = requests.get(url=url, headers=headers, timeout=3).json()
    list_info_type = []

    time.sleep(random.uniform(0, 3))
    for i in range(50):
        try:
            list_info = (html['data']['band_list'][i]['category']).split(',')
            for i in list_info:
                list_info_type.append(i)
        except Exception as e:
            pass
    # 拼凑出字典
    myset = set(list_info_type)
    list_type = []
    for item in myset:
        dic_type = {'name': item, 'value': list_info_type.count(item)}
        list_type.append(dic_type)
    print(list_type)
    return list_type


app = Flask(__name__)


@app.route("/show_hot")
def index_hot():
    hot_data = show_hot()
    return render_template('show_hot.html', data=hot_data)


@app.route("/show_type")
def index_type():
    type_data = show_type()
    return render_template("show_type.html", data=type_data)


if __name__ == '__main__':
    app.run(debug=True)
