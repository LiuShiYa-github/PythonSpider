#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: dump_json.py
@Time    : 2022/3/20 16:19
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 
"""
import json

app_list = [
{'名称': '他趣', '类型': '社交通讯', '代言词': '交友需谨慎，请注意保护个人隐私。抵制粗俗语言，共创文明网络环境。', '下载次数': '7,209 万次安装', '下载链接': 'https://appstore.huawei.com/app/C100297699'},
{'名称': '最右', '类型': '社交通讯', '代言词': '最右，一个看搞笑短视频、搞笑帖子的社区', '下载次数': '4 亿次安装', '下载链接': 'https://appstore.huawei.com/app/C10212948'},
{'名称': '本地陌交友', '类型': '社交通讯', '代言词': '交友需谨慎，请注意保护个人隐私。抵制粗俗语言，共创文明网络环境。', '下载次数': '766 万次安装', '下载链接': 'https://appstore.huawei.com/app/C100880143'},
{'名称': '网易大神', '类型': '社交通讯', '代言词': '马上进入游戏热爱者的世界', '下载次数': '1 亿次安装', '下载链接': 'https://appstore.huawei.com/app/C100246713'}
]

with open('app_list.json', 'w', encoding='utf-8') as f:
	json.dump(app_list, f, ensure_ascii=False)