from django import forms

from service.models import ServiceModel


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = ServiceModel
        exclude = ['created']
