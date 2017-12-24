from base_query import BaseQuery
from Query import Query
from base_list import BaseList
from ast import literal_eval


class ProductQuery(BaseQuery):
	def __init__(self, query, filters, sort_by, page_len, page_num):
		super(self.__class__, self).__init__(query.lower(), filters, sort_by, page_len, page_num)

	def create_query(self):
		self.complete_query = Query()
		self.complete_query.QUERY = self.get_bool_query()
		#print (literal_eval(self.complete_query))


	def get_bool_query(self):
		Option = Query()
		Bool = Query()
		Option.MUST = self.get_must_query()
		Bool.BOOL = Option
		#print (literal_eval(Bool))
		return Bool

	def get_must_query(self):
		self.must_list = BaseList()
		self.must_list.add(self.get_title_desc_query_string())
		#print (literal_eval(self.must_list))
		return self.must_list

	def get_match_query(self):
		match_query = Query()
		match_query.MATCH = {"title":self.query}
		#print(literal_eval(match_query))
		return match_query

	def get_title_desc_query_string(self):
		query_string = Query()
		query_string.FIELDS = ["title^2", "long_desc"]
		query_string.QUERY = self.query
		query_string_title_desc = Query()
		query_string_title_desc.QUERY_STRING = query_string
		return query_string_title_desc

			