#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: MaoyanFilmFlask.py
@Time    : 2022/6/8 21:37
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 
"""
# !/usr/bin/env python3.8.8
# -*- encoding: utf-8 -*-
"""
@File    :   spider-test.py
@Time    :   2022/02/07 16:49:51
@Author  :   热气球
@Version :   1.0
@Contact :   2573514647@qq.com
"""

"""
猫眼电影经典影片 按照热门排序
"""
from flask import Flask, render_template
import random
import re
import time
from urllib import request


def get_info():
    list_info = []
    for page in range(0, 91, 10):
        url = 'https://www.maoyan.com/films?showType=3&sortId=1&offset={}'.format(page * 30)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Cookie': 'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1648430918; _lxsdk_cuid=17e9fe22a08c8-070607354480fd-c343365-1fa400-17e9fe22a08c8; _lxsdk=63BEABF0AE3611ECAE06EF84F7388A3FDC613A38511A4011A056BE32E482E41B; __mta=210679466.1648430918411.1648433444390.1648433592567.21; uuid_n_v=v1; uuid=051308B0E73111ECBA196766E70FEE9959542C3890534DBDA8CB30C789A4F19A'
        }
        time.sleep(random.randint(1, 2))
        try:
            req = request.Request(url=url, headers=headers)
            res = request.urlopen(req)
            html = res.read().decode("utf-8", 'ignore')
            regex = '<div class="movie-hover-info">.*?<span class="name ">(.*?)</span>.*?<span class="score channel-detail-orange"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></span>.*?<span class="hover-tag">类型:</span>(.*?)</div>.*?<span class="hover-tag">主演:</span>(.*?)</div>.*?<span class="hover-tag">上映时间:</span>(.*?)</div>.*?</div>'
            pattern = re.compile(regex, re.S)
            r_list = pattern.findall(html)
        except UnicodeEncodeError as e:
            print(e)
        for r in r_list:
            film_list = r[3].strip().split('／')
            for i in film_list:
                list_info.append(i)

    myset = set(list_info)
    list_type = []
    for item in myset:
        dic_type = {'name': item, 'value': list_info.count(item)}
        list_type.append(dic_type)
    print(list_type)
    return list_type


app = Flask(__name__)


@app.route("/")
def index_hot():
    list_type = get_info()
    return render_template('film_type.html', data=list_type)


if __name__ == '__main__':
    app.run(debug=True)
