import pymongo
from pk.repo.repository import Repository
from pk.objects.song import Song
from pk.objects.genre import Genre
from pk.objects.author import Author

class MongoRepository(Repository):
	def __init__(self):
		self.__connection = pymongo.MongoClient("mongodb://localhost:27017/", username="root", password="mongo")
		self.__database = self.__connection["mongo"]
		self.__collection = self.__database["songs"]

	def create(self):
		self.__collection.drop()
	
	def insert(self, item):
		to_insert = {
			"_id" : item.id,
			"title" : item.title,
			"genre" : {
				"_id" : item.genre.id,
				"name" : item.genre.name
			},
			"artist" : {
				"_id" : item.artist.id,
				"name" : item.artist.name
			},
			"year" : item.year,
			"views" : item.views,
			"features" : item.features,
			"lyrics" : item.lyrics,
			"lang_cld3" : item.lang_cld3,
			"lang_ft" : item.lang_ft,
			"language" : item.language
		}

		self.__collection.insert_one(to_insert)
	
	def update(self, item):
		pass
	
	def remove(self, item):
		pass
	
	def select_all(self):
		results = self.__collection.find({})
		
		for result in results:
			yield Song(
				result["_id"],
				result["title"],
				Genre(result["genre"]["_id"], result["genre"]["name"]),
				Author(result["artist"]["_id"], result["artist"]["name"]),
				result["year"],
				result["views"],
				result["features"],
				result["lyrics"],
				result["lang_cld3"],
				result["lang_ft"],
				result["language"]
			)
