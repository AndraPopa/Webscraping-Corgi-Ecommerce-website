from scrapy.settings.default_settings import DOWNLOADER_MIDDLEWARES

BOT_NAME = 'corgi_things'

SPIDER_MODULES = ['corgi_things.spiders']
NEWSPIDER_MODULE = 'corgi_things.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'corgi_things.pipelines.CorgiMongoPipeline': 300,
   'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_STORE = 's3://store-the-corgi-pictures-23021998/images/'
IMAGES_STORE_S3_ACL = 'public-read'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
}

USER_AGENTS = [
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 '
     'Firefox/55.0')  # firefox
]

