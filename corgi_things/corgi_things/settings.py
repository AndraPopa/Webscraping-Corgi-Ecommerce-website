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

