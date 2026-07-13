
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return self.name

class Order(models.Model):
    product_name = models.CharField(max_length=200)
    price =  models.DecimalField(max_digits=10,decimal_places=2)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=50,default='new')
    created = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE,db_column='contact_id')

    class Meta:
        db_table='orders'

    def __str__(self):
        return self.name

    @property
    def change(self):
        """Сдача за переплату"""
        if self.paid > self.price:
            return self.paid - self.price
        return 0

    @property
    def is_paid(self):
        """Хватило денег или нет."""
        return self.paid >= self.price


class category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null = True,blank = True,db_column='parent_id')
    #ну получилась моделька с иерархией ссылающаяся на саму себя
    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

