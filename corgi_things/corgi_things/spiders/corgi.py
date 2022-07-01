import scrapy
from ..items import CorgiThingsItem


class CorgiSpider(scrapy.Spider):
    name = 'corgi'
    page_number = 2
    allowed_domains = ['corgithings.com']
    start_urls = ['https://corgithings.com/collections/shop']

    def parse(self, response):
        corgi_product_link = response.css('div.product-title a::attr(href)')
        yield from response.follow_all(corgi_product_link, callback=self.parse_corgi_item)

        next_page = response.css('link[rel="next"]::attr(href)')
        if next_page:
            abs_url = f"https://corgithings.com{next_page}"
            yield from response.follow_all(abs_url, callback=self.parse)

    def parse_corgi_item(self, response):
        item = CorgiThingsItem()

        def extract_with_css(query):
            return response.css(query).get()

        product_title = extract_with_css('h1::text')
        product_price = extract_with_css('span.money::text')
        product_no_of_reviews = extract_with_css('span.jdgm-prev-badge__text::text')
        product_image_link = extract_with_css('div meta[itemprop="image"]::attr(content)')

        images = list()
        for img in response.css('div meta[itemprop="image"]::attr(content)').getall():
            images.append(response.urljoin(img))

        if product_title:
            item["product_title"] = product_title
        if product_price:
            item["product_price"] = product_price.rstrip().lstrip()
        if product_no_of_reviews:
            item["product_no_of_reviews"] = product_no_of_reviews.rstrip().lstrip()
        if product_image_link:
            item["product_image_link"] = product_image_link

        yield item
        yield {
            'image_urls': images
        }
