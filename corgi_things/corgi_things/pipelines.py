import pymongo


class CorgiMongoPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['corgi_things']
        self.collection = db['corgi_stuff']

    def process_item(self, item, spider):
        global item_dict
        try:
            item_dict = {
                'Title': item['product_title'],
                'Price': item['product_price'],
                'No. reviews': item['product_no_of_reviews'],
                'Link to image': item['product_image_link']
            }
        except KeyError:
            print("corgi broken")
        finally:
            self.collection.insert_one(item_dict)
        return item
