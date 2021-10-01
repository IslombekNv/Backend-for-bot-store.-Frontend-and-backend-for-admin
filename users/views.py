from rest_framework.generics import CreateAPIView

from users.models import TelegramUserModel
from users.serializers import TelegramRegistrationSerializer


class TelegramRegistrationView(CreateAPIView):
    serializer_class = TelegramRegistrationSerializer
    queryset = TelegramUserModel.objects.all()