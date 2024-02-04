from django.urls import path
from .views import restaurant_list, restaurant_delete, restaurant_edit, restaurant_search
from django.conf import settings

urlpatterns = [
    path('restaurant_list', restaurant_list, name='restaurant_list'),
    path('restaurant_confirm_delete/',restaurant_delete, name='restaurant_confirm_delete'),
    path('restaurant_edit/', restaurant_edit, name='restaurant_edit'),
    path('restaurant_search/', restaurant_search, name='restaurant_search'),
]