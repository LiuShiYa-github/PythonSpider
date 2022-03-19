"""
抓取指定贴吧的所有贴子中的图片
"""

import random
import time
from urllib import parse

import requests
from lxml import etree


class TiebaImageSpider:
    
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
        # 此处适用IE的User-Agent
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    
    def get_html(self, url):
        """功能函数1 - 请求"""
        html = requests.get(url=url, headers=self.headers).text

        return html

    def xpah_func(self, html, xpath_bds):
        """功能函数2 - 解析"""
        p = etree.HTML(html)
        r_list = p.xpath(xpath_bds)

        return r_list

    def parse_html(self, one_url):
        """一级页面：提取帖子连接，依次向每个帖子连接发送请求，最终下载图片"""
        one_html = self.get_html(url=one_url)
        # print(one_html)
        one_xpath = '//li[@class=" j_thread_list clearfix thread_item_box"]/div[@class="t_con cleafix"]/div[@class="col2_right j_threadlist_li_right "]/div/div/a/@href'
        href_list = self.xpah_func(html=one_html, xpath_bds=one_xpath)
        print(href_list)
        for href in href_list:
            # 拿到1个帖子的链接，把这个帖子中所有的图片保存到本地
            self.get_image(href)

    def get_image(self, href):
        """功能：把1个帖子中所有的图片保存到本地"""
        two_url = 'https://tieba.baidu.com' + href
        two_html = self.get_html(url=two_url)
        two_xpath = '//*[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        img_list = self.xpah_func(html=two_html, xpath_bds=two_xpath)
        print(img_list)
        for img in img_list:
            html = requests.get(url=img, headers=self.headers).content
            filename = two_url[-10:] + '.jpg'
            with open(filename, 'wb') as f:
                f.write(html)
            print(filename, '下载成功')
            time.sleep(random.randint(0, 1))

    def run(self):
        name = '赵丽颖'
        start = 1
        end = 3
        name = parse.quote(name)
        for i in range(start, end + 1):
            pn = (i - 1) * 50
            one_url = self.url.format(name, pn)
            print(one_url)
            self.parse_html(one_url=one_url)


if __name__ == '__main__':
    spider = TiebaImageSpider()
    spider.run()
