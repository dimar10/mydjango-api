
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'contacts'

class Order(models.Model):
    product_name = models.CharField(max_length=200)
    price =  models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=50,default='new')
    created = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE,db_column='contact_id')

    class Meta:
        db_table='orders'
