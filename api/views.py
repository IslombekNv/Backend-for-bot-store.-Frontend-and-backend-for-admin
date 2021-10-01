from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from api.serializers import ServiceModelSerializer, CategoryModelSerializer, OrderModelSerializer, UserModelSerializer
from orders.models import OrderModel
from service.models import ServiceModel, CategoryModel
from users.models import TelegramUserModel


class ServiceListAPIView(ListAPIView):
    serializer_class = ServiceModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        q = self.request.GET.get('q')
        if pk:
            return ServiceModel.objects.filter(category_id=pk)
        elif q:
            return ServiceModel.objects.filter(title__icontains=q)
        else:
            return ServiceModel.objects.none()


class CategoryListAPIView(ListAPIView):
    serializer_class = CategoryModelSerializer
    queryset = CategoryModel.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ServiceModelSerializer
    queryset = ServiceModel.objects.all()


class OrderCreateView(CreateAPIView):
    serializer_class = OrderModelSerializer
    queryset = OrderModel.objects.all()


class UserListAPIView(ListAPIView):
    serializer_class = UserModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return TelegramUserModel.objects.filter(tg_id=pk)
        return TelegramUserModel.objects.all()


class OrderListAPIView(ListAPIView):
    serializer_class = OrderModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return OrderModel.objects.filter(user_id=pk)
        return OrderModel.objects.all()
