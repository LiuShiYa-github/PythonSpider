#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: CarHomeSpider.py
@Time    : 2022/4/10 22:32
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 汽车之家数据抓取-两级页面
"""
from urllib import request
import re
import time
import random


class CarHomeSpider:
    def __init__(self):
        self.url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
            'Cookie': 'userarea=0; listuserarea=0; ahpvno=20; fvlid=16448409775563f5wVFOyojHF; sessionid=fe8e143c-5d08-4286-b2dd-47a499bb7e30; sessionip=58.100.81.5; area=330106; ahuuid=26E0CF41-819F-48AF-9773-780E233F3F61; Hm_lvt_d381ec2f88158113b9b76f14c497ed48=1644840978; Hm_lpvt_d381ec2f88158113b9b76f14c497ed48=1644847499; che_sessionid=72D464C3-BAF6-4470-B548-B50EC8087FC8%7C%7C2022-02-14+20%3A16%3A17.878%7C%7Cwww.autohome.com.cn; v_no=5; visit_info_ad=72D464C3-BAF6-4470-B548-B50EC8087FC8||BEADF579-BFBC-439B-9150-42C94B1AADBC||-1||-1||5; che_ref=www.autohome.com.cn%7C0%7C100533%7C0%7C2022-02-14+22%3A04%3A59.043%7C2022-02-14+20%3A16%3A17.878; showNum=20; UsedCarBrowseHistory=0%3A42132005%2C0%3A42916651%2C0%3A42387464%2C0%3A42583492%2C0%3A42962517; carDownPrice=1; sessionvisit=c1f632d9-2fee-4378-8b1c-3aa0984812fd; sessionvisitInfo=fe8e143c-5d08-4286-b2dd-47a499bb7e30|www.che168.com|0; che_sessionvid=7106799D-494B-48C1-9E53-8DC36209C0CE; sessionuid=fe8e143c-5d08-4286-b2dd-47a499bb7e30'
        }
        self.i = 0

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
            # 抓取1辆汽车的信息，随机休眠1-2秒钟
            time.sleep(random.uniform(0, 5))

    def get_data(self, car_url):
        """功能：抓取1辆汽车的详情信息"""
        two_html = self.get_html(car_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">(.*?)<b>万</b><i class="usedfont used-xiajiantou"></i>.*?'
        car_lsit = self.re_func(two_regex, two_html)
        item = {}
        try:
            item['name'] = car_lsit[0][0].strip()
            item['km'] = car_lsit[0][1].strip()
            item['time'] = car_lsit[0][2].strip()
            item['type'] = car_lsit[0][3].split('/')[0].strip()
            item['city'] = car_lsit[0][4].strip()
            item['price'] = car_lsit[0][5].split(';')[1].strip()
            print(item)
        except Exception:
            pass

    def run(self):
        """程序的入口函数"""
        for i in range(1, 3):
            url = self.url.format(i)
            self.parse_html(url)


if __name__ == '__main__':
    spider = CarHomeSpider()
    spider.run()