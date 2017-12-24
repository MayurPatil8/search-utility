#from abc import abstractmethod
class BaseQuery:
	def __init__(self, query, filters, sort_by, page_len, page_num):
		self.query = query
		self.filters = filters
		self.sort_by = sort_by
		self.page_len = page_len
		self.page_num = page_num
		self.create_query()

	def get_query(self):
		return self.complete_query


