from elasticsearch import Elasticsearch
from ssl import create_default_context, CERT_NONE
from pk.repo.repository import Repository

class ElasticsearchRepository(Repository):
	def __init__(self):
		context = create_default_context()
		context.check_hostname = False
		context.verify_mode = CERT_NONE
		
		self.__connection = Elasticsearch(
			hosts="https://localhost:9200",
			http_auth=("elastic", "es"),
			ssl_context=context,
			verify_certs=False,
		)
	
	def insert(self, item):
		self.__connection.index(index="index", body=item)
	
	def update(self, item):
		pass
	
	def remove(self, item):
		pass
	
	def select_all(self):
		search_query = {
			"query": {
				"match_all": {}
			}
		}
		
		search_results = self.__connection.search(index="index", body=search_query)
		
		for result in search_results["hits"]["hits"]:
			yield result
