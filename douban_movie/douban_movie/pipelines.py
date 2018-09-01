# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
    	item['score']=int(item['score'])
    	if item['score']>=8:
    		i=json.dumps(dict(item))
    		self.redis.lpush('douban_movie:items',i)
    	return item
    def open_spider(self,spider):
    	self.redis=redis.StrictRedis(host='localhost',port=6379,db=0)
