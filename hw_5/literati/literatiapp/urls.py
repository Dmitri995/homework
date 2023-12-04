from django.urls import include, path
from .views import literatiapp


urlpatterns = [
    path('', literatiapp, name='literatiapp'),
]