from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
import random
random.seed(None)
suffix = random.random()
string = "index" + str(suffix)
doc = {
    'Name': 'CUJAH?',
    'Type': 'SZN', 'Place of Origin': 'CUSOH',
    'Service history': {
        'Used by' : 'Cascased',}
    }
res = es.index(index=string, doc_type='tweet', id=1, body=doc)
print(res['created'])

res = es.get(index=string, doc_type='tweet', id=1)
print(res['_source'])
"""
es.indices.refresh(index="indexs")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
print("%(Name)s %(Type)s: %(Place of Origin)s" % hit["_source"])
 """
