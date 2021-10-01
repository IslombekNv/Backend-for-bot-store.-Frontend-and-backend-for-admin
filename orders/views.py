from django.views.generic import ListView

from orders.models import OrderModel
from users.models import TelegramUserModel


class OrderListAPIView(ListView):
    template_name = 'admin_pages/index.html'
    queryset = OrderModel.objects.order_by('-pk')

    def get_context_data(self, **kwargs):
        context = super(OrderListAPIView, self).get_context_data(**kwargs)
        context['order_count'] = OrderModel.objects.count()
        context['user_count'] = TelegramUserModel.objects.count()
        context['cop_count'] = OrderModel.objects.filter(order='Performed').count()
        context['prog_count'] = OrderModel.objects.filter(order='Performing').count()
        return context


class OrdersListAPIView(ListView):
    template_name = 'admin_pages/order.html'
    queryset = OrderModel.objects.order_by('-pk')


class ProcessingListAPIView(ListView):
    template_name = 'admin_pages/Processing.html'
    queryset = OrderModel.objects.filter(order='').order_by('-pk')


class ConfirmedListAPIView(ListView):
    template_name = 'admin_pages/confirmed.html'
    queryset = OrderModel.objects.filter(order='Confirmed').order_by('-pk')


class PerformingListAPIView(ListView):
    template_name = 'admin_pages/performing.html'
    queryset = OrderModel.objects.filter(order='Performing').order_by('-pk')


class PerformedListAPIView(ListView):
    template_name = 'admin_pages/performed.html'
    queryset = OrderModel.objects.filter(order='Performed').order_by('-pk')


class CanceledListAPIView(ListView):
    template_name = 'admin_pages/canceled.html'
    queryset = OrderModel.objects.filter(order='Canceled').order_by('-pk')