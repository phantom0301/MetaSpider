# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from MetaCrawler.items import MetacrawlerItem


class Phantom0301Spider(CrawlSpider):
    name = 'phantom0301'
    allowed_domains = ['phantom0301.cc']
    start_urls = ['http://phantom0301.cc/']

    rules = (
        Rule(LinkExtractor(allow=('page/.*/'))),
        Rule(LinkExtractor(allow=('[0-9]{4}/[0-9]{2}/[0-9]{2}/.*/')),callback='parse_item')
    )

    def parse_item(self, response):
        item = MetacrawlerItem()
        selector = scrapy.Selector(response)
        item['src'] = selector.xpath('//img/@src').extract()
        mid = []
        for src in selector.xpath('//img/@src').extract():
            mid.append(src.split('/')[-1])
        item['title'] = mid
        print(item)
        time.sleep(1)
        yield item

