from .models import Product, Shop
from .serializers import ShopSerializer, ProductSerializer, BookmarkSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination

from rest_framework import views, viewsets, permissions, status, response


from django.http import Http404
from django.shortcuts import get_object_or_404

from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
        shop = get_object_or_404(Shop, id=shop_id)
        return Product.objects.filter(shop=shop)


class BookmarkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id=None):
        try:
            product = get_object_or_404(Product, pk=id)
            is_bookmarked = product.bookmarked_by.filter(pk=request.user.pk).exists()

            if is_bookmarked:
                product.bookmarked_by.remove(request.user)
                message = 'Product is not bookmarked anymore.'
                return response.Response({'message': message, 'product_id': id})
            else:
                product.bookmarked_by.add(request.user)
                message = 'Product bookmarked successfully.'
                #
                # product.save()
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
