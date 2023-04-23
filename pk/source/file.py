from pk.objects.song import Song
import pandas as pd

class FileSource:
	def __init__(self):
		self.df = pd.read_csv("data/song_lyrics.csv")

	def get(self):
		for index, line in self.df.iterrows():
			song = Song(line["id"], line["title"], line["tag"], line["artist"], line["year"],
	       				line["views"], line["features"], line["lyrics"], line["language_cld3"], line["language_ft"], line["language"])

			yield song
