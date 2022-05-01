#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: MaoyanClassicMovieMongoDB.py
@Time    : 2022/4/10 22:31
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : 猫眼电影经典影片 按照热门排序

create table maoyantab(
name varchar(100),
score varchar(50),
type varchar(50),
star varchar(50),
time varchar(50)
)charset=utf8;
"""

import pymysql

db = pymysql.connect(host='', port='', user='', database='')  # 创建数据库连接对象
cursor = db.cursor() # 创建游标对象
cursor.execute() # 执行SQL语句
db.commit() #  提交到数据库执行
cursor.close() # 关闭游标
db.close() # 断开数据库连接
