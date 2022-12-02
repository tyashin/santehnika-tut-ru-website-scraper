from urllib.parse import urljoin

import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

from santehnika_tut.items import SantehnikaTutItem
class SantechspiderSpider(scrapy.Spider):
    name = 'santehspider'
    allowed_domains = ['santehnika-tut.ru']
    start_urls = ['https://santehnika-tut.ru/']

    def parse(self, response: HtmlResponse):
        categories_refs = set(response.xpath("//a[@class='link n-w-navigation-menu__node-link b-zone b-spy-events i-bem']/@href").extract())
        yield from response.follow_all(categories_refs, callback=self.category_parse)

    def category_parse(self, response: HtmlResponse):
        last_page_num = response.xpath("//div[@class='pagination']/a/@data-page").get()
        if last_page_num:
            last_page_num = int(last_page_num)
            current_page_num = response.xpath("//div[contains(@class, 'pagination')]/a[@class='_active']/text()").get()
            if current_page_num:
                current_page_num = int(current_page_num)
                if current_page_num < last_page_num:
                    next_page = response.url
                    page_pos = next_page.find('/page')
                    if page_pos != -1:
                        next_page = next_page[:page_pos+1]
                    next_page = f'{next_page}page{current_page_num+1}'
                    yield response.follow(next_page, callback=self.category_parse)

        product_refs = set(response.xpath("//a[@class='img pos_rel']/@href").extract())
        for product_ref in product_refs:
            yield response.follow(product_ref, self.product_parse)

    def product_parse(self, response: HtmlResponse):

        iloader = ItemLoader(item=SantehnikaTutItem(), response=response)
        iloader.add_value('url', response.url)
        iloader.add_xpath('name', "//h1[@itemprop='name']/text()")
        iloader.add_xpath('item_id', "//div[contains(text(), 'Товарный код:')]/text()")
        iloader.add_xpath('article', "//div[@class='info']//span[contains(text(), 'Артикул:')]/../following-sibling::div[@class='val']/text()")

        iloader.add_xpath('description', "//div[@class='content tab_des']/node()")
        iloader.add_xpath('characteristics', "///ul[@class='chars']/node()")
        iloader.add_xpath('category', "(//a[@class='bcsm'])[1]/span/text()")

        yield iloader.load_item()
