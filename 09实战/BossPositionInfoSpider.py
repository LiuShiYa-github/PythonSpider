#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: BossPositionInfoSpider.py
@Time    : 2022/5/3 17:20
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 爬取BOSS中指定职位的相关信息
"""

from lxml import etree
import time
import random
from selenium import webdriver

"""
BOSS根据IP地址进行限制

一级页面：薪资、公司名称、学历要求、公司规模
二级页面：职位描述、公司介绍、公司地址、成立时间、注册资金
"""

position = input('请输入要查询的职位名称：')
for i in range(1, 20):
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://www.zhipin.com/job_detail/?query={}&page={}&city=101210100&industry=&position='.format(position, 1)
    print(url)
    driver.get(url=url)
    time.sleep(10)
    time.sleep(random.randint(1, 3))
    html = driver.page_source
    p = etree.HTML(html)
    for num in range(1, 31):
        if num % 2 == 1:
            li_list = p.xpath('//*[@id="main"]/div/div[{}]/ul/li[{}]'.format(3, num))
        else:
            li_list = p.xpath('//*[@id="main"]/div/div[{}]/ul/li[{}]'.format(2, num))
        item = {}
        for li in li_list:
            try:
                item['职位名称'] = li.xpath('.//div/div[1]/div[1]/div/div[1]/span[1]/a/text()')[0]
                item['薪资范围'] = li.xpath('.//div/div[1]/div[1]/div/div[2]/span/text()')[0]
                item['公司名称'] = li.xpath('.//div/div[1]/div[2]/div/h3/a/text()')[0]
                item['学历要求'] = li.xpath('.//div/div[1]/div[1]/div/div[2]/p/text()')[0]
                item['融资情况'] = li.xpath('.//div/div[1]/div[2]/div/p/text()[1]')[0]
                item['公司规模'] = li.xpath('.//div/div[1]/div[2]/div/p/text()[2]')[0]
                driver.get(
                    url='https://www.zhipin.com' + li.xpath('.//div/div[1]/div[1]/div/div[1]/span[1]/a/@href')[0])
                time.sleep(random.randint(3, 5))
                two_html = driver.page_source
                two_p = etree.HTML(two_html)
                item['职位描述'] = two_p.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div/text()')[0]
                item['公司介绍'] = two_p.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[2]/div/text()')[0]
                item['公司地址'] = two_p.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[6]/div/div[1]/text()')[0]
                item['注册资金'] = two_p.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[5]/div[2]/li[2]/text()')[0]
                item['链接'] = 'https://www.zhipin.com' + li.xpath('.//div/div[1]/div[1]/div/div[1]/span[1]/a/@href')[0]
                print(item)
            except Exception as e:
                pass
