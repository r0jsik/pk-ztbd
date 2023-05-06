from pk.source.source import Source
from pk.objects.song import Song
from pk.objects.genre import Genre
from pk.objects.author import Author
import csv

class FileSource:
	def __init__(self, file_path):
		self.file_path = file_path

	def get_next_song(self):
		author_id = 1
		genre_id = 1

		authors = {}
		genres = {}
		with open(self.file_path, encoding="utf-8") as csv_file:
			reader = csv.reader(csv_file)
			for index, line in enumerate(reader):
				if index == 0:
					continue

				elif index > 1000:
					break

				title, tag, artist, year, views, features, lyrics, id, language_cld3, language_ft, language = line

				if tag not in genres:
					genres[tag] = Genre(genre_id, tag)
					genre_id += 1

				if artist not in authors:
					authors[artist] = Author(author_id, artist)
					author_id += 1

				yield Song(id, title, genres[tag], authors[artist], year, views, features, lyrics, language_cld3, language_ft, language)