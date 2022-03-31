import scrapy
from ..items import DaomuItem
import os


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['https://www.daomubiji.com/']

    def parse(self, response):
        """ 一级页面解析函数、提取： 大标题、大链接 """
        a_list = response.xpath('//li[contains(@id, "menu-item-")]/a')
        for a in a_list:
            item = DaomuItem()
            item['parent_title'] = a.xpath('./text()').get()
            parent_href = a.xpath('./@href').get()
            # 创建对应的目录结构
            directory = './novel/{}/'.format(item['parent_title'])
            if not os.path.exists(directory):
                os.makedirs(directory)

            # 将parent_href继续交给调度器入队列
            yield scrapy.Request(url=parent_href, meta={'item': item}, callback=self.parse_second_page)

    def parse_second_page(self, response):
        """ 二级页面解析函数，提取小标题和小链接 """
        meta1 = response.meta['item']
        a_list = response.xpath('//article/a')
        num = 0
        for a in a_list:
            # 创建全新的item对象，避免再给对象赋值时一直被覆盖
            item = DaomuItem()
            item['son_title'] = str(num) + a.xpath('./text()').get()
            item['parent_title'] = meta1['parent_title']
            son_href = a.xpath('./@href').get()
            num += 1
            # 将son_href继续交给调度器入队列
            yield scrapy.Request(url=son_href, meta={'item': item}, callback=self.parse_third_page)

    def parse_third_page(self, response):
        """ 三级页面解析函数，提取具体的小说内容 """
        item = response.meta['item']
        # xpath提取出来的是列表，extract是去掉<Selector xpath='xxx'此类的信息)
        p_list = response.xpath('//article/p/text()').extract()
        item['novel_content'] = '\n'.join(p_list)
        # 至此一本小说的内容已经全部提取出来了，交给管道文件处理
        print(item)
        yield item
