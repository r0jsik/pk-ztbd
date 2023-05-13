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
    def __init__(self, controller):
        self.__controller = controller
        
        self.__root = tk.Tk()
        self.__root.geometry("600x480")
        self.__root.title("Projekt ZTBD")
        
        self.__label = tk.Label(self.__root, text="")
        self.__label.pack()
        
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
    
    def insert_record(self, title, artist, genre, year, language, lyrics):
        duration, _ = self.__controller.insert_record(title, artist, genre, year, language, lyrics)
        self.show_duration(duration)
    
    def import_records(self):
        filename = tk.filedialog.askopenfilename(filetypes=[("Dokumenty CSV", "*.csv")])
        
        if filename:
            duration, _ = self.__controller.import_from_file(filename)
            self.show_duration(duration)
    
    def show_duration(self, duration):
        self.__label.config(text=f"Czas ostatniej operacji: {duration:.3f}s")
    
    def search_records(self, title, year, keywords, artist, language):
        duration, records = self.__controller.select_records(title, year, keywords, artist, language)
        self.show_duration(duration)
        
        for record in records:
            yield {"title": record.title, "popularity": record.views}
    
    def show(self):
        self.__root.mainloop()
