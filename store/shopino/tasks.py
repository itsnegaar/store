from celery import shared_task
from .models import Shop

@shared_task
def update_product_counts():
    for shop in Shop.objects.all():
        shop.product_count = shop.product_set.count()
        shop.save(update_fields=['product_count'])
