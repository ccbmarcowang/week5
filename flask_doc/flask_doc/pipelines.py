# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        haha = ''.join(item['text'])
        item['text'] = re.sub('\s+', ' ', haha)
        '''
        text=''
        for i in item['text1']:
            text+=i
            text+=' '
        text=re.sub(r'html.*?','',text)
        '''
        i=json.dumps(dict(item))
        self.redis.lpush('flask_doc:items',i)
        return item
    def open_spider(self,spider):
        self.redis=redis.StrictRedis(host='localhost',port=6379,db=0)
