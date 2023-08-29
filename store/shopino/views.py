from .models import Product, Shop , UserBookmark
from .serializers import ShopSerializer, ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination

from rest_framework import views, viewsets, permissions, status, response

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView

from datetime import datetime

from rest_framework import permissions

from django.db.models import Count




class ShopViewSet(viewsets.ModelViewSet):
    # queryset = Shop.objects.all()
    queryset = Shop.objects.annotate(product_count=Count('product'))
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



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class ShopsProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        shop_id = self.kwargs['id']
        shop = get_object_or_404(Shop, id=shop_id)
        return Product.objects.filter(shop=shop)


class BookmarkView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id=None):
        try:
            product = get_object_or_404(Product, pk=id)
            is_bookmarked = product.bookmarked_by.filter(pk=request.user.pk).exists()

            if is_bookmarked:
                product.bookmarked_by.remove(request.user)
                UserBookmark.objects.filter(user=request.user, product=product).delete()
                message = 'Product is not bookmarked anymore.'
            else:
                product.bookmarked_by.add(request.user)
                UserBookmark.date_bookmarked = datetime.now()
                message = 'Product bookmarked successfully.'

            return response.Response({'message': message, 'product_id': id})
        except Product.DoesNotExist:
            return response.Response({'error': 'Product not found.'})



class BookmarkedUsersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id, *args, **kwargs):
        try:
            product = Product.objects.get(pk=product_id)
            bookmarked_users = product.bookmarked_by.all()
            bookmarked_usernames = [user.username for user in bookmarked_users]
            return response.Response({'bookmarked_users': bookmarked_usernames})
        except Product.DoesNotExist:
            return response.Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)


