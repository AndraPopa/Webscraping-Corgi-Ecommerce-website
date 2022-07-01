BOT_NAME = 'corgi_things'

SPIDER_MODULES = ['corgi_things.spiders']
NEWSPIDER_MODULE = 'corgi_things.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'corgi_things.pipelines.CorgiMongoPipeline': 300,
   'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_STORE = 'F:\Stefanini\scrapy_corgi\corgi_things\corgi_things\image_downloads'

