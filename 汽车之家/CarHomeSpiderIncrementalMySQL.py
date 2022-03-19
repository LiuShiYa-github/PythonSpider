#!/usr/bin/env python3.8.8
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2022/02/15 08:19:32
@Author  :   热气球
@Version :   1.0
@Contact :   17695691664@163.com
'''

# C:/Users/shiya.liu/AppData/Local/Programs/Python/Python38/python.exe -m pip install
# here put the import lib


"""
汽车之家数据抓取-两级页面
爬取目标：车的型号、形势里程、上牌时间、挡位、排量、车辆所在地
第一页：https://www.che168.com/china/a0_0msdgscncgpi1ltocsp1exx0/?pvareaid=102179#currengpostion
第二页：https://www.che168.com/china/a0_0msdgscncgpi1ltocsp2exx0/?pvareaid=102179#currengpostion
第三页：https://www.che168.com/china/a0_0msdgscncgpi1ltocsp3exx0/?pvareaid=102179#currengpostion
"""

from urllib import request
import re
import time
import random
import pymysql
from hashlib import md5
import sys


class CarHomeSpiderIncrementalMySQL:
    def __init__(self):
        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
        }
        # 技术变量
        self.i = 0
        # 数据库相关变量
        self.db = pymysql.connect(host='10.0.0.101', user='root', password='123456', database='cardb', charset='utf8')
        self.cursor = self.db.cursor()
        # 定义item为空字典
        self.item = {}

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
                url_md5 = self.md5_url(href)
                sel = 'select * from request_finger where finger=%s'
                self.cursor.execute(sel, [url_md5])
                result = self.cursor.fetchall()
                # result为空元组的情况，表示之前没有抓取过
                if not result:
                    self.item = {}
                    self.get_data(car_url=href)
                    # 如果不为空则插入
                    if self.item:
                        ins = 'insert into request_finger values(%s)'
                        self.cursor.execute(ins, [url_md5])
                        self.db.commit()
                else:
                    sys.exit('抓取完成')
            else:
                car_url = 'https://www.che168.com' + href
                url_md5 = self.md5_url(car_url)
                sel = 'select * from request_finger where finger=%s'
                self.cursor.execute(sel, [url_md5])
                result = self.cursor.fetchall()
                if not result:
                    self.item = {}
                    self.get_data(car_url=car_url)
                    if self.item:
                        ins = 'insert into request_finger values(%s)'
                        self.cursor.execute(ins, [url_md5])
                        self.db.commit()
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
            ins = 'insert into cartab values(%s,%s,%s,%s,%s,%s)'
            li = [
                self.item['name'],
                self.item['km'],
                self.item['time'],
                self.item['type'],
                self.item['city'],
                self.item['price'],
            ]
            self.cursor.execute(ins, li)
            self.db.commit()
            print(self.item)
        except IndexError as e:
            print('--------->', e)

    def run(self):
        """程序的入口函数"""
        for i in range(1, 5):
            url = self.url.format(i)
            self.parse_html(url)
        # 断开数据库
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    spider = CarHomeSpiderIncrementalMySQL()
    spider.run()
