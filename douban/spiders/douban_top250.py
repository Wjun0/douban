# -*- coding: utf-8 -*-
import scrapy


class DoubanTop250Spider(scrapy.Spider):
    name = 'douban_top250'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        with open("test.html","w",encoding='utf8') as f:
            f.write(response.text)
        print("拿到的源码是：",response.text)

