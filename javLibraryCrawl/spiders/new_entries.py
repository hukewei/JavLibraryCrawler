from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import log

from javLibraryCrawl.items import JavlibrarycrawlItem


class BestRatedSpider(CrawlSpider):
    name = "new_entries_spider"
    allowed_domains = ["javlibrary.com"]
    start_urls = [
        "http://www.javlibrary.com/cn/vl_newentries.php?&mode=&page=25",
    ]
    rules = (
        # Extract links matching 'category.php'
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=('vl_newentries\.php', ))),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(allow=(r'/\?v=jav.*',)), callback='parse_video', follow=True),
    )

    def parse_video(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://www.javlibrary.com/cn/vl_newentries.php
        @url http://www.javlibrary.com/cn/vl_newentries.php
        @scrapes name
        """
        video = Selector(response)
        items = []

        item = JavlibrarycrawlItem()
        item['url'] = response.request.url
        item['image_urls'] = video.xpath("//*[@id='video_jacket_img']/@src").extract()
        item['title'] = video.xpath("//h3/a/text()").extract()[0]
        item['designation'] = video.xpath('//*[@id="video_id"]/table/tr/td[2]/text()').extract()[0]
        item['category'] = video.xpath('//*[@class="genre"]/a/text()').extract()
        item['actor'] = video.xpath('//*[@class="star"]/a/text()').extract()
        item['duration'] = video.xpath('//*[@id="video_length"]/table/tr/td[2]/span/text()').extract()
        item['release_date'] = video.xpath('//*[@id="video_date"]/table/tr/td[2]/text()').extract()
        items.append(item)

        return items