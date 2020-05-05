from django.contrib.auth.models import User
from rest_framework import serializers

from product.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProductSerializer(serializers.ModelSerializer):
    create_by = UserSerializer()
    class Meta:
        model = Product
        fields = ['create_by', 'name', 'content', 'image']
        depth = 1