# -*- coding: utf-8 -*-

# Scrapy settings for javLibraryCrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'javLibraryCrawl'

SPIDER_MODULES = ['javLibraryCrawl.spiders']
NEWSPIDER_MODULE = 'javLibraryCrawl.spiders'
ITEM_PIPELINES = {'javLibraryCrawl.pipelines.MongoDBPipeline':5,}

IMAGES_STORE = 'src/images'

IMAGES_THUMBS = {
    'small': (50, 50),
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "javLibrary"
MONGODB_COLLECTION = "videos"
MONGODB_COLLECTION_ALL = "videos"
MONGODB_COLLECTION_BEST_RATED = "best_rated"
MONGODB_COLLECTION_MOST_WANTED = "most_wanted"
MONGODB_COLLECTION_NEW_RELEASES = "new_releases"
MONGODB_COLLECTION_NEW_ENTRIES = "new_entries"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'javLibraryCrawl (+http://www.yourdomain.com)'
