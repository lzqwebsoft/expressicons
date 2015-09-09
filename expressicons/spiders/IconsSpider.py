#!/bin/env python
# -*- coding: utf8 -*-
import scrapy
from expressicons.items import ExpressiconsItem

class IconSpider(scrapy.Spider):
    name = 'expressicons'
    allowed_domains = ['cdn.kuaidi100.com']

    def __init__(self, category=None, *args, **kwargs):
        super(IconSpider, self).__init__(*args, **kwargs)
        # http://cdn.kuaidi100.com/images/all/56/debangwuliu.png
        self.start_urls = ['http://m.kuaidi100.com/all/']

    def parse(self, response):
        sel = scrapy.Selector(response)
        for category in response.xpath('//section/dl[@id="comList"]/dt'):
            item = ExpressiconsItem()
            item['type'] = "".join(category.xpath("normalize-space(text())").extract())
            companies = []
            for express in category.xpath('following-sibling::dd[1]/a'):
                name = "".join(express.xpath("normalize-space(text())").extract())
                code = "".join(express.xpath("@data-code").extract())
                image = 'http://cdn.kuaidi100.com/images/all/56/' + code + ".png"
                companies.append({'name': name, 'code': code, 'image': image})
            item['companies'] = companies
            yield item

        #for url in response.xpath('//a/@href').extract():
        #   yield scrapy.Request(url, callback=self.parse)
