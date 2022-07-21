import scrapy


class CorgiThingsItem(scrapy.Item):
    product_title = scrapy.Field()
    product_price = scrapy.Field()
    product_no_of_reviews = scrapy.Field()
    product_image_link = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
