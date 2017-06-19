# -*- coding: utf-8 -*-
import scrapy
from scrapyTest.items import ScrapytestItem
from scrapy import Request
import re


# 少帅的spider
class Car(scrapy.Spider):
    name = 'xcar'
    start_urls = ['http://newcar.xcar.com.cn/car/0-0-0-0-0-0-9-0-0-0-0-0/']

    # def start_requests(self):
    #     for i in self.start_urls:
    #         yield scrapy.Request(i,callback=self.parse)
    def parse(self, response):

        xpth = '//div[@class="cenl"]/h6/a/@href'
        link = response.xpath(xpth).extract()

        for i in link:
            url = 'http://newcar.xcar.com.cn' + i
            yield Request(url, callback=self.parse2)
        # xpth='//p[@class="tw_gmpage"]/a[last()]/@href'
        # next_url = response.xpath(xpth).extract()
        net = response.body[response.body.find('tw_gmpage"><a'):response.body.find('id="tw_newcar')]
        print(net)
        url = re.findall(r'/car/0-0-0-0-0-0-9-0-0-0-0-\d/', net)
        # print url
        for i in url:
            yield Request('http://newcar .xcar.com.cn' + i, callback=self.parse)

    def parse2(self, response):

        item = ScrapytestItem()
        xpth = '//span[@class="lt_f1"]/text()|c//div[@class="tt_h1"]/h1/text()'
        name2 = response.xpath(xpth).extract()
        name3 = name2[0] + name2[1]
        item['car_name'] = name3
        xpth = '//div[@class="placepython "]/a[2]/text()'
        type = response.xpath(xpth).extract()
        item['type'] = type[0]
        item['price'] = '123'
        yield item


# 构建项目的spider
class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        print(response.body)


# 文档的spider
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


# 文档的spider2
class Quotes2Spider(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
