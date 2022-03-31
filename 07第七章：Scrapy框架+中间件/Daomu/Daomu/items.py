# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义数据结构依据： 管道文件数据处理时你需要哪些数据
    parent_title = scrapy.Field()
    son_title = scrapy.Field()
    novel_content = scrapy.Field()
