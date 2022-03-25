"""
链家二手房源信息的抓取
目标数据： 房源名称、地址、户型、面积、方位、是否精装、楼层、年代、类型、总价、单价
"""
import random
import time

import requests
from fake_useragent import UserAgent
from lxml import etree


class LianHomeSpider:
    def __init__(self):
        self.url = 'https://sh.lianjia.com/ershoufang/pg{}/'
    
    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        for i in range(3):
            try:
                html = requests.get(url=url, headers=headers, timeout=3).text
                self.parse_html(html)
            except Exception as e:
                print('页面响应超时，重试中。。。。。。')

    def parse_html(self, html):
        p = etree.HTML(html)
        # 1、基准xpath
        li_list = p.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        item = {}
        for li in li_list:
            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item['name'] = name_list[0].strip() if name_list else None
            address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = address_list[0].strip() if address_list else None
            info_li = li.xpath('.//div[@class="houseInfo"]/text()')
            if info_li:
                info_li = info_li[0].split('|')
                if len(info_li) == 7:
                    item['model'] = info_li[0].strip()
                    item['area'] = info_li[1].strip()
                    item['direct'] = info_li[2].strip()
                    item['perfect'] = info_li[3].strip()
                    item['floor'] = info_li[4].strip()
                    item['year'] = info_li[5].strip()
                    item['type'] = info_li[6].strip()
                else:
                    item['model'] = item['area'] = item['direct'] = item['perfect'] = item['floor'] = item['year'] = item[
                        'type'] = None
            else:
                item['model'] = item['area'] = item['direct'] = item['perfect'] = item['floor'] = item['year'] = item[
                    'type'] = None

            total_list = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')
            item['total'] = total_list[0].strip() + '万' if total_list else None
            unit_list = li.xpath('.//div[@class="unitPrice"]/span/text()')
            item['unit'] = unit_list[0].strip() if unit_list else None

            print(item)

    def run(self):
        for pg in range(1, 101):
            url = self.url.format(pg)
            self.get_html(url)
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = LianHomeSpider()
    spider.run()
