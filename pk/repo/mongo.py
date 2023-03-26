import pymongo
from pk.repo.repository import Repository

class MongoRepository(Repository):
	def __init__(self):
		self.__connection = pymongo.MongoClient("mongodb://localhost:27017/", username="mongo", password="mongo")
		self.__database = self.__connection["mongo"]
		self.__collection = self.__database["your-collection-name"]
	
	def insert(self, item):
		self.__collection.insert_one(item)
	
	def update(self, item):
		pass
	
	def remove(self, item):
		pass
	
	def select_all(self):
		results = self.__collection.find({})
		
		for result in results:
			yield result
