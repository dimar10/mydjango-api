from django.urls import path
from . import views

urlpatterns = [
    path('categories/',views.categories)
    path('categories/', views.get_all),
    path('categories/<int:one>/', views.get_one),
    path('categories/create/', views.create),
    path('categories/<int:one>/upd/', views.upd),
    path('categories/<int:one>/del/', views.delete)
]
