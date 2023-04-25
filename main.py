from pk.gui.window import Window
from pk.repo.postgres import PostgresRepository
#from pk.repo.elasticearch import ElasticsearchRepository
#from pk.repo.mongo import MongoRepository
from pk.source.file import FileSource

if __name__ == '__main__':
	source = FileSource()
	
	repository = PostgresRepository()
	#repository = ElasticsearchRepository()
	#repository = MongoRepository()
	repository.create()
	
	for song in source.get_next_song():
		repository.insert(song)
	
	results = repository.select_all()
	for song in results:
		print(song.artist)
	
	window = Window()
	window.show()
