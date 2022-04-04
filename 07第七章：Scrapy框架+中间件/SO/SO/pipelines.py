# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class SoPipeline(ImagesPipeline):
    # 重写get_media_requests()方法,将图片链接交给调度器入队列即可
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['image_url'], meta={'title': item['image_title']})
        
    # 重写file_path()方法,来处理文件路径及文件名
    def file_path(self, request, response=None, info=None, *, item=None):
        image_title = request.meta['title']
        filename = image_title + '.jpg'
        
        return filename