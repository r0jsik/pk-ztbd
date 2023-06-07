import tkinter as tk
from tkinter import ttk

from pk.scraper.lyrics_provider import scrap_lyrics


class CreateForm:
	def __init__(self, panel, insert_record_callback, import_records_callback):
		self.panel = panel
		self.insert_record_callback = insert_record_callback
		self.import_records_callback = import_records_callback
		self.title_entry = tk.Entry(self.panel, width=80)
		self.artist_entry = tk.Entry(self.panel, width=80)
		self.genre_entry = tk.Entry(self.panel, width=80)
		self.year_entry = tk.Entry(self.panel, width=80)
		self.language_entry = tk.Entry(self.panel, width=80)
		self.views_entry = tk.Entry(self.panel, width=80)
		self.lyrics_entry = tk.Text(self.panel, width=60, height=10)
	
	def show(self):
		tk.Label(self.panel, text="Tytuł").grid(row=0, column=0, sticky=tk.W)
		self.title_entry.grid(row=0, column=1)
		
		tk.Label(self.panel, text="Wykonawca").grid(row=1, column=0, sticky=tk.W)
		self.artist_entry.grid(row=1, column=1)
		
		tk.Label(self.panel, text="Gatunek").grid(row=2, column=0, sticky=tk.W)
		self.genre_entry.grid(row=2, column=1)
		
		tk.Label(self.panel, text="Rok").grid(row=3, column=0, sticky=tk.W)
		self.year_entry.grid(row=3, column=1)
		
		tk.Label(self.panel, text="Język").grid(row=4, column=0, sticky=tk.W)
		self.language_entry.grid(row=4, column=1)
		
		tk.Label(self.panel, text="Wyświetlenia").grid(row=5, column=0, sticky=tk.W)
		self.views_entry.grid(row=5, column=1)
		
		tk.Label(self.panel, text="Tekst").grid(row=6, column=0, sticky=tk.W)
		self.lyrics_entry.grid(row=6, column=1)
		
		lyrics_button = tk.Button(self.panel, text="Pobierz tekst", command=self.fill_lyrics, width=12)
		lyrics_button.grid(row=7, column=1, sticky=tk.E)
		
		create_button = tk.Button(self.panel, text="Dodaj", command=self.create_record, width=12)
		create_button.grid(row=8, column=1, sticky=tk.E)
		
		import_button = tk.Button(self.panel, text="Importuj", command=self.import_records_callback, width=12)
		import_button.grid(row=9, column=1, sticky=tk.E)
	
	def fill_lyrics(self):
		artist = self.artist_entry.get()
		title = self.title_entry.get()
		lyrics = scrap_lyrics(artist, title)
		
		self.lyrics_entry.delete("1.0", tk.END)
		self.lyrics_entry.insert(tk.END, lyrics)
	
	def create_record(self):
		title = self.title_entry.get()
		artist = self.artist_entry.get()
		genre = self.genre_entry.get()
		year = self.year_entry.get()
		language = self.language_entry.get()
		views = self.views_entry.get()
		lyrics = self.lyrics_entry.get("1.0", tk.END)
		
		self.insert_record_callback(title, artist, genre, year, language, views, lyrics)


class SearchForm:
	def __init__(self, panel, search_records_callback):
		self.panel = panel
		self.search_records_callback = search_records_callback
		self.title_entry = tk.Entry(self.panel, width=80)
		self.year_entry = tk.Entry(self.panel, width=80)
		self.keywords_entry = tk.Entry(self.panel, width=80)
		self.artist_entry = tk.Entry(self.panel, width=80)
		self.language_entry = tk.Entry(self.panel, width=80)
		self.treeview = ttk.Treeview(self.panel)
	
	def show(self):
		tk.Label(self.panel, text="Tytuł").grid(row=0, column=0, sticky=tk.W)
		self.title_entry.grid(row=0, column=1)
		
		tk.Label(self.panel, text="Rok").grid(row=1, column=0, sticky=tk.W)
		self.year_entry.grid(row=1, column=1)
		
		tk.Label(self.panel, text="Słowa kluczowe").grid(row=2, column=0, sticky=tk.W)
		self.keywords_entry.grid(row=2, column=1)
		
		tk.Label(self.panel, text="Wykonawca").grid(row=3, column=0, sticky=tk.W)
		self.artist_entry.grid(row=3, column=1)
		
		tk.Label(self.panel, text="Język").grid(row=4, column=0, sticky=tk.W)
		self.language_entry.grid(row=4, column=1)
		
		search_button = tk.Button(self.panel, text="Szukaj", command=self.update_records, width=12)
		search_button.grid(row=5, column=1, sticky=tk.E)
		
		self.treeview.grid(row=6, column=0, columnspan=2)
		self.treeview["columns"] = ("artist", "title", "views")
		self.treeview["show"] = "headings"
		self.treeview.heading("artist", text="Wykonawca")
		self.treeview.heading("title", text="Tytuł")
		self.treeview.heading("views", text="Wyświetlenia")
	
	def update_records(self):
		title = self.title_entry.get()
		year = self.year_entry.get()
		keywords = self.keywords_entry.get()
		artist = self.artist_entry.get()
		language = self.language_entry.get()
		records = self.search_records_callback(title, int(year) if year else "", keywords, artist, language)
		
		for row in self.treeview.get_children():
			self.treeview.delete(row)
		
		for record in records:
			record = record["artist"]["name"], record["title"], record["views"]
			self.treeview.insert("", "end", values=record)
