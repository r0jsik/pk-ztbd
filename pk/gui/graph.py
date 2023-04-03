import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
	def __init__(self, root):
		self.__root = root
	
	def prepare_canavs(self):
		fig = plt.Figure(figsize=(5, 4), dpi=100)
		
		# Generate some data
		x = np.arange(0, 4 * np.pi, 0.1)
		y = np.sin(x)
		
		# Plot the data on the figure
		fig.add_subplot(111).plot(x, y)
		
		# Embed the figure in the tkinter window
		canvas = FigureCanvasTkAgg(fig, master=self.__root)
		canvas.draw()
		canvas = canvas.get_tk_widget()
		
		return canvas
