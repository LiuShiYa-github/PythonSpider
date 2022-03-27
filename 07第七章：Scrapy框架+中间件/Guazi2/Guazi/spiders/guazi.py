import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    page = 1
    car_num = 0
    allowed_domains = ['mapi.guazi.com']
    # start_urls = [
    #     'https://mapi.guazi.com/car-source/carList/pcList?minor=&sourceType=&ec_buy_car_list_ab=&location_city'
    #     '=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission'
    #     '=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,'
    #     '-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year'
    #     '=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page=1&pageSize=20&city_filter=12&city=12&guazi_city'
    #     '=12&qpres=520467436215214080&versionId=0.0.0.0&osv=Unknown&platfromSource=wap']
    
    def start_requests(self):
        """ 一次性生成所有的URL地址,一次性交给调度器入队列 """
        for page in range(1, 5):
            url = 'https://mapi.guazi.com/car-source/carList/pcList?minor=&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page={}&pageSize=20&city_filter=12&city=12&guazi_city=12&qpres=520467436215214080&versionId=0.0.0.0&osv=Unknown&platfromSource=wap'.format(page)
            yield scrapy.Request(url=url, callback=self.datail_page)
            
    def datail_page(self, response):
        for i in range(0, 20):
            try:
                # 给items.py中的GuaziItem类做实例化
                item = GuaziItem()
                item['name'] = response.json()['data']['postList'][i]['title']
                # item['price'] = response.json()['data']['postList'][i]['price']
                item['link'] = 'https://www.guazi.com/Detail?clueId={}'.format(response.json()['data']['postList'][i]['clue_id'])
                # print(item)
                # 把抓取的数据提交给管道文件处理:yield item
                self.car_num += 1
                yield item
            except Exception as e:
                print('抓取完成,程序结束.共有汽车:{}'.format(self.car_num))
                break
        
            # 生成下一页的地址,去交给调度器入队列
        if self.page < 80:
            self.page += 1
            url = 'https://mapi.guazi.com/car-source/carList/pcList?minor=&sourceType=&ec_buy_car_list_ab=&location_city' \
                  '=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement' \
                  '=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,' \
                  '-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num' \
                  '=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page={}&pageSize=20&city_filter=12&city=12&guazi_city=12&qpres=520467436215214080&versionId=0.0.0.0&osv' \
                  '=Unknown&platfromSource=wap'.format(self.page)
            yield scrapy.Request(url=url, callback=self.datail_page)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
