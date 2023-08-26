from rest_framework import serializers
from .models import Shop

# class ShopSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shop
#         fields = '__all__'

class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shop
        fields = ('id', 'shop_name', 'owner', 'shop_address', 'shop_description')


