from .models import Product, Shop
from .serializers import ShopSerializer, ProductSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination

from django.http import Http404
from django.shortcuts import get_object_or_404

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'followers': ['gte', 'lte'],
    }

    class pagination_class(pagination.PageNumberPagination):
        page_size = 5
        page_size_query_param = 'page_size'
        max_page_size = 10
        page_query_param = 'p'

    # pagination_class = CustomPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ShopsProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        shop_id = self.kwargs['id']
        shop= get_object_or_404(Shop, id=shop_id)
            # Product.objects.filter(shop=shop))
        return Product.objects.filter(shop=shop)
        # Products = Product.objects.filter(shop=shop)

        # try:
        #     queryset = Shop.objects.get(id=shop)
        #     return Product.objects.filter(shop=shop)
        #
        # except:
        #     raise Http404
        # shop_ids = Shop.objects.values_list('id', flat=True)
        # shop =self.kwargs['id']
        # if int(shop) in shop_ids:
        #     return Product.objects.filter(shop=shop)
        # else:
        #     raise Http404
