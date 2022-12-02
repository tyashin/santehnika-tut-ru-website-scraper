# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, Identity, MapCompose
from bs4 import BeautifulSoup
from w3lib.html import remove_tags

def extract_id(value):
    return value[0].replace('Товарный код:', '').strip()


def extract_description(value):
    return remove_tags("".join(value)).strip().replace("  ", "")

def extract_characteristics(value):
    return remove_tags("###".join(value)).strip().replace("  ", "")

class SantehnikaTutItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field(output_processor=Identity())
    name = scrapy.Field(output_processor=TakeFirst())
    item_id = scrapy.Field(output_processor=extract_id)
    article = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=extract_description)
    characteristics = scrapy.Field(output_processor=extract_characteristics)


