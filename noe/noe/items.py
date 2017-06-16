# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NoeItem(scrapy.Item):
    # define the fields for your item here like:
    car_name = scrapy.Field()
    type = scrapy.Field()
    price = scrapy.Field()
    pass
