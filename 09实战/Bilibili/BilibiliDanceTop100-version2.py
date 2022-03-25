"""
BilibiliDanceTop100
https://www.bilibili.com/v/popular/rank/tv
"""
import re

import requests
from lxml import etree


class BilibiliDanceTop100:
    def __init__(self):
        self.url = 'https://www.bilibili.com/v/popular/rank/dance'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
        # 添加计数变量
        self.i = 0

    def get_html(self, url):
        """获取HTML内容"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        return html

    def parse_html_one(self, html):
        """提取HTML内容"""
        regex = '<div class="content">.*?<a href="(.*?)".*?class="title">(.*?)</a>.*?alt="up">(.*?)</span></a>.*?alt="play">(.*?)</span>.*?alt="like">(.*?)</span>'
        pattern = re.compile(regex, re.S)
        r_list_one = pattern.findall(html)
        # 调用数据处理函数
        self.save_html(r_list_one)

    def save_html(self, r_list):
        """数据处理函数"""
        item = {}
        for r_one in r_list:
            item['链接'] = 'https:{}'.format(r_one[0].strip())
            item['视频名称'] = "《{}》".format(r_one[1].strip())
            item['up'] = r_one[2].strip()
            item['播放量'] = r_one[3].strip()
            item['弹幕'] = r_one[4].strip()
            two_html = self.get_html(url='https:{}'.format(r_one[0]))
            # time.sleep(2)
            p = etree.HTML(two_html)

            NumberOfViewers = p.xpath('//*[@id="bilibiliPlayer"]/div[1]/div[2]/div/div[1]/div[1]/text()')
            if NumberOfViewers:
                item['正在观看人数'] = NumberOfViewers[0].strip()
            else:
                item['正在观看人数'] = '未获取到'

            Describe = p.xpath('//*[@id="v_desc"]/div[2]/span/text()')
            if Describe:
                item['视频描述'] = Describe[0].strip()
            else:
                item['视频描述'] = '无'
            OneKeyThreeLinks = p.xpath('//*[@id="arc_toolbar_report"]/div[1]')
            for one_key_three_links in OneKeyThreeLinks:
                try:
                    item['点赞'] = one_key_three_links.xpath('.//span[1]/text()')[0].strip()
                    item['投币'] = one_key_three_links.xpath('.//span[2]/text()')[0].strip()
                    item['收藏'] = one_key_three_links.xpath('.//span[3]/text()')[0].strip()
                    item['转发'] = one_key_three_links.xpath('.//span[4]/text()')[0].strip()
                    print(item)
                    self.i += 1
                except IndexError as e:
                    print('出现了异常数据，正在选择过滤,错误信息为：', e)


    def run(self):
        """程序运行调配"""
        html_one = self.get_html(url=self.url)
        self.parse_html_one(html=html_one)


if __name__ == '__main__':
    spider = BilibiliDanceTop100()
    spider.run()
    print('作品数量：', spider.i)
