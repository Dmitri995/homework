from django.urls import path
from .views import Head_modelView

urlpatterns = [
    path('', Head_modelView.as_view(), name='headphones'),
]