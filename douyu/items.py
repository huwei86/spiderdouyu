# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 存储照片的名字
    nickname=scrapy.Field()
    # 照片的url路径
    imagelink=scrapy.Field()
    # 照片保存在本地的路径
    imagepath=scrapy.Field()
