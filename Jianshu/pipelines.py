# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class JianshuPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='******(your password)', database='*****(your database)',charset='utf8(advised)')
        cursor = conn.cursor()
        sql = "insert into tb_js (title,author,content) values(%s,%s,%s)"
        cursor.execute(sql,(item['title'],item['author'],item['content'][:500]))
        conn.commit()
        return item

