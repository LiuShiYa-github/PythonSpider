#!/usr/bin/env python3.8.8
# -*- encoding: utf-8 -*-
"""
@File    :   CarHomeSpider.py
@Time    :   2022/02/15 08:19:32
@Author  :   热气球
@Version :   1.0
@Contact :   17695691664@163.com
"""

"""
汽车之家数据抓取-两级页面
爬取目标：车的型号、形势里程、上牌时间、挡位、排量、车辆所在地
第一页：https://www.che168.com/china/a0_0msdgscncgpi1ltocsp1exx0/?pvareaid=102179#currengpostion
第二页：https://www.che168.com/china/a0_0msdgscncgpi1ltocsp2exx0/?pvareaid=102179#currengpostion
第三页：https://www.che168.com/china/a0_0msdgscncgpi1ltocsp3exx0/?pvareaid=102179#currengpostion
"""

import random
import re
import time
from urllib import request

import pymongo


class CarHomeSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
        }
        self.i = 0
        self.conn = pymongo.MongoClient(host='10.0.0.101', port=27017)
        self.db = self.conn['carhomedb']
        self.myset = self.db['carhomeset']

    def get_html(self, url):
        """功能函数1：获取响应内容"""
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('gb18030', 'ignore')
        # html = res.read().decode('utf-8','ignore')

        return html

    def re_func(self, regex, html):
        """功能函数2：解析提取数据"""
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    def parse_html(self, one_url):
        """数据抓取函数，从一级页面解析开始"""
        one_html = self.get_html(one_url)
        one_regex = '<li class="cards-li list-photo-li.*?<a href="(.*?)".*?</li>'
        href_list = self.re_func(one_regex, one_html)
        for href in href_list:
            if 'https://semnt.autohome.com.cn/' in href:
                self.get_data(car_url=href)
            else:
                car_url = 'https://www.che168.com' + href
                self.get_data(car_url=car_url)
            # 抓取1辆汽车的信息，随机休眠1-5秒钟
            time.sleep(random.uniform(0, 5))

    def get_data(self, car_url):
        """功能：抓取1辆汽车的详情信息"""
        two_html = self.get_html(car_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">(.*?)<b>万</b><i class="usedfont used-xiajiantou"></i>.*?'
        car_lsit = self.re_func(two_regex, two_html)
        try:
            item = {'name': car_lsit[0][0].strip(), 'km': car_lsit[0][1].strip(), 'time': car_lsit[0][2].strip(),
                    'type': car_lsit[0][3].split('/')[0].strip(), 'city': car_lsit[0][4].strip(),
                    'price': car_lsit[0][5].split(';')[1].strip()}
            print(item)
            self.myset.insert_one(item)
        except IndexError as e:
            print('--------->', e)

    def run(self):
        """程序的入口函数"""
        for i in range(1, 5):
            url = self.url.format(i)
            self.parse_html(url)


if __name__ == '__main__':
    spider = CarHomeSpider()
    spider.run()
