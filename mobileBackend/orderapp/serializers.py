from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product, Order


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity_in_stock', 'id']


class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # item = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

    # def create(self, validated_data):
    #     return Order.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # instance.email = validated_data.get('email', instance.email)
    #     # instance.content = validated_data.get('content', instance.content)
    #     # instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance

    # def save(self):
    #     email = self.validated_data['email']
    #     message = self.validated_data['message']
    #     send_email(from=email, message=message)
