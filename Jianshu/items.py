# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    read_count = scrapy.Field()
    like_count = scrapy.Field()
    word_count = scrapy.Field()
    subjects = scrapy.Field()
    content = scrapy.Field()

