from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from santehnika_tut import settings
from santehnika_tut.spiders.santechspider import SantechspiderSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(SantechspiderSpider)
    process.start()
