import pymongo


class CorgiThingsPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['corgi_things']
        self.collection = db['corgi_stuff']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
