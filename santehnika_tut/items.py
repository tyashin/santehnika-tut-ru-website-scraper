# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, Identity, MapCompose
from bs4 import BeautifulSoup


class santehnikaTutItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field(output_processor=Identity)
    name = scrapy.Field(output_processor=TakeFirst)

    category = scrapy.Field(output_processor=TakeFirst)
    description = scrapy.Field(input_processor=None, output_processor=Identity)

