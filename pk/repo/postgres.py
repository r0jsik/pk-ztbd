import psycopg2
from pk.repo.repository import Repository
from pk.objects.song import Song

class PostgresRepository(Repository):
	def __init__(self):
		self.__connection = psycopg2.connect(
			host="localhost",
			database="psql",
			user="psql",
			password="psql"
		)

	def create(self):
		with self.__connection.cursor() as cursor:
			query = "DROP TABLE IF EXISTS song_lyrics"
			cursor.execute(query)

			query = """CREATE TABLE "song_lyrics" (
			"id" integer PRIMARY KEY,
			"title" varchar,
			"tag" varchar,
			"artist" varchar,
			"year" integer,
			"views" integer,
			"features" varchar,
			"lyrics" varchar,
			"lang_cld3" varchar,
			"lang_ft" varchar,
			"language" varchar
			);"""
			cursor.execute(query)
	
	def insert(self, item):
		with self.__connection.cursor() as cursor:
			query = ("INSERT INTO song_lyrics "
	     			"(id, title, tag, artist, year, views, features, lyrics, lang_cld3, lang_ft, language) "
					"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
			params = (item.id, item.title, item.tag, item.artist, item.year, item.views,
	     			  item.features, item.lyrics, item.lang_cld3, item.lang_ft, item.language)
			cursor.execute(query, params)
	
	def update(self, item):
		pass
	
	def remove(self, item):
		pass
	
	def select_all(self):
		with self.__connection.cursor() as cursor:
			cursor.execute("SELECT id, title, tag, artist, year, views, features, lyrics, lang_cld3, lang_ft, language FROM song_lyrics;")
			rows = cursor.fetchall()
			
			for row in rows:
				id, title, tag, artist, year, views, features, lyrics, lang_cld3, lang_ft, language = row
				yield Song(id, title, tag, artist, year, views, features, lyrics, lang_cld3, lang_ft, language)
