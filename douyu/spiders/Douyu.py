# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = "Douyu"
    allowed_domains = ["capi.douyucdn.cn"]
    offset=0
    url="http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url+str(offset)]

    def parse(self, response):
        # 将从json里获取的数据转换成python对象 data段数据集合 response.text获取内容
        data=json.loads(response.text)["data"]
        for each in data:
            item=DouyuItem()
            item["nickname"]=each["nickname"]
            item["imagelink"]=each["vertical_src"]
            yield item
        self.offset+=100
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
