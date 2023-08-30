from celery import shared_task
from .models import Shop

@shared_task
def update_product_counts():
    shops = Shop.objects.all()
    for shop in shops:
        shop.product_count = shop.product_set.count()

    Shop.objects.bulk_update(list(shops), ['product_count'])

#
# shops = Shop.objects.annotate(product_count=F('product__id__count'))
# updated_count = shops.update(product_count=F('product_count'))


