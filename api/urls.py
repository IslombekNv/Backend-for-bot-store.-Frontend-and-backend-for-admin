from django.urls import path

from api.views import ServiceListAPIView, CategoryListAPIView, ProductRetrieveAPIView, OrderCreateView, UserListAPIView, \
    OrderListAPIView

app_name = 'api'

urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', ServiceListAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('order/', OrderCreateView.as_view()),
    path('user/<int:pk>/', UserListAPIView.as_view()),
    path('order/<int:pk>/', OrderListAPIView.as_view()),
]
