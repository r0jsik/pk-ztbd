import tkinter as tk
from tkinter import ttk


class CreateForm:
	def __init__(self, panel, insert_record_callback, import_records_callback):
		self.panel = panel
		self.insert_record_callback = insert_record_callback
		self.import_records_callback = import_records_callback
		self.title_entry = tk.Entry(self.panel)
		self.artist_entry = tk.Entry(self.panel)
		self.genre_entry = tk.Entry(self.panel)
		self.year_entry = tk.Entry(self.panel)
		self.language_entry = tk.Entry(self.panel)
		self.keywords_entry = tk.Entry(self.panel)
	
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
		
		tk.Label(self.panel, text="Słowa kluczowe").grid(row=5, column=0, sticky=tk.W)
		self.keywords_entry.grid(row=5, column=1)
		
		create_button = tk.Button(self.panel, text="Utwórz", command=self.create_record)
		create_button.grid(row=6, column=1, sticky=tk.E)
		
		import_button = tk.Button(self.panel, text="Importuj", command=self.import_records_callback)
		import_button.grid(row=7, column=1, sticky=tk.E)
	
	def create_record(self):
		title = self.title_entry.get()
		artist = self.artist_entry.get()
		genre = self.genre_entry.get()
		year = self.year_entry.get()
		language = self.language_entry.get()
		keywords = self.keywords_entry.get()
		
		self.insert_record_callback(title, artist, genre, year, language, keywords)


class SearchForm:
	def __init__(self, panel, search_records_callback):
		self.panel = panel
		self.search_records_callback = search_records_callback
		self.title_entry = tk.Entry(self.panel)
		self.year_entry = tk.Entry(self.panel)
		self.keywords_entry = tk.Entry(self.panel)
		self.artist_entry = tk.Entry(self.panel)
		self.language_entry = tk.Entry(self.panel)
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
		
		search_button = tk.Button(self.panel, text="Szukaj", command=self.update_records)
		search_button.grid(row=5, column=1)
		
		self.treeview.grid(row=6, column=0, columnspan=2)
		self.treeview["columns"] = ("title", "popularity")
		self.treeview["show"] = "headings"
		self.treeview.heading("title", text="Tytuł")
		self.treeview.heading("popularity", text="Popularność")
	
	def update_records(self):
		title = self.title_entry.get()
		year = self.year_entry.get()
		keywords = self.keywords_entry.get()
		artist = self.artist_entry.get()
		language = self.language_entry.get()
		records = self.search_records_callback(title, year, keywords, artist, language)
		
		for row in self.treeview.get_children():
			self.treeview.delete(row)
		
		for record in records:
			record = record["title"], record["popularity"]
			self.treeview.insert("", "end", values=record)
