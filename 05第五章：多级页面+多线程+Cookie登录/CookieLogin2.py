#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: CookieLogin2.py
@Time    : 2022/3/22 10:54
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 17695691664@163.com
@Des     : Cookie模拟登陆二
"""
import requests


def login():
    url = 'https://weread.qq.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', }
    cookies = get_cookies()
    html = requests.get(url=url, headers=headers, cookies=cookies).text
    # 确认HTML中是否存在收藏的书籍信息:bash shell脚本编程经典实例
    print(html)


def get_cookies():
    """ 功能：处理字符串形式的Cookie为字典形式 """
    cookies = {}
    cookie_string = '_qpsvr_localtk=0.4192265630313492; RK=GF1gnmVh3H; ptcz=493c08710b1aba6b42e625c7f2ba2bfd2c4d4a9fa7ce4009d64914146ae61b25; wr_gid=251557801; wr_vid=42146813; wr_skey=oMEpfEIC; wr_pf=0; wr_rt=web%40XqNo4vmmDY63nJ78lXS_WL; wr_localvid=594324c072831bfd594d158; wr_name=%E7%83%AD%E6%B0%94%E7%90%83%F0%9F%8E%88; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FxPjAuSXMic26mSVL9bunqtwxNO6cXMibWbRdHts7Sib1ibW8tFCR3BuwicQmztozLxXia9GNoURicEAP1Ol6BqxeaM1UA%2F132; wr_gender=1'
    for kv in cookie_string.split('; '):
        key = kv.split('=')[0]
        value = kv.split('=')[1]
        cookies[key] = value
    # 此循环结束后，cookies为最终的字典
    return cookies


login()
