import scrapy
from urllib import parse
import json
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    key = input("请输入职位类别: ")
    keyword = parse.quote(key)
    first_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1647777009701&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex=1&pageSize=10&language=zh-cn&area=cn'.format(keyword)
    start_urls = [first_url]

    def parse(self, response):
        """ 把所有要抓取的一级页面的URL地址一次性交给调度器入队列 """
        # 计算总页数,response.text获取响应内容,是字符串格式
        html = json.loads(response.text)
        count = html['Data']['Count']
        total = count // 10 if count % 10 == 0 else count // 10 + 1
        # 把所有页交给调度器入队列
        for index in range(1, total + 1):
            page_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1647777009701&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(self.keyword, index)
            # 交给调度器入队列
            # dont_filter=True: 让一级页面的URL地址不参与去重
            yield scrapy.Request(url=page_url, callback=self.detail_page, dont_filter=True)
        
    def detail_page(self, response):
        """ 一级页面解析函数,提取postid """
        one_html = json.loads(response.text)
        for one_job_dict in one_html['Data']['Posts']:
            post_id = one_job_dict['PostId']
            # 拼接二级页面URL地址,再次交给调度器入队列
            two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1647777072080&postId={}&language=zh-cn'.format(post_id)
            yield scrapy.Request(url=two_url, callback=self.get_job_info)
    
    def get_job_info(self, response):
        """ 提取每个职位的具体信息 """
        two_html = json.loads(response.text)
        item = TencentItem()
        item['job_name'] = two_html['Data']['RecruitPostName']
        item['job_address'] = two_html['Data']['LocationName']
        item['job_type'] = two_html['Data']['CategoryName']
        item['job_time'] = two_html['Data']['LastUpdateTime']
        item['job_responsibility'] = two_html['Data']['Responsibility']
        item['job_requirement'] = two_html['Data']['Requirement']
        # 至此一个职位完整信息抓取万册灰姑娘,交给管道文件处理
        yield item