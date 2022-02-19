"""
BilibiliDanceTop100
"""
from urllib import request
import re


class BilibiliDanceTop100:
    def __init__(self):
        self.url = 'https://www.bilibili.com/v/popular/rank/dance'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}
        # 添加计数变量
        self.i = 0

    def get_html(self):
        "获取HTML内容"
        req = request.Request(url=self.url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # print(html)
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        "提取HTML内容"
        regex = '<div class="content">.*?class="title">(.*?)</a>.*?alt="up">(.*?)</span></a>.*?alt="play">(.*?)</span>.*?alt="like">(.*?)</span>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # 调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        "数据处理函数"
        item = {}
        for r in r_list:
            item['视频名称'] = "《{}》".format(r[0].strip())
            item['up'] = r[1].strip()
            item['播放量'] = r[2].strip()
            item['弹幕'] = r[3].strip()
            print(item)
            self.i += 1

    def run(self):
        "程序运行调配"
        self.get_html()


if __name__ == '__main__':
    spider = BilibiliDanceTop100()
    spider.run()
    print('作品数量：', spider.i)
