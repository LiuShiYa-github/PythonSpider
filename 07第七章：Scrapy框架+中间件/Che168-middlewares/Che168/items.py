# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
//*[@class="cards-li list-photo-li "]/a/div[2]/h4 车名
//*[@class="cards-li list-photo-li "]/a/div[2]/p info信息
//*[@class="cards-li list-photo-li "]/a/div[2]/div[1]/span[1]/em 价格信息
//*[@class="cards-li list-photo-li "]/a/@href 连接信息
"""


class Che168Item(scrapy.Item):
    # define the fields for your item here like:
    名称 = scrapy.Field()
    信息 = scrapy.Field()
    链接 = scrapy.Field()
    表显里程 = scrapy.Field()
    上牌时间 = scrapy.Field()
    排量 = scrapy.Field()
    车辆所在地 = scrapy.Field()
    国标 = scrapy.Field()
    价格 = scrapy.Field()
