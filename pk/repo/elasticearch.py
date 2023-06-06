from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from pk.repo.repository import Repository


class ElasticsearchRepository(Repository):
    def __init__(self):
        self.__connection = Elasticsearch(
            hosts="http://localhost:9200",
            http_auth=("elastic", "es"),
            verify_certs=False,
            request_timeout=60000
        )
    
    def create(self):
        mapping = {
            "properties": {
                "title": {"type": "text"},
                "genre": {
                    "properties": {
                        "_id": {"type": "keyword"},
                        "name": {"type": "text"}
                    }
                },
                "artist": {
                    "properties": {
                        "_id": {"type": "keyword"},
                        "name": {"type": "text"}
                    }
                },
                "year": {"type": "integer"},
                "views": {"type": "integer"},
                "lyrics": {"type": "text"},
                "lang_cld3": {"type": "keyword"},
                "lang_ft": {"type": "keyword"},
                "language": {"type": "keyword"}
            }
        }
        
        self.__connection.indices.delete(index="index", ignore=[404])
        self.__connection.indices.create(index="index")
        self.__connection.indices.put_mapping(index="index", body=mapping)

    def insert_all(self, items):
        actions = [
            {
                "_index": "index",
                "_source": item
            }
            for item in items
        ]
        
        bulk(self.__connection, actions)

    def insert(self, item):
        self.__connection.index(index="index", body=item)
    
    def update(self, item_id, item):
        self.__connection.update(index="index", id=item_id, body={"doc": item})
    
    def remove(self, item_id):
        self.__connection.delete(index="index", id=item_id)
    
    def select_all(self, **criteria):
        query = {
            "query": {
                "bool": {
                    "must": []
                }
            }
        }
        
        for parameter, value in criteria.items():
            if value:
                query["query"]["bool"]["must"].append({"match": {parameter: value}})
        
        search_results = self.__connection.search(index="index", body=query)
        
        return list(search_results["hits"]["hits"]["_source"])
