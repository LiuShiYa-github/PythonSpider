# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KfcItem(scrapy.Item):
    # define the fields for your item here like:
    rownum = scrapy.Field()
    storeName = scrapy.Field()
    addressDetail = scrapy.Field()
    cityName = scrapy.Field()
    provinceName = scrapy.Field()
    

