from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Shop
        fields = ('id', 'name', 'owner', 'address', 'description', 'followers')

    def validate_address(self, value):
        min_length = 5
        if len(value) < min_length:
            raise serializers.ValidationError('Address has to be more than 5 characters.')
        return value


