#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@FileName: test.py
@Time    : 2022/3/26 0:00
@Author  : 热气球
@Software: PyCharm
@Version : 1.0
@Contact : 2573514647@qq.com
@Des     :
"""

import requests

for page in range(1, 79):
	print('page:{}'.format(page))
	url = 'https://mapi.guazi.com/car-source/carList/pcList?minor=&sourceType=&ec_buy_car_list_ab=&location_city=&district_id=&tag=-1&license_date=&auto_type=&driving_type=&gearbox=&road_haul=&air_displacement=&emission=&car_color=&guobie=&bright_spot_config=&seat=&fuel_type=&order=&priceRange=0,-1&tag_types=&diff_city=&intention_options=&initialPriceRange=&monthlyPriceRange=&transfer_num=&car_year=&carid_qigangshu=&carid_jinqixingshi=&cheliangjibie=&page={}&pageSize=20&city_filter=12&city=12&guazi_city=12&qpres=520467436215214080&versionId=0.0.0.0&osv=Unknown&platfromSource=wap'.format(
		page)
	cookie = 'uuid=beeaf3eb-8e9a-44c2-eaa5-54a41a0fa703; sessionid=98b23e69-7b5b-4c44-a6d3-fc05034bca49; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; cainfo=%7B%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%22beeaf3eb-8e9a-44c2-eaa5-54a41a0fa703%22%7D',
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
		'Cookie': 'uuid=beeaf3eb-8e9a-44c2-eaa5-54a41a0fa703; sessionid=98b23e69-7b5b-4c44-a6d3-fc05034bca49; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; cainfo=%7B%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22guid%22%3A%22beeaf3eb-8e9a-44c2-eaa5-54a41a0fa703%22%7D'
		
	}
	html = requests.get(url=url, headers=headers).json()
	for i in range(0, 20):
		try:
			# 给items.py中的GuaziItem类做实例化
			item = {}
			item['name'] = html['data']['postList'][i]['title']
			# item['price'] = response.json()['data']['postList'][i]['price']
			item['link'] = 'https://www.guazi.com/Detail?clueId={}'.format(html['data']['postList'][i]['clue_id'])
			print(item)
		except Exception as e:
			print(e)
