import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.stats import norm
import tkinter as tk
from tkinter import ttk

class Graph:
	def __init__(self, root):
		self.__root = root
		self.fig = plt.Figure(figsize=(5, 4), dpi=100)
		self.plot = self.fig.add_subplot(111)
		self.canvas = FigureCanvasTkAgg(self.fig, master=self.__root)
		self.canvas.get_tk_widget().pack()
		self.average = tk.Label(self.__root, text="Średnia: ")
		self.average.pack()
		self.median = tk.Label(self.__root, text="Mediana: ")
		self.median.pack()
		self.standard_deviation = tk.Label(self.__root, text="Odchylenie standardowe: ")
		self.standard_deviation.pack()
	
	def show(self, x, y):
		figure = plt.Figure(figsize=(5, 4), dpi=100)
		figure.add_subplot(111).plot(x, y)
		
		canvas = FigureCanvasTkAgg(figure, master=self.__root)
		canvas.draw()
		
		widget = canvas.get_tk_widget()
		widget.pack()

	def draw_gauss_dist(self, data):
		mean = np.mean(data)
		std_dev = np.std(data)
		median = np.median(data)
		x = np.linspace(min(data), max(data), 100)
		pdf = norm.pdf(x, mean, std_dev)

		self.plot.cla()
		self.plot.plot(x, pdf, label='Rozkład')
		self.plot.hist(data, bins=10, density=True, alpha=0.5, label='Popularność')
		self.plot.set_xlabel('Popularność')
		self.plot.set_ylabel('Wystąpienia')
		self.plot.legend()

		self.average.config(text="Średnia: {:.2f}".format(mean))
		self.median.config(text="Mediana: {:.2f}".format(median))
		self.standard_deviation.config(text="Odchylenie standardowe: {:.2f}".format(std_dev))

		self.canvas.draw()
