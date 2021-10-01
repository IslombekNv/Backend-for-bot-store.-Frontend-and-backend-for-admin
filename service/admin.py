from django.contrib import admin

from service.models import ServiceModel, CategoryModel


@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_filter = ['created']
    list_display = ['title']
    search_fields = ['title']


@admin.register(CategoryModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_filter = ['created']
    list_display = ['title']
    search_fields = ['title']
