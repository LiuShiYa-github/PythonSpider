# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class DaomuPipeline:
    def process_item(self, item, spider):
        """ 将item（也就是抓取到的小说信息）存储到文件中 """
        filename = './novel/{}/{}.txt'.format(
            item['parent_title'].replace(' ', '_'),
            item['son_title'].replace(' ', '_')
        )
        with open(filename, 'w') as f:
            f.write(item['novel_content'])
        return item
