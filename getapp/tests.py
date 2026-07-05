from django.test import TestCase,Client
import json
from .models import Contact
class ContactTests(TestCase):
    # todo увеличить число проверок,
    #  непонятно что может придти в гет, непонятно что update сработал и тд
    def setUp(self):
        self.c = Client()
        self.contact = Contact.objects.create(name='Test', phone='+7', email='t@mail.ru')

    def test_get_all(self):
        r = self.c.get('/api/contacts/')
        self.assertEqual(r.status_code, 200)

    def test_get_one(self):
        r = self.c.get(f'/api/contacts/{self.contact.id}/')
        self.assertEqual(r.status_code, 200)

    def test_create(self):
        r = self.c.post('/api/contacts/create/', {'name': 'A', 'phone': '+8', 'email': 'a@mail.ru'}, content_type='application/json')
        self.assertEqual(r.status_code, 201)

    def test_update(self):
        r = self.c.put(f'/api/contacts/{self.contact.id}/upd/', {'name': 'B'}, content_type='application/json')
        self.assertEqual(r.status_code, 200)

    def test_delete(self):
        r = self.c.delete(f'/api/contacts/{self.contact.id}/del/')
        self.assertEqual(r.status_code, 200)
