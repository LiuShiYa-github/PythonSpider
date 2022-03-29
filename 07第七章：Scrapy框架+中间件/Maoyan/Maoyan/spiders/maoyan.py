import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.maoyan.com']
    start_urls = ['https://www.maoyan.com/films?showType=3&sortId=1&offset=0']

    def parse(self, response):
        
        pass
