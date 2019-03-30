from .models import Things
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Signal to save each new blog post instance into ElasticSearch
@receiver(post_save, sender=Things)
def index_post(sender, instance, **kwargs):
    print(instance)
    instance.indexing()


@receiver(post_delete, sender=Things)
def delete_post(sender, instance, **kwargs):
    print(instance)
    instance.deleting()
