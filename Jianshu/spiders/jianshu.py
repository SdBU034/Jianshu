# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Jianshu.items import JianshuItem


class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/[0-9a-z]{12}'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        item = JianshuItem()
        item['title'] = response.xpath('//h1/text()').get()
        item['author'] = response.xpath('//span[@class="_22gUMi"]/text()').get()
        item['content'] = ''
        contents = response.xpath('//p/text()').getall()
        for content in contents:
            item['content'] += content.strip()
        print("*"*50+"\n",len(item['content']),"*"*50+"\n")
        yield item
