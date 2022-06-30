import scrapy


class CorgiSpider(scrapy.Spider):
    name = 'corgi'
    allowed_domains = ['corgithings.com']
    start_urls = ['http://corgithings.com/']

    def parse(self, response):
        pass
