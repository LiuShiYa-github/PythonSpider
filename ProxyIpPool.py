#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: ProxyIpPool.py
@Time    : 2022/3/14 8:53
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 17695691664@163.com
@Des     : 抓取飞度代理的免费高匿代理并测试可用性
"""

import requests
import re
from fake_useragent import UserAgent


class ProxyPool:
    def __init__(self):
        self.proxy_url = 'http://www.feidudaili.com/index/gratis/index?page={}'
        self.test_url = 'https://www.baidu.com/'
        self.headers = {'User-Agent': UserAgent().random}
        self.ip_list = []

    def get_proxy_pool(self, url):
        try:
            html = requests.get(url=url, headers=self.headers, timeout=3).text
            self.parse_html(html=html)
        except Exception as e:
            print('页面响应超时，重试中。。。。。。')

    def parse_html(self, html):
        regex = '<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>.*?</td>.*?</td>.*?</tr>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        try:
            for li in r_list:
                host = li[0]
                port = li[1]
                ipaddress = host + ':' + port
                self.test_proxy(proxy=ipaddress)
        except IndexError as e:
            print(e)

    def test_proxy(self, proxy):
        """ 测试一个代理IP地址是否可用 """
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'http://{}'.format(proxy)
        }
        try:
            res = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=2)
            if res.status_code == 200:
                print(proxy, '\033[32m可用\033[0m')
                html = requests.get(url='http://httpbin.org/get', headers=self.headers, proxies=proxies, timeout=3).text
                print('html:', html)
                self.ip_list.append(proxy)
        except Exception as e:
            print(proxy, '\033[31m不可用\033[0m')

    def run(self):
        for pg in range(1, 4504):
            url = self.proxy_url.format(pg)
            self.get_proxy_pool(url=url)


if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()
    print('可用的代理列表为：', spider.ip_list)
