# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CorgiThingsItem(scrapy.Item):
    product_title = scrapy.Field()
    product_price = scrapy.Field()
    product_no_of_reviews = scrapy.Field()
