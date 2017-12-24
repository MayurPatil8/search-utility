from elasticsearch import Elasticsearch
from pprint import pprint


es = Elasticsearch()
#res = es.get(index="learn_analyzer",id =1)
#pprint (res)
res = es.search(index="learn_analyzer", body={"query": {"match_all": {}}})
# pprint (res)
# print(len(res['hits']['hits']))
 
res = es.search(index="learn_analyzer", body={"query": {"bool": {}}})
pprint (res)
print(len(res['hits']['hits']))