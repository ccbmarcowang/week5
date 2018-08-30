# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem
import re

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']
    rules=(Rule(LinkExtractor(allow=r'http://.*'),callback='parse_page',follow=True),)

    def parse_page(self, response):
        item=PageItem()
        item['url']=response.url
        #item['text1']=response.xpath('//*/text()').re('(\S+)')
        item['text'] = response.xpath('//text()').extract()
        return item
        
