import scrapy
from ..items import CorgiThingsItem
from ..utils import get_image_link


class CorgiSpider(scrapy.Spider):
    name = 'corgi'
    allowed_domains = ['corgithings.com']
    start_urls = ['https://corgithings.com/collections/shop']

    def parse(self, response):
        corgi_product_link = response.css('div.product-title a::attr(href)')
        yield from response.follow_all(corgi_product_link, callback=self.parse_corgi_item)

    def parse_corgi_item(self, response):
        item = CorgiThingsItem()

        def extract_with_css(query):
            return response.css(query).get()

        product_title = extract_with_css('h1::text')
        product_price = extract_with_css('span.money::text')
        product_no_of_reviews = extract_with_css('span.jdgm-prev-badge__text::text')
        product_image_link = extract_with_css('div meta[itemprop="image"]')

        if product_title:
            item["product_title"] = product_title
        if product_price:
            item["product_price"] = product_price.rstrip().lstrip()
        if product_no_of_reviews:
            item["product_no_of_reviews"] = product_no_of_reviews
        if product_image_link:
            item["product_image_link"] = get_image_link(product_image_link)

        yield item
