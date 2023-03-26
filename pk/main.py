from pk.repo.postgres import PostgresRepository
from pk.repo.elasticearch import ElasticsearchRepository
from pk.repo.mongo import MongoRepository

if __name__ == '__main__':
	repository = PostgresRepository()
	#repository = ElasticsearchRepository()
	#repository = MongoRepository()
	results = repository.select_all()
	
	repository.insert({
		"id": 1,
		"name": "test"
	})
	
	for result in results:
		print(result)
