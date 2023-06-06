import time

from pk.gui.window import Window
from pk.repo.elasticearch import ElasticsearchRepository
from pk.repo.mongo import MongoRepository
from pk.repo.postgres import PostgresRepository
from pk.source.file import FileSource


def timed(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		stop = time.time()
		return stop - start, result
	
	return wrapper
	

class Controller:
	def __init__(self):
		# self.repository = PostgresRepository()
		# self.repository = ElasticsearchRepository()
		self.repository = MongoRepository()
		
	def initialize(self):
		# self.repository.create()
		pass
	
	@timed
	def select_items(self, title, year, keywords, artist, language):
		return self.repository.select_all(title=title, year=year, keywords=keywords, artist=artist, language=language)
	
	@timed
	def insert_item(self, title, artist, genre, year, language, views, lyrics):
		self.repository.insert(
			{
				"id": 0,
				"title": title,
				"genre": {
					"id": 0,
					"name": genre
				},
				"artist": {
					"id": 0,
					"name": artist
				},
				"year": int(year),
				"views": int(views),
				"lyrics": lyrics,
				"lang_cld3": "",
				"lang_ft": "",
				"language": language
			}
		)
	
	@timed
	def import_from_file(self, file_name):
		file_source = FileSource(file_name)
		items = []
		
		for item in file_source.get_next_song():
			items.append(item)
			
			if len(items) == 10000:
				self.repository.insert_all(items)
				items = []
				print(item["id"])
		
		self.repository.insert_all(items)


if __name__ == '__main__':
	controller = Controller()
	controller.initialize()
	
	window = Window(controller)
	window.show()
