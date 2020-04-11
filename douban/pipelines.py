# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class DoubanPipeline(object):
    def open_spider(self,spider):
        self.client = MongoClient("192.168.59.129",27017)
        self.db = self.client['scrapy_douban_top250']
        self.col = self.db['db_top250']


    def process_item(self, item, spider):
        data = dict(item)
        self.col.insert(data)
        return item

    def close_spider(self,spider):
        self.client.close()