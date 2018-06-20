# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from douban_movie.items import DoubanMovieItem

class DoubanMovieSpider(CrawlSpider):
    name = 'movie'
    #allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']
    rules = (
        Rule(LinkExtractor(allow='https://movie.douban.com/subject/\d+/\?from=subject-page'),
            callback = 'parse_item',
            follow = True
        ),
    )

    def parse_item(self, response):
        yield DoubanMovieItem({
            'url':response.url,
            'name':response.xpath('//span[@property="v:itemreviewed"]/text()').extract(),
            'summary':response.xpath('//span[@property="v:summary"]/text()').extract_first(),
            'score':response.xpath('//strong[@property="v:average"]/text()').extract_first()
        })
