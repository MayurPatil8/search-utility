from product_query import ProductQuery
from ast import literal_eval
from elasticsearch import Elasticsearch
from pprint import pprint

class BaseBuilder():
	HOST = "http://es-search-cluster.edmodoqabranch.com:9200"
	INDEX = "spotlight_qa"
	DOC_TYPE = "product"
	def __init__(self, query, sort_by=3 ,page_len=2, page_num=1, filters={}):
		self.query = query
		self.filters = filters
		self.sort_by = sort_by
		self.page_len = page_len
		self.page_num = page_num

	def build_and_execute_query(self):
		query_list = [ProductQuery]
		body = []
		for query in query_list:
			es_query = query(self.query, self.filters, self.sort_by, self.page_len, self.page_num)
			self.query_body = literal_eval(str(es_query.get_query()))
			self.execute_query()

	def execute_query(self):
		es = Elasticsearch(self.HOST)

		response = es.search(index=self.INDEX,
							 doc_type=self.DOC_TYPE,
							 body=self.query_body,
							 #size=self.page_len,
							 #from_=(self.page_num-1)*self.page_len,
							 _source=["title", "long_desc"])
		pprint (response)



builder = BaseBuilder("internal",2,3,2,{"surname":"patil"})
builder.build_and_execute_query()

# from filter_base import Parent
#
# class Child(Parent):
#
# 	pass
#
# c = Child()
