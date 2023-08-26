import django_filters
from .models import Shop

# class ShopFollowersFilter(django_filters.FilterSet):
#     min_followers = django_filters.NumberFilter(field_name='followers', lookup_expr='gte')
#     max_followers = django_filters.NumberFilter(field_name='followers', lookup_expr='lte')
#     class Meta:
#         model = Shop
#         fields = ['min_followers', 'max_followers']
