#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: MaoyanClassicMovieMysql.py
@Time    : 2022/4/10 22:31
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 猫眼电影经典影片 按照热门排序
"""

from urllib import request
import random
import time
import re
import pymysql


class MaoyanSpider_Classic_Film:
    def __init__(self):
        self.url = 'https://www.maoyan.com/films?showType=3&sortId=1&offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
            'Cookie': '__mta=150960649.1645347489665.1648359488006.1648359602267.36; _lxsdk_cuid=17f16596927c8-0466fea13319f6-576153e-144000-17f16596927c8; uuid_n_v=v1; uuid=40676940C88411ECB7121591F0C657D661F33FA860EA4951B337B0151B32BBDE; _csrf=a470cd2799dd3a8cced04ed718e25a055de1dc9e07c539ec0a7a2292a8d0711c; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1651323092; _lxsdk=40676940C88411ECB7121591F0C657D661F33FA860EA4951B337B0151B32BBDE; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1651323108; __mta=150960649.1645347489665.1648359602267.1651323108420.37; _lxsdk_s=1807a86be77-29-ab5-4c5%7C%7C6'
        }
        self.i = 0
        self.db = pymysql.connect(host='10.0.0.101', user='root', password='123456', database='maoyandb', charset='utf8')
        self.cursor = self.db.cursor()

    def get_html(self, url):
        """获取HTML内容"""
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # print(html)
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """提取HTML内容"""
        regex = '<div class="movie-hover-info">.*?<span class="name ">(.*?)</span>.*?<span class="score channel-detail-orange"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></span>.*?<span class="hover-tag">类型:</span>(.*?)</div>.*?<span class="hover-tag">主演:</span>(.*?)</div>.*?<span class="hover-tag">上映时间:</span>(.*?)</div>.*?</div>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # 调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        ins = 'insert into maoyantab values(%s, %s, %s, %s, %s)'
        for r in r_list:
            film_li = [
                r[0].strip(),
                r[1].strip() + r[2].strip(),
                r[3].strip(),
                r[4].strip(),
                r[5].strip()
            ]
            self.cursor.execute(ins, film_li)
            self.db.commit()
            print(film_li)
            self.i += 1

    def run(self):
        """程序运行调配"""
        for page in range(0, 91, 10):
            self.get_html(url=self.url.format(page * 30))
            time.sleep(random.randint(1, 2))
        # 所有页面数据抓取完成后关闭
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    spider = MaoyanSpider_Classic_Film()
    spider.run()
    print('电影数量：', spider.i)