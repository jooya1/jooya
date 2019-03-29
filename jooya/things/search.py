from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# Create a connection to ElasticSearch
connections.create_connection()


# ElasticSearch "model" mapping out what fields to index
class ThingIndex(DocType):
    user = Text()
    date_added = Date()
    title = Text()
    description = Text()
    image = Text()

    class Meta:
        index = 'things-index'


# Bulk indexing function, run in shell
def bulk_indexing():
    ThingIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Things.objects.all().iterator()))


# Simple search function
def search(user):
    s = Search().filter('term', user=user)
    response = s.execute()
    return response