from django.urls import path

from orders.views import OrderListAPIView, OrdersListAPIView, ProcessingListAPIView, ConfirmedListAPIView, \
    PerformingListAPIView, PerformedListAPIView, CanceledListAPIView

app_name = 'order'

urlpatterns = [
    path('', OrderListAPIView.as_view(), name='home'),
    path('orders/', OrdersListAPIView.as_view(), name='all'),
    path('processing/', ProcessingListAPIView.as_view(), name='processing'),
    path('confirmed/', ConfirmedListAPIView.as_view(), name='confirmed'),
    path('performing/', PerformingListAPIView.as_view(), name='performing'),
    path('Performed/', PerformedListAPIView.as_view(), name='performed'),
    path('Canceled/', CanceledListAPIView.as_view(), name='canceled'),
]