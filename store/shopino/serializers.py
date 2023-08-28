from rest_framework import serializers
from .models import Shop, Product , UserBookmark


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




