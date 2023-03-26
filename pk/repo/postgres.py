import psycopg2
from pk.repo.repository import Repository

class PostgresRepository(Repository):
	def __init__(self):
		self.__connection = psycopg2.connect(
			host="localhost",
			database="psql",
			user="psql",
			password="psql"
		)
	
	def insert(self, item):
		with self.__connection.cursor() as cursor:
			query = "INSERT INTO mytable (id, name) VALUES (%s, %s)"
			params = (item["id"], item["name"])
			cursor.execute(query, params)
	
	def update(self, item):
		pass
	
	def remove(self, item):
		pass
	
	def select_all(self):
		with self.__connection.cursor() as cursor:
			cursor.execute("SELECT * FROM mytable;")
			rows = cursor.fetchall()
			
			for row in rows:
				yield row
