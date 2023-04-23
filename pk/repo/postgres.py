import psycopg2
from pk.repo.repository import Repository
from pk.objects.song import Song
from pk.objects.genre import Genre
from pk.objects.author import Author

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

			query = "DROP TABLE IF EXISTS song_authors"
			cursor.execute(query)

			query = "DROP TABLE IF EXISTS song_genres"
			cursor.execute(query)

			query = """CREATE TABLE "song_lyrics" (
			"id" integer PRIMARY KEY,
			"title" varchar,
			"genre" integer,
			"artist" integer,
			"year" integer,
			"views" integer,
			"features" varchar,
			"lyrics" varchar,
			"lang_cld3" varchar,
			"lang_ft" varchar,
			"language" varchar
			);"""
			cursor.execute(query)

			query = """CREATE TABLE "song_authors" (
			"id" integer PRIMARY KEY,
			"name" varchar
			);"""
			cursor.execute(query)

			query = """CREATE TABLE "song_genres" (
			"id" integer PRIMARY KEY,
			"name" varchar
			);"""
			cursor.execute(query)		
	
	def insert(self, item):
		with self.__connection.cursor() as cursor:
			query = ("INSERT INTO song_lyrics "
	     			"(id, title, genre, artist, year, views, features, lyrics, lang_cld3, lang_ft, language) "
					"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);")
			params = (item.id, item.title, item.genre.id, item.artist.id, item.year, item.views,
	     			  item.features, item.lyrics, item.lang_cld3, item.lang_ft, item.language)
			cursor.execute(query, params)

			query = ("INSERT INTO song_authors "
	    			 "(id, name)" 
					 "VALUES (%s, %s) "
					 "ON CONFLICT DO NOTHING;")
			params = (item.artist.id, item.artist.name)
			cursor.execute(query, params)

			query = ("INSERT INTO song_genres "
	    			 "(id, name)" 
					 "VALUES (%s, %s) "
					 "ON CONFLICT DO NOTHING;")
			params = (item.genre.id, item.genre.name)
			cursor.execute(query, params)
	
	def update(self, item):
		pass
	
	def remove(self, item):
		pass
	
	def select_all(self):
		with self.__connection.cursor() as cursor:
			cursor.execute("SELECT song_lyrics.id, title, song_genres.id, song_genres.name, song_authors.id, song_authors.name, year, views, features, lyrics, lang_cld3, lang_ft, language "
		   				   "FROM song_lyrics, song_authors, song_genres "
						   "WHERE song_lyrics.genre = song_genres.id AND song_lyrics.artist = song_authors.id;")
			rows = cursor.fetchall()
			
			for row in rows:
				id, title, genre_id, genre_name, artist_id, artist_name, year, views, features, lyrics, lang_cld3, lang_ft, language = row
				yield Song(id, title, Genre(genre_id, genre_name), Author(artist_id, artist_name), year, views, features, lyrics, lang_cld3, lang_ft, language)
