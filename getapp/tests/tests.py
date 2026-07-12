from django.test import TestCase,Client
import json
from getapp.models import Order, Contact, category


class ContactTests(TestCase):
    def test_create_contact(self):
        contact = Contact.objects.create(
            name = 'Alex',
            phone = '+79999999999',
            email  = 'alex@test.com',
        )
        '''закреатили контакт и чекаем в бд'''
        self.assertEqual(Contact.objects.count(),1)#чек в базе на 1 контакт
        '''чек на правильную запись'''
        self.assertEqual(contact.name,'Alex')
        self.assertEqual(contact.phone, '+79999999999')
        self.assertEqual(contact.email, 'alex@test.com')
        '''ищем контакт по эмэйлу'''
    def test_find_email(self):
        Contact.objects.create(name = 'Joe',phone = '123',email = 'joe@mail.ru')

        found = Contact.objects.get(email ='joe@mail.ru')
        self.assertEqual(found.name, 'Joe')
    def test_delete_contact(self):
        contact = Contact.objects.create(name='Петр', phone='222', email='petr@mail.com')
        contact.delete()

        self.assertEqual(Contact.objects.count(),0)

class OrderTests(TestCase):
    def test_create_order(self):
        order = Order.objects.create(
            product_name='iPhone 15',
            price=999.99,
            status='new',
        )#создаем заказ и проверяем поля

        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(order.product_name, 'iPhone 17')
        self.assertEqual(order.status, 'new')

    def test_filter_status(self):
        Order.objects.create(product_name='A', price=100, status='new')
        Order.objects.create(product_name='B', price=200, status='paid')
        #чекаем фильтр

        paid_orders = Order.objects.filter(status='paid')

        self.assertEqual(paid_orders.count(),1)
        self.assertEqual(paid_orders.first().product_name,'B')

    def test_filter_contact(self):
        contact = Contact.objects.create(name='Клиент', phone='000', email='c@mail.com')
        Order.objects.create(product_name='Заказ 1', price=50, status='new', contact=contact)
        found = Order.objects.filter(contact = contact)
        self.assertEqual(found.count(),1)
        self.assertEqual(found.first().product_name,'Заказ 1')

    def test_delete_order(self):
        order = Order.objects.create(product_name = 'удалить',price = 1,status = 'new')
        order.delete()

        self.assertEqual(Order.objects.count(),0)

class CategoryTest(TestCase):
    def test_create_cat(self):
        cat =  category.objects.create(name='Телефоны', type='phones')

        self.assertEqual(category.objects.count(), 1)
        self.assertEqual(cat.name,'Телефоны')
        self.assertEqual(cat.type,'phones')

    def test_upd_catname(self):
        cat  = category.objects.create(name = 'Старые',type = 'old')#меняем имя и сохранияем
        cat.name = 'Новые'
        cat.save()
        #достаем копию из базы
        copy = category.objects.get(pk = cat.pk)
        self.assertEqual(copy.name,'Новые')
    def test_delete_cat(self):
        cat = category.objects.create(name = 'удаление',type = 'del')
        cat.delete()

        self.assertEqual(category.objects.count(),0)

