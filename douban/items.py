# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()       #电影名称
    url = scrapy.Field()        #电影url
    score = scrapy.Field()      #电影评分
    image_url = scrapy.Field()  #电影图片连接image
    desc = scrapy.Field()       #描述/简介
    ranking = scrapy.Field()    #排名


