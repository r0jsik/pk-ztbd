from pk.source.source import Source
import csv


class FileSource(Source):
    def __init__(self, file_path):
        self.file_path = file_path
    
    def get_next_song(self):
        genre_id = 1
        artist_id = 1
        
        genres = set()
        artists = set()
        
        with open(self.file_path, encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            
            # Skip the first line
            next(reader, None)
            
            for index, line in enumerate(reader):
                title, genre, artist, year, views, _, lyrics, song_id, lang_cld3, lang_ft, lang = line
                
                if genre not in genres:
                    genres.add(genre)
                    genre_id += 1
                
                if artist not in artists:
                    artists.add(artist)
                    artist_id += 1
                
                yield {
                    "id": song_id,
                    "title": title,
                    "genre": {
                        "id": genre_id,
                        "name": genre
                    },
                    "artist": {
                        "id": artist_id,
                        "name": artist
                    },
                    "year": int(year),
                    "views": views,
                    "lyrics": lyrics,
                    "lang_cld3": lang_cld3,
                    "lang_ft": lang_ft,
                    "language": lang
                }
