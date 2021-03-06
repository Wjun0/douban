# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class DoubanTop250Spider(scrapy.Spider):
    name = 'douban_top250'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        #可以先将源码拿到,查看需要的数据是否拿到

        # with open("test.html","w",encoding='utf8') as f:
        #     f.write(response.text)


        #拿去该页的数据和下一页的url
        # 将该页数据组装到meta中传递给详情页,在详情页拼接所有数据保存

        data_list = response.xpath('//*[@id="content"]/div/div/ol/li/div')

        for item in data_list:
            dic = {}
            detail_url = item.xpath('./div/a/@href').extract_first()
            image_url = item.xpath('./div/a/img/@src').extract_first()
            name = item.xpath('./div[2]/div[1]/a/span[1]/text()').extract_first()
            score  = item.xpath('./div[2]/div[2]/div/span[2]/text()').extract_first()
            ranking = item.xpath('./div[1]/em/text()').extract_first()

            dic['name'] = name
            dic['image_url'] = image_url
            dic['score'] = score
            dic['url'] = detail_url
            dic['ranking'] = ranking
            yield scrapy.Request(detail_url,callback=self.detail_parse,meta=dic)


        url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        next_url = response.urljoin(url)
        yield scrapy.Request(next_url,callback=self.parse)


    def detail_parse(self,response):
        # with open('detail.html',"w",encoding='utf8')as f:
        #     f.write(response.text)
        detail = response.xpath('//*[@id="link-report"]/span/text()').extract_first().strip()

        data_dic = response.meta

        item = DoubanItem()
        item['name'] = data_dic.get('name')
        item['url'] = data_dic.get('url')
        item['image_url'] = data_dic.get('image_url')
        item['score'] = data_dic.get('score')
        item['desc'] = detail
        item['ranking'] = data_dic.get('ranking')


        #可以在这里调用pipeline进行保存
        yield item