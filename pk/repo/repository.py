class Repository:
	def create(self):
		raise NotImplementedError()
	
	def insert_all(self, items):
		raise NotImplementedError()

	def insert(self, item):
		raise NotImplementedError()
	
	def update(self, item_id, item):
		raise NotImplementedError()
	
	def remove(self, item_id):
		raise NotImplementedError()
	
	def select_all(self, **criteria):
		raise NotImplementedError()
