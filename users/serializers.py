from rest_framework import serializers

from users.models import TelegramUserModel


class TelegramRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUserModel
        fields = '__all__'