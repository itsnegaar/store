from rest_framework import serializers
from .models import Shop, Product


class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ('id', 'name', 'owner', 'address', 'description', 'followers', 'product_count')

    def validate_address(self, value):
        min_length = 5
        if len(value) < min_length:
            raise serializers.ValidationError('Address has to be more than 5 characters.')
        return value

    def get_product_count(self, obj):
        return obj.product_set.count()


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'owner', 'description', 'shop', 'date', 'is_bookmarked')

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        return obj.bookmarked_by.filter(pk=user.pk).exists()


class BookmarkSerializer(serializers.Serializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ('date_bookmarked')
