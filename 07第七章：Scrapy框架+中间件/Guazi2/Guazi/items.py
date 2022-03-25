# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
# 相当于你定义了一个字典，只给了key，没有给value
# 什么时候去赋值： 当爬虫程序获取到具体数值后进行赋值

