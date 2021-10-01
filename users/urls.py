from django.urls import path

from users.views import TelegramRegistrationView

app_name = 'users'

urlpatterns = [
    path('register/', TelegramRegistrationView.as_view())
]