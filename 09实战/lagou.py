#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: lagou.py
@Time    : 2022/6/10 17:52
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     :
"""
import requests
from lxml import etree
import random
import time


def get_lagou():
    i = 0
    item = {}
    zw = input("请输入要查询的职位信息：")
    for page in range(1, 25):
        url = "https://www.lagou.com/wn/jobs?pn={}&px=new&fromSearch=true&kd={}".format(page, zw)
        print("第{}页".format(page))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
            'Cookie': 'user_trace_token=20220505094517-5816dd43-a5da-4c91-81b1-7ca772326221; _ga=GA1.2.1997510957.1651715118; LGUID=20220505094518-4d772e00-902f-4262-ae79-d3cdb34ecfed; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1654854608; JSESSIONID=ABAAABAABEIABCIC34BBEA2A4FE447392D861D87D981766; WEBTJ-ID=20220610175149-1814d06f23534e-00baacbd801524-9771a3f-3686400-1814d06f236f28; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; privacyPolicyPopup=false; index_location_city=%E6%9D%AD%E5%B7%9E; _gid=GA1.2.150214763.1654854713; TG-TRACK-CODE=index_search; __lg_stoken__=a49743e62d55b8d0d9f123f8316b5c9d53b69bfaceffad7b581a4c5b1bc673b23e7a1633190e786c3b4b25900c6c829b432249855677b314e956125613f759dabbbbcec9b0d5; X_MIDDLE_TOKEN=d15e4ecbd5b1a452f4bfa960524fdeaf; LGSID=20220610184614-285c7020-0c0f-45a3-bc51-64863bb8f874; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D122.233.95.102%26u%3D2; gate_login_token=5a457d9a1aa4c20edec9246753ed254187a19205bd26209cf3892ab9453d222d; _putrc=F6FE2931887E339D123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B71664; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; X_HTTP_TOKEN=ce1000ec1d086f6040085845618a0004bbaf4cbbf8; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1654858004; LGRID=20220610184644-c0fee2d2-f82e-4ad3-a958-c153da906988; __SAFETY_CLOSE_TIME__14841168=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2214841168%22%2C%22%24device_id%22%3A%22180941cfe03f7f-0536527c703f8c-9771a3f-921600-180941cfe04aff%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2299.0.4844.82%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22180941cfe03f7f-0536527c703f8c-9771a3f-921600-180941cfe04aff%22%7D'
        }
        html = requests.get(url=url, headers=headers, timeout=3).text
        p = etree.HTML(html)
        for num in range(1, 16):
            # li_list = p.xpath('//*[@id="jobList"]/div[1]/div[1]/div[{}]'.format(num))
            li_list = p.xpath('//*[@id="jobList"]/div[1]/div[{}]'.format(num))
            for li in li_list:
                i += 1
                name_list = li.xpath('.//div[1]/div[1]/a/text()')
                item['职位名称'] = name_list[0].strip() if name_list else None
                name_list = li.xpath('.//div[1]/div[2]/span/text()')
                item['薪资'] = name_list[0].strip() if name_list else None
                name_list = li.xpath('.//div[1]/div[2]/text()')
                item['工作经验'] = name_list[0].strip() if name_list else None
                name_list = li.xpath('.//div[1]/span/text()')
                item['发布时间'] = name_list[0].strip() if name_list else None
                name_list = li.xpath('.//div[2]/div[1]/a/text()')
                item['公司名称'] = name_list[0].strip() if name_list else None
                name_list = li.xpath('.//div[2]/div[2]/text()')
                item['公司简介'] = name_list[0].strip() if name_list else None
                print(item)
        time.sleep(random.randint(1, 3))
    print("职位的个数为：{}".format(i))


get_lagou()