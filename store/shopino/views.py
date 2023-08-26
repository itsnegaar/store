from .models import Shop
from .serializers import ShopSerializer
from rest_framework import viewsets
from rest_framework import permissions
# from .filters import ShopFollowersFilter
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Shop
from rest_framework import pagination


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


