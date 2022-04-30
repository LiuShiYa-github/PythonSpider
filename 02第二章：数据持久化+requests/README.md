# 数据持久化存储-CSV
**CSV模块**
```text
模块
    -- csv Python标准库模块
作用
    -- 将爬取的数据存放到本地的csv文件中
使用流程
    -- 打开csv文件
    -- 初始化写入对象
    -- 写入数据(参数为列表)
示例
    import csv #导入csv模块
    with open('test.csv', 'w') as f: #正常打开文件,后缀为.csv
        writer = csv.writer(f) #初始化写入对象
        writer.writerow([]) #写入数据
```
**Demo**

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: test.py
@Time    : 2022/4/30 20:27
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     : CSV
"""
import csv

# writerow 单行写入
with open('../02第二章：数据持久化+requests/test.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['热气球', '起飞'])
# writerows 一次性写入多行
TV_li = [
	('非自然死亡', '石原里美'),
	('逃避虽然可耻但有用', '新垣结衣'),
	('深夜食堂', '未知master')
]

with open('../02第二章：数据持久化+requests/test.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(TV_li)
```
![img_28.png](../Image/img_28.png)

**猫眼经典电影-保存为CSV**

[代码-单行写入](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieCSVWriterow.py)
![img_30.png](../Image/img_30.png)


[代码-一次性写入多行](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieCSVWriterows.py)
![img_29.png](../Image/img_29.png)


# 数据持久化存储-MySQL

**猫眼经典电影-存储在MySQL**

[代码](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieMysql.py)

![img_34.png](../Image/img_34.png)

# 数据持久化存储-MongoDB

**猫眼经典电影-存储在MongoDB**

[代码](https://github.com/LiuShiYa-github/PythonSpider/blob/master/02%E7%AC%AC%E4%BA%8C%E7%AB%A0%EF%BC%9A%E6%95%B0%E6%8D%AE%E6%8C%81%E4%B9%85%E5%8C%96%2Brequests/MaoyanClassicMovieMongoDB.py)

![img_31.png](../Image/img_31.png)
![img_32.png](../Image/img_32.png)

# 多级页面抓取

# requets模块

# 增量爬虫-MySQL以及Redis实现