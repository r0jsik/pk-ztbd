class Repository:
	def insert(self, item):
		raise NotImplementedError()
	
	def update(self, item):
		raise NotImplementedError()
	
	def remove(self, item):
		raise NotImplementedError()
	
	def select_all(self):
		raise NotImplementedError()
