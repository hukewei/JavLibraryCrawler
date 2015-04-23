# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavlibrarycrawlItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() #
    designation = scrapy.Field() # ABP-108
    url = scrapy.Field() #javliiqq6e
    category = scrapy.Field() # categories
    release_date = scrapy.Field() # 2015-04-24
    duration = scrapy.Field() # 120
    image_urls = scrapy.Field() #
    images = scrapy.Field()
    actor = scrapy.Field()
