from django.urls import path, include
from . import views

urlpatterns = [

    path('contacts/', include('getapp.contacts.urls')),
    path('orders/', include('getapp.orders.urls')),
]
