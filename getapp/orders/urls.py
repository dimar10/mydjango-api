from django.urls import path
from . import views

urlpatterns = [
    path('orders/',views.orders),
    path('orders/', views.get_all),
    path('orders/<int:one>/', views.get_one),
    path('orders/create/', views.create),
    path('orders/<int:one>/upd/', views.upd),
    path('orders/<int:one>/del/', views.delete)
]
