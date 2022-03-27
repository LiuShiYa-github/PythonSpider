# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
create database guazidb charset utf8;
use guazidb;
create table guazitab(
name varchar(200),
link varchar(300)
)charset=utf8;
"""

import pymysql
import pymongo
from .settings import *


class GuaziPipeline:
    def process_item(self, item, spider):
        # print(item['name'], item['price'], item['link'])
        print(item['name'], item['link'])
        return item
    
    
class GuaziMysqlPipeline(object):
    def open_spider(self, spider):
        """ 爬虫程序开始时,执行一次,一般用于数据库的连接 """
        self.db = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PWD, database=MYSQL_DB, charset=CHARSET)
        self.cur = self.db.cursor()
        print("我是open函数")

    def process_item(self, item, spider):
        """ 进行写入MySQL """
        ins = 'insert into guazitab values(%s,%s)'
        li = [
            item['name'].strip(),
            item['link'].strip()
        ]
        self.cur.execute(ins, li)
        # 千万不要忘记提交到数据库执行
        self.db.commit()
        return item
    
    def close_spider(self, spider):
        """ 爬虫程序结束时,只执行一次,一般用于数据库的断开 """
        self.cur.close()
        self.db.close()
        print("我是close函数")


class GuaziMongoPipeline:
    def open_spider(self, spider):
        """ 连接mongodb """
        self.conn = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]
    
    def process_item(self, item, spider):
        d =dict(item)
        self.myset.insert_one(d)
        return item