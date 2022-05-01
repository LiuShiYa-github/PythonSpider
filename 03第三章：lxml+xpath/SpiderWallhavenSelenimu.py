#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: SpiderWallhaven.py
@Time    : 2022/4/16 11:25
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 爬取wallhaven.cc
"""


"""
需求:抓取按照热度排名的图片，并存储到img中。图片的命名为图片的名字
URL： https://wallhaven.cc/search?categories=101&purity=100&topRange=1y&sorting=toplist&order=desc&page=1
URL2: https://wallhaven.cc/search?categories=101&purity=100&sorting=favorites&order=desc&page=4
get请求
每个page 有25个 0~24
//*[@id="thumbs"]/section/ul/li[24]/figure/a/@href
二级页面
/html/body/main/section/div[1]/img/@src
"""

from selenium import webdriver
import time
import requests
from lxml import etree

driver = webdriver.Chrome()
for i in range(1, 10):
    url = 'https://wallhaven.cc/search?categories=101&purity=100&sorting=favorites&order=desc&page={}'.format(i)
    driver.get(url=url)
    time.sleep(1)
    driver.maximize_window()
    # 获取第一页所有的图片地址并存储到列表中
    html = driver.page_source
    p = etree.HTML(html)
    two_url_list = []
    for li in range(1, 25):
        two_url = p.xpath('//*[@id="thumbs"]/section/ul/li[{}]/figure/a/@href'.format(li))
        two_url_list.append(two_url[0])
# 从列表中循环每个元素 发起请求 得到PNG链接
    image_url_list = []
    for two in two_url_list:
        # print(two)
        driver.get(url=two)
        time.sleep(1)
        two_html = driver.page_source
        p = etree.HTML(two_html)
        image_url = p.xpath('/html/body/main/section/div[1]/img/@src')
        image_url_list.append(image_url[0])
        driver.get(url=image_url[0])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
        }
        img_data = requests.get(url=image_url[0], headers=headers).content
        img_path = image_url[0]
        img_name = img_path.split('/')
        with open('./img/{}'.format(img_name[-1]), 'wb') as fp:
            fp.write(img_data)
            print(image_url[0], '下载成功！！！')
