from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
import random
random.seed(None)
suffix = random.random()
DataPoints = {
    'Name': 'HJHJ',
    'Type': 'BAR', 'Place of Origin': 'FOO',
    'Service history': {
        'Used by' : 'FOO',
        'In service' : 'HAZAH' } ,
    'Production_history': {
        'Designer': 'SAMPSON',
        'Designed' : 'JAN',
        'Manufacturer' : 'REALBIBNS',
        'Produced' : 'hjhj',
        'Variants' : 'hjhjhhjhj', },
    'Specifications': {
        'Parent case' : 'hdjhsjd',
        'Case type' : 'HJHSDJS',
        'Bullet diameter' : 'FHKDKF',
        'Neck diameter' : 'HJSD',
        'Shoulder diameter': 'hHDKS',
        'Base diameter' : 'hsdjsdHJ',
        'Rim diameter' : 'DSFHKJSHD',
        'Rim thickness' : 'hdjhsdjfhdsHJ',
        'Case length' : 'SDHJHFJK',
        'Overall length' : 'SDJKSD',
        'Case capacity' : 'HJASHDJS',
        'Rifling twist' : 'ASDFJHJDF',
        'Primer type' : 'HJDSJH',
        'Maximum pressure' : 'JDSFKJKD', },
    'Ballistic_Performance' : {
        'Bullet mass/type': 'SHDFJDSH',
        'Velocity' : 'DSHJSD',
        'Energy': 'SDJDSKFJKSDFJKDS', }}

string = "index" + str(suffix)
res = es.index(index=string, doc_type='tweet', id=1, body=DataPoints)
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
