import scrapy


class SantechspiderSpider(scrapy.Spider):
    name = 'santechspider'
    allowed_domains = ['santehnika-tut.ru']
    start_urls = ['http://santehnika-tut.ru/']

    def parse(self, response):
        pass
