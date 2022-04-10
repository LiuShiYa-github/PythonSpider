#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: CarHomeSpiderIncrementalRedis.py
@Time    : 2022/4/10 22:35
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 基于Redis实现增量爬虫
"""
from urllib import request
from hashlib import md5
import re
import time
import random
import sys
import redis


class CarHomeSpiderIncrementalMySQL:
    def __init__(self):
        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
        }
        # Redis相关变量
        self.r = redis.Redis(host='10.0.0.101', port=6379, db=0, password=123456)

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

    def md5_url(self, url):
        """功能函数3：对URL地址进行md5加密"""
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def parse_html(self, one_url):
        """数据抓取函数，从一级页面解析开始"""
        one_html = self.get_html(one_url)
        one_regex = '<li class="cards-li list-photo-li.*?<a href="(.*?)".*?</li>'
        href_list = self.re_func(one_regex, one_html)
        for href in href_list:
            if 'https://semnt.autohome.com.cn/' in href:
                finger = self.md5_url(href)
                if self.r.sadd('carspider:finger', finger) == 1:
                    self.get_data(car_url=href)
                else:
                    sys.exit('抓取完成')
            else:
                car_url = 'https://www.che168.com' + href
                finger = self.md5_url(car_url)
                if self.r.sadd('carspider:finger', finger) == 1:
                    self.get_data(car_url=car_url)
                else:
                    sys.exit('抓取完成')
            # 抓取1辆汽车的信息，随机休眠1-5秒钟
            time.sleep(random.uniform(0, 5))

    def get_data(self, car_url):
        """功能：抓取1辆汽车的详情信息"""
        two_html = self.get_html(car_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">(.*?)<b>万</b><i class="usedfont used-xiajiantou"></i>.*?'
        car_lsit = self.re_func(two_regex, two_html)
        try:
            self.item = {'name': car_lsit[0][0].strip(), 'km': car_lsit[0][1].strip(), 'time': car_lsit[0][2].strip(),
                         'type': car_lsit[0][3].split('/')[0].strip(), 'city': car_lsit[0][4].strip(),
                         'price': car_lsit[0][5].split(';')[1].strip()}
            print(self.item)
        except IndexError as e:
            print('--------->', e)

    def run(self):
        """程序的入口函数"""
        for i in range(1, 5):
            url = self.url.format(i)
            self.parse_html(url)


if __name__ == '__main__':
    spider = CarHomeSpiderIncrementalMySQL()
    spider.run()