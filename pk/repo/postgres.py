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
    
    def create(self):
        with self.__connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS songs;")
            cursor.execute("DROP TABLE IF EXISTS artists;")
            cursor.execute("DROP TABLE IF EXISTS genres;")
            
            cursor.execute("""
                CREATE TABLE songs (
                    "id" SERIAL PRIMARY KEY,
                    "title" varchar,
                    "genre_id" integer,
                    "artist_id" integer,
                    "year" integer,
                    "views" integer,
                    "lyrics" varchar,
                    "lang_cld3" varchar,
                    "lang_ft" varchar,
                    "language" varchar
                    );
            """)
            
            cursor.execute("""
                CREATE TABLE artists (
                    "id" SERIAL PRIMARY KEY,
                    "name" varchar
                );
            """)
            
            cursor.execute("""
                CREATE TABLE genres (
                    "id" SERIAL PRIMARY KEY,
                    "name" varchar
                );
            """)

    def insert_all(self, items):
        pass

    def insert(self, item):
        with self.__connection.cursor() as cursor:
            query = "INSERT INTO artists (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING;"
            params = (item["artist"]["id"], item["artist"]["name"])
            cursor.execute(query, params)
    
            query = "INSERT INTO genres (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING;"
            params = (item["genre"]["id"], item["genre"]["name"])
            cursor.execute(query, params)
            
            query = "INSERT INTO songs" \
                    " (id, title, genre_id, artist_id, year, views, lyrics, lang_cld3, lang_ft, language)" \
                    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            params = (item["id"], item["title"], item["genre"]["id"], item["artist"]["id"], item["year"], item["views"],
                      item["lyrics"], item["lang_cld3"], item["lang_ft"], item["language"])
            cursor.execute(query, params)
    
    def update(self, item_id, item):
        with self.__connection.cursor() as cursor:
            query = """
                        UPDATE songs
                        SET title = %s, genre_id = %s, artist_id = %s, year = %s, views = %s, lyrics = %s,
                            lang_cld3 = %s, lang_ft = %s, language = %s
                        WHERE id = %s;
                    """
            params = (item["title"], item["genre"]["id"], item["artist"]["id"], item["year"], item["views"],
                      item["lyrics"], item["lang_cld3"], item["lang_ft"], item["language"], item_id)
            cursor.execute(query, params)
        
        self.__connection.commit()
    
    def remove(self, item_id):
        with self.__connection.cursor() as cursor:
            query = "DELETE FROM songs WHERE id = %s;"
            params = (item_id,)
            cursor.execute(query, params)
        
        self.__connection.commit()
    
    def select_all(self, **criteria):
        with self.__connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    s.id, title, g.id, g.name, a.id, a.name, year, views, lyrics, lang_cld3, lang_ft, language
                FROM
                    songs s JOIN artists a ON s.artist_id = a.id JOIN genres g ON s.genre_id = g.id;
            """)
            
            rows = cursor.fetchall()
            
            for row in rows:
                song_id, title, genre_id, genre, artist_id, artist, year, views, lyrics, lang_cld3, lang_ft, lang = row
                
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
                    "year": year,
                    "views": views,
                    "lyrics": lyrics,
                    "lang_cld3": lang_cld3,
                    "lang_ft": lang_ft,
                    "language": lang
                }
