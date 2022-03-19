"""
链家二手房源信息的抓取
目标数据： 房源名称、地址、户型、面积、方位、是否精装、楼层、年代、类型、总价、单价
"""
import requests
from lxml import etree
import random
import time
from fake_useragent import UserAgent


class LianHomeSpider:
    def __init__(self):
        self.url = 'https://hz.lianjia.com/ershoufang/pg{}/'
        self.i = 0

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers, timeout=3).text
        self.parse_html(html)

    def parse_html(self, html):
        p = etree.HTML(html)
        # 1、基准xpath
        for num in range(1, 31):
            li_list = p.xpath('//*[@id="content"]/div[1]/ul/li[{}]/div[1]'.format(num))
            item = {}
            for li in li_list:
                name_list = li.xpath('.//div[2]/div/a[1]/text()')
                item['小区名'] = name_list[0].strip() if name_list else None
                address_list = li.xpath('.//div[2]/div/a[2]/text()')
                item['地址'] = address_list[0].strip() if address_list else None
                info_li = li.xpath('.//div[3]/div/text()')
                if info_li:
                    info_li = info_li[0].split('|')
                    if len(info_li) == 6:
                        item['户型'] = info_li[0].strip()
                        item['面积'] = info_li[1].strip()
                        item['朝向'] = info_li[2].strip()
                        item['装修'] = info_li[3].strip()
                        item['楼层'] = info_li[4].strip()
                        item['结构'] = info_li[5].strip()
                    else:
                        item['户型'] = item['面积'] = item['朝向'] = item['装修'] = item['楼层'] = item['结构'] = None
                else:
                    item['户型'] = item['面积'] = item['朝向'] = item['装修'] = item['楼层'] = item['结构'] = None

                total_list = li.xpath('.//div[6]/div[1]/span/text()')
                item['总价'] = total_list[0].strip() + '万' if total_list else None
                unit_list = li.xpath('.//div[6]/div[2]/span/text()')
                item['单价'] = unit_list[0].strip() if unit_list else None

                print(item)
            self.i += 1

    def run(self):
        for pg in range(1, 101):
            url = self.url.format(pg)
            self.get_html(url)
            time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    spider = LianHomeSpider()
    spider.run()
    print('房源数量：', spider.i)
