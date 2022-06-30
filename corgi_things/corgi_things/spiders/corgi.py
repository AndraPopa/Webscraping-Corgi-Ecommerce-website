import scrapy
from corgi_things.corgi_things.items import CorgiThingsItem

class CorgiSpider(scrapy.Spider):
    name = 'corgi'
    allowed_domains = ['corgithings.com']
    start_urls = ['https://corgithings.com/collections/shop']

    def parse(self, response):
        corgi_product_link = response.css('div.product-title::attr(href)')
        yield from response.follow_all(corgi_product_link, callback=self.parse_corgi_item)

    def parse_corgi_item(self):
        pass
