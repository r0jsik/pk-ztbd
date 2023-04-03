import tkinter as tk
from tkinter import filedialog
from pk.gui.graph import Graph

class Window:
	def __init__(self):
		self.__root = tk.Tk()
		self.__root.geometry("600x480")
		self.__root.title("Projekt ZTBD")
		
		self.__label = tk.Label(self.__root, text="")
		self.__label.pack()
		
		graph = Graph(self.__root)
		canvas = graph.prepare_canavs()
		canvas.pack()
		
		button = tk.Button(self.__root, text="Import data", command=self.open_file_explorer)
		button.pack()
	
	def open_file_explorer(self):
		filename = tk.filedialog.askopenfilename(filetypes=[("Dokumenty JSON", "*.json")])
		self.change_label_text(filename)
	
	def change_label_text(self, text):
		self.__label.config(text=text)
		self.__root.update()
	
	def show(self):
		self.__root.mainloop()
