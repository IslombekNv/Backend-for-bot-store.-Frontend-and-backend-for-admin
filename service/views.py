from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from service.forms import ServiceModelForm
from service.models import ServiceModel


class ServiceListView(ListView):
    template_name = 'service.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = ServiceModel.objects.order_by('-pk')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['count'] = ServiceModel.objects.count()

        return context


class ServiceDelateView(DeleteView):
    model = ServiceModel
    success_url = '/'


class ServiceUpdateView(UpdateView):
    model = ServiceModel
    form_class = ServiceModelForm
    template_name = 'service.html'
    success_url = '/'


class ServiceCreateView(CreateView):
    template_name = 'users.html'
    form_class = ServiceModelForm
    success_url = '/'