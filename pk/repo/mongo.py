import pymongo
from pk.repo.repository import Repository


class MongoRepository(Repository):
    def __init__(self):
        self.__connection = pymongo.MongoClient("mongodb://localhost:27017/", username="mongo", password="mongo")
        self.__database = self.__connection["mongo"]
        self.__collection = self.__database["songs"]
    
    def create(self):
        self.__collection.drop()

    def insert_all(self, items):
        self.__collection.insert_many(items)

    def insert(self, item):
        self.__collection.insert_one(item)
    
    def update(self, item_id, item):
        update_query = {
            "$set": item
        }
    
        self.__collection.update_one({"_id": item_id}, update_query)
    
    def remove(self, item_id):
        self.__collection.delete_one({"_id": item_id})
    
    def select_all(self, **criteria):
        query = {}
        
        for parameter, value in criteria.items():
            if value:
                query[parameter] = value
        
        for result in self.__collection.find(query):
            yield result
