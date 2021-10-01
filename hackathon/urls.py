from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.urls', namespace='service')),
    path('api/', include('api.urls', namespace='api')),
    path('users/', include('users.urls', namespace='users')),
    path('order/', include('orders.urls', namespace='order')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
