import time
from pk.gui.window import Window
from pk.repo.postgres import PostgresRepository
#from pk.repo.elasticearch import ElasticsearchRepository
#from pk.repo.mongo import MongoRepository
from pk.source.file import FileSource


def timed(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		stop = time.time()
		return stop - start
	
	return wrapper
	

class Controller:
	def __init__(self):
		self.repository = PostgresRepository()
		# repository = ElasticsearchRepository()
		# repository = MongoRepository()
		
	def initialize(self):
		self.repository.create()
	
	@timed
	def import_from_file(self, file_name):
		file_source = FileSource(file_name)
		
		for song in file_source.get_next_song():
			self.repository.insert(song)
		
		for song in self.repository.select_all():
			print(song.artist)


if __name__ == '__main__':
	controller = Controller()
	controller.initialize()
	
	window = Window(controller)
	window.show()
