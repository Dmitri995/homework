from django.urls import include, path
from .views import cityinfo


urlpatterns = [
    path('', cityinfo, name='cityinfo'),
]