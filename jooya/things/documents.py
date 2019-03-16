from django_elasticsearch_dsl import DocType, Index
from .models import Things

# Name of the Elasticsearch index
thing = Index('things')
# See Elasticsearch Indices API reference for available settings
thing.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@thing.doc_type
class ThingDocument(DocType):
    class Meta:
        model = Things  # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
            'description',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000