#!/usr/bin/env python3.8.8
# -*- encoding: utf-8 -*-
"""
@File    :   BaiduTiebaSpider.py
@Time    :   2022/02/07 16:49:51
@Author  :   热气球
@Version :   1.0
@Contact :   2573514647@qq.com
"""

"""
抓取指定贴吧的指定页的数据，保存到本地
"""

import random
import time
from urllib import request, parse


class BaiduTiebaSpider:
    def __init__(self):
        """定义常用的变量"""
        self.url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
        }
    
    def get_html(self, url):
        """获取相应内容的函数"""
        req = request.Request(url=url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')

        return html

    def parse_html(self):
        """解析提取数据的函数"""
        pass

    def save_html(self,filename,html):
        """数据处理函数"""
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)

    def run(self):
        """程序入口函数"""
        name = input("请输入贴吧名称：")
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        params = parse.quote(name)
        for page in  range(start,end+1):
            pn = (page-1)*50
            url = self.url.format(params,pn)
            # 发请求、解析、保存
            html = self.get_html(url)
            filename = '{}_第{}页.html'.format(name,page)
            self.save_html(filename,html)
            # 终端提示打印
            print('第%d页抓取成功' % page)
            #控制抓取的频率
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    spider = BaiduTiebaSpider()
    spider.run()
