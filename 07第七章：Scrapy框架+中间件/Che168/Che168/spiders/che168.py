import scrapy
from ..items import Che168Item
from lxml import etree


class Che168Spider(scrapy.Spider):
    name = 'che168'
    car_num = 0
    page = 2
    allowed_domains = ['www.che168.com']
    start_urls = ['https://www.che168.com/china/a0_0msdgscncgpi1ltocsp1exx0/?pvareaid=102179#currengpostion']
    # "https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion".format()

    def parse(self, response):
        """ 提取一页的数据 """
        p = etree.HTML(response.text)
        li_list = p.xpath('//*[@name="lazyloadcpc"]')
        for i in li_list:
            item = Che168Item()
            item['名称'] = i.xpath('.//a/div[2]/h4/text()')[0].strip()
            item['信息'] = i.xpath('.//a/div[2]/p/text()')[0].strip()
            item['链接'] = 'https://www.che168.com' + i.xpath('.//a/@href')[0].strip()
            # meta参数：在不同的解析函数之间传递数据
            yield scrapy.Request(url=item['链接'], meta={'item':item}, callback=self.get_car_info)

        if self.page < 100:
            self.page += 1
            url = 'https://www.che168.com/china/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179#currengpostion'.format(
                self.page)
            yield scrapy.Request(url=url, callback=self.parse)

    def get_car_info(self, response):
        """ 获取二级页面的内容 """

        """ 
        /html/body/div[5]/div[2]/ul/li[1]/h4 表显里程
        /html/body/div[5]/div[2]/ul/li[2]/h4 上牌时间
        /html/body/div[5]/div[2]/ul/li[3]/h4 排量
        /html/body/div[5]/div[2]/ul/li[4]/h4 车辆所在地
        /html/body/div[5]/div[2]/ul/li[5]/h4/text() 国标
        //*[@id="overlayPrice"]/text() 价格 
        """
        item = response.meta['item']
        item['表显里程'] = response.xpath('/html/body/div[5]/div[2]/ul/li[1]/h4/text()').get()
        item['上牌时间'] = response.xpath('/html/body/div[5]/div[2]/ul/li[2]/h4/text()').get()
        item['排量'] = response.xpath('/html/body/div[5]/div[2]/ul/li[3]/h4/text()').get()
        item['车辆所在地'] = response.xpath('/html/body/div[5]/div[2]/ul/li[4]/h4/text()').get()
        item['国标'] = str(response.xpath('/html/body/div[5]/div[2]/ul/li[5]/h4/text()').get()).replace("\r\n", "")
        item['价格'] = str(response.xpath('//*[@id="overlayPrice"]/text()').get()).strip('¥') + 'w'
        yield item
