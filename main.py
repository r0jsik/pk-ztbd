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
		self.repository = ElasticsearchRepository()
		# self.repository = MongoRepository()
		
	def initialize(self):
		self.repository.create()
	
	@timed
	def select_items(self, title, year, keywords, artist, language):
		return self.repository.select_all(title=title, year=year, keywords=keywords, artist=artist, language=language)
	
	@timed
	def insert_item(self, title, artist, genre, year, language, lyrics):
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
				"views": 0,
				"lyrics": lyrics,
				"lang_cld3": "",
				"lang_ft": "",
				"language": language
			}
		)
	
	@timed
	def import_from_file(self, file_name):
		file_source = FileSource(file_name)
		batch = []
		
		for song in file_source.get_next_song():
			batch.append(song)
			
			if len(batch) == 1000:
				self.repository.insert_all(batch)
				batch.clear()
		
		self.repository.insert_all(batch)


if __name__ == '__main__':
	controller = Controller()
	controller.initialize()
	
	window = Window(controller)
	window.show()
