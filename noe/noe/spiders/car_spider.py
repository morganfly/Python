from noe.items import NoeItem
import scrapy
from scrapy import Request
class Car(scrapy.Spider):
    name = 'xcar'
    start_urls=['http://newcar.xcar.com.cn/car/0-0-0-0-0-0-9-0-0-0-0-0/']
    # def start_requests(self):
    #     for i in self.start_urls:
    #         yield scrapy.Request(i,callback=self.parse)
    def parse(self, response):
        xpth='//div[@class="cenl"]/h6/a/@href'
        link=response.xpath(xpth).extract()

        for i in link:

            url = 'http://newcar.xcar.com.cn'+i
            print(url)
            yield Request(url,callback=self.parse2)
    def parse2(self,response):

        item=NoeItem()
        xpth = '//span[@class="lt_f1"]/text()|//div[@class="tt_h1"]/h1/text()'
        name2= response.xpath(xpth).extract()
        name3=name2[0]+name2[1]
        item['car_name']=name3
        xpth = '//div[@class="place"]/a[2]/text()'
        type = response.xpath(xpth).extract()
        item['type'] = type[0]
        item['price'] = '123'
        yield item