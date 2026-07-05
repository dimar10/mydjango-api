from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_all),
    path('create/',views.create),
    path('<int:one>/',views.get_one),
    path('<int:one>/upd/',views.upd),
    path('<int:one>/del/',views.delete),]