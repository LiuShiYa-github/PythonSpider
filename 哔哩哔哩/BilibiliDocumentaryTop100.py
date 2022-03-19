"""
BilibiliDocumentaryTop100
https://www.bilibili.com/v/popular/rank/documentary
"""
from urllib import request
import re


class BilibiliDocumentaryTop100:
    def __init__(self):
        self.url = 'https://www.bilibili.com/v/popular/rank/documentary'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
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
        regex = '<div class="info"><a.*?class="title">(.*?)</a>.*?class="data-box">(.*?)</span>.*?alt="play">(.*?)</span>.*?alt="follow">(.*?)</span></div></div></div>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # 调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        "数据处理函数"
        item = {}
        for r in r_list:
            item['名称'] = "《{}》".format(r[0].strip())
            item['集数'] = r[1].strip()
            item['播放量'] = r[2].strip()
            item['点赞量'] = r[3].strip()
            print(item)
            self.i += 1

    def run(self):
        "程序运行调配"
        self.get_html()


if __name__ == '__main__':
    spider = BilibiliDocumentaryTop100()
    spider.run()
    print('电视剧数量：', spider.i)
