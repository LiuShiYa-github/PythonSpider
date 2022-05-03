#!/usr/bin/env python3.8.8
# -*- encoding: utf-8 -*-
"""
@File    :   spider-test.py
@Time    :   2022/02/07 16:49:51
@Author  :   热气球
@Version :   1.0
@Contact :   2573514647@qq.com
"""

"""
猫眼电影TOP100抓取
"""

import random
import re
import time
from urllib import request


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36',
            'Cookie': '__mta=214675752.1627866406865.1627875459110.1627875460018.12; uuid_n_v=v1; uuid=E85FEA50F32D11EB8C9F5D6CCA53AC9DD7DBAF07A29F40DB93EF3FC782A0F81F; _csrf=38f9740349f3f3b55a88970a5164681765e4611ccbd2fc8ef5f526914970614d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1627866407; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=17b04661fb4c8-0813968a22224b-d7e1938-e1000-17b04661fb4c8; _lxsdk=E85FEA50F32D11EB8C9F5D6CCA53AC9DD7DBAF07A29F40DB93EF3FC782A0F81F; __mta=214675752.1627866406865.1627866406865.1627866409991.2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1627875460; _lxsdk_s=17b04f00a6e-9d7-717-d8%7C%7C9'
        }
        # 添加计数变量
        self.i = 0

    def get_html(self,url):
        "获取HTML内容"
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # print(html)
        #直接调用解析函数
        self.parse_html(html)

    def parse_html(self,html):
        "提取HTML内容"
        regex = '<div class="movie-item-info">.*?title="(.*?)".*?">.*?</a></p>.*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(regex,re.S)
        r_list = pattern.findall(html)
        #调用数据处理函数
        self.save_html(r_list)

    def save_html(self,r_list):
        "数据处理函数"
        item = {}
        for r in r_list:
            item['name'] = r[0].strip()
            item['star'] = r[1].strip()
            item['time'] = r[2].strip()
            print(item)
            self.i += 1



    def run(self):
        "程序运行调配"
        for page in range(0,91,10):
            url = self.url.format(page)
            # print(url)
            self.get_html(url)
            #控制数据抓取频率
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
    print('电影数量：',spider.i)
