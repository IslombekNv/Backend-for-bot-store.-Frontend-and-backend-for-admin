from rest_framework import serializers

from orders.models import OrderModel
from service.models import ServiceModel, CategoryModel
from users.models import TelegramUserModel


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserModel
        fields = '__all__'