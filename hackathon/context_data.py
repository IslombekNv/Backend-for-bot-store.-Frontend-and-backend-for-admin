from orders.models import OrderModel


def get_order(request):
    return {
        'contacts': OrderModel.objects.order_by('-pk')
    }