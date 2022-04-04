# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class KfcPipeline:
    def process_item(self, item, spider):
        print(item)
        return item


# 管道2 - 数据持久化到MySQL数据库
import pymysql
class KfcMysqlPipeline:
    def open_spider(self, spider):
        self.db = pymysql.connect(host='10.0.0.101', user='root', password='123456', database='kfcdb', charset='utf8')
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        ins = 'insert into kfctab values(%s,%s,%s,%s,%s)'
        li = [
            item['rownum'],
            item['storeName'],
            item['addressDetail'],
            item['cityName'],
            item['provinceName'],
        ]
        self.cur.execute(ins, li)
        self.db.commit()
        
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.db.close()
    


"""
create database kfcdb charset utf8;
use kfcdb;
create table kfctab(
rownum varchar(100),
storeName varchar(100),
addressDetail varchar(100),
cityName varchar(100),
provinceName varchar(100)
)charset=utf8;
"""