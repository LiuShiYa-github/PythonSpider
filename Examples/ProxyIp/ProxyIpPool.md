

```text
代理IP定义：代替你原来的IP地址去对接网络的IP地址
作用：隐藏自身真是IP，避免被目标网站封掉。

代理IP分类：
高匿代理：web端只能看到代理IP
普通代理：web端知道有人通过此代理IP访问，但不知道用户真是IP
透明代理：web端能看到用户真实IP，也能看到代理IP

应用场景：
针对高频率访问的IP地址进行了反爬机制，封掉IP地址的网站

代理IP地址：自行百度代理IP
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/5de762ffd35e4d53ae117b5e4ccdb36c.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA54Ot5rCU55CD44CB,size_20,color_FFFFFF,t_70,g_se,x_16)
语法格式
```python
        proxies = {
            'http': 'http://IP:端口号',
            'https': 'http://IP:端口号'
        }
       res = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=2)
```

示例
```python
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
```

效果展示

![在这里插入图片描述](https://img-blog.csdnimg.cn/389661fd13ce4479a4617c3de1468fd0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA54Ot5rCU55CD44CB,size_20,color_FFFFFF,t_70,g_se,x_16)