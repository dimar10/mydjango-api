from django.urls import path
from . import views

urlpatterns = [
    path('contacts/',views.get_all),
    path('contacts/<int:one>/',views.get_one),
    path('contacts/create/',views.create),
    path('contacts/<int:one>/upd/',views.upd),
    path('contacts/<int:one>/del/',views.delete),

]
