from django.urls import include, path
from .views import programmer_day

urlpatterns = [
    path('', programmer_day, name='programmer_day'),
]

