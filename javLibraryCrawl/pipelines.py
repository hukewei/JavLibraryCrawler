# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
import sys
import jpush as jpush

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from scrapy.conf import settings
from scrapy import log
from conf import app_key, master_secret

            
class JavlibrarycrawlPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

class MongoDBPipeline(object):
    def __init__(self):
       reload(sys)
       sys.setdefaultencoding("utf-8")
       self._jpush = jpush.JPush(app_key, master_secret) 
        
    def process_item(self, item, spider):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        if spider.name == 'actor_spider':
            self.collection = db[settings['MONGODB_COLLECTION']]
        elif spider.name == 'best_rated_spider':
            self.collection = db[settings['MONGODB_COLLECTION_BEST_RATED']]
        elif spider.name == 'most_wanted_spider':
            self.collection = db[settings['MONGODB_COLLECTION_MOST_WANTED']]
        elif spider.name == 'new_releases_spider':
            self.collection = db[settings['MONGODB_COLLECTION_NEW_RELEASES']]
        elif spider.name == 'new_entries_spider':
            self.collection = db[settings['MONGODB_COLLECTION_NEW_ENTRIES']]
        else:
            self.collection = db[settings['MONGODB_COLLECTION']]
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        title = item['title']
        actors = item['actor']
        if self.is_already_in_db(title):
            valid = False
        if valid:
            _id = self.collection.insert(dict(item))
            self.send_notification(_id, title, actors)
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item

    def send_notification(self, _id, title, actors):
	for actor in actors:
            client_ids = self.get_actor_subscribers(actor)
            if client_ids:
                push = self._jpush.create_push()
                push.audience = jpush.audience(
                    jpush.registration_id(*client_ids)
                )
	        log.msg("client ids = " + json.dumps(client_ids))
	        message = jpush.android(alert=u'新片通知 : 您关注的艺人 ' + actor.encode('utf-8') + u' 有新片 %s ，点击查看详情。' %(title.encode('utf-8')), extras={'VideoID':str(_id)})
                push.notification = jpush.notification(alert=u'新片通知 : 您关注的艺人发布了新片，点击查看详情。', android=message)
	        log.msg("Sending push notification for %s and %s" %(title, actor))
                push.platform = jpush.all_
                push.send()

    def is_already_in_db(self, title):
        'check if the title is already in the current db or not'
        return self.collection.find( { 'title': { '$exists': True, '$in': [title] } } ).count() > 0

    def get_actor_subscribers(self, actor):
        'iterate the membersPreference collection, find client_id where favorite_actors contains actor'
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db['membersPreference']
        result = []
        cursor = self.collection.find({'notified_actors' : actor}, { 'clientID': 1, '_id':0 })
        for record in cursor:
            result.append(record.get('clientID'))
	result.append('02068f6a423')
	return result

