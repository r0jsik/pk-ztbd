import tkinter as tk
import numpy as np
from tkinter import filedialog, ttk

from pk.gui.form import CreateForm, SearchForm
from pk.gui.graph import Graph


class Tab(ttk.Frame):
    def __init__(self, tab_panel):
        super().__init__(tab_panel)
        self.tab_panel = tab_panel
    
    def show(self, title):
        self.tab_panel.add(self, text=title)


class Window:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.geometry("600x480")
        self.__root.title("Projekt ZTBD")
        
        self.tab_panel = ttk.Notebook(self.__root)
        
        creator_tab = Tab(self.tab_panel)
        creator_tab.show("Wstawianie")
        
        search_tab = Tab(self.tab_panel)
        search_tab.show("Wyszukiwanie")
        
        summary_tab = Tab(self.tab_panel)
        summary_tab.show("Podsumowanie")
        
        self.tab_panel.pack(expand=1, fill="both")
        
        create_form = CreateForm(creator_tab, self.insert_record, self.import_records)
        create_form.show()
        
        search_form = SearchForm(search_tab, self.search_records)
        search_form.show()
        
        x = np.arange(0, 4 * np.pi, 0.1)
        y = np.sin(x)
        
        graph = Graph(summary_tab)
        graph.show(x, y)
    
    def insert_record(self, title, artist, genre, year, language, keywords):
        print(f"Saved record: {title}, {artist}, {genre}, {year}, {language}, {keywords}")
    
    def import_records(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Dokumenty JSON", "*.json")])
        print(f"import from {filename}")
    
    def search_records(self, title, year, keywords, artist, language):
        return [
            {"title": "The Catcher in the Rye", "popularity": 1000},
            {"title": "To Kill a Mockingbird", "popularity": 1000},
            {"title": "1984", "popularity": 1000},
            {"title": "One Hundred Years of Solitude", "popularity": 1000}
        ]
    
    def show(self):
        self.__root.mainloop()
