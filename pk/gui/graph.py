import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
	def __init__(self, root):
		self.__root = root
	
	def show(self, x, y):
		figure = plt.Figure(figsize=(5, 4), dpi=100)
		figure.add_subplot(111).plot(x, y)
		
		canvas = FigureCanvasTkAgg(figure, master=self.__root)
		canvas.draw()
		
		widget = canvas.get_tk_widget()
		widget.pack()
