from django.urls import path

from service.views import ServiceListView, ServiceDelateView, ServiceUpdateView, ServiceCreateView

app_name = 'service'

urlpatterns = [
    path('', ServiceListView.as_view(), name='list'),
    path('delate/<int:pk>/', ServiceDelateView.as_view(), name='delate'),
    path('update/<int:pk>/', ServiceUpdateView.as_view(), name='update'),
    path('create/', ServiceCreateView.as_view(), name='create'),
]