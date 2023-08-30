from rest_framework import serializers
from .models import Shop, Product , UserBookmark
from django.core.cache import cache



class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shop
        fields = ('id', 'name', 'owner', 'address', 'description', 'followers', 'product_count')

    def validate_address(self, value):
        min_length = 5
        if len(value) < min_length:
            raise serializers.ValidationError('Address has to be more than 5 characters.')
        return value

    # def get_product_count(self, obj):
    #     return obj.product_set.count()

    # def get_product_count(self, obj):
    #     cache_key = f'product_count_{obj.id}'
    #     cached_product_count = cache.get(cache_key)
    #
    #     if cached_product_count is None:
    #         product_count = obj.product_set.count()
    #         cache.set(cache_key, product_count, timeout=60 * 15)  # Cache for 15 minutes
    #         return product_count
    #
    #     return cached_product_count


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_bookmarked = serializers.SerializerMethodField()
    date_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'owner', 'description', 'shop', 'date', 'is_bookmarked', 'date_bookmarked')

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        return obj.bookmarked_by.filter(pk=user.pk).exists()

    def get_date_bookmarked(self, obj):
        user = self.context['request'].user

        if user.is_authenticated:
            user_bookmark = UserBookmark.objects.filter(user=user, product=obj).first()
            if user_bookmark:
                return user_bookmark.date_bookmarked

        return None