from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact, Order, Category
from django.db.models import Q
from django.http import JsonResponse
from .utils import json_response, paginate, search_filter,sort


def get_all(rq):
    qs = Contact.objects.all().values('id','name','phone','email')
    qs = search_filter(qs,rq,['name','phone','email'])
    qs = sort(qs,rq,['id','name','phone','email'])#новый сортинг
    data = paginate(qs,rq)
    return json_response(data)

def get_one(rq,one):
    c = Contact.objects.get(id = one)
    return json_response({'id': c.id,'name': c.name,'phone':c.phone, 'email':c.email})

@csrf_exempt
def create(rq):
    a = json.loads(rq.body)
    c = Contact.objects.create(name = a['name'],phone = a['phone'],email = a['email'])
    return json_response({'id': c.id,'name': c.name,'phone':c.phone, 'email':c.email},status = 201)
@csrf_exempt
def upd(rq,one):
    c = Contact.objects.get(id = one)
    a = json.loads(rq.body)
    c.name = a.get('name',c.name)
    c.phone =a.get('phone',c.phone)
    c.email = a.get('email',c.email)
    c.save()
    return json_response({'id': c.id,'name': c.name,'phone':c.phone, 'email':c.email})
@csrf_exempt
def delete(rq,one):
    Contact.objects.get(id=one).delete()
    return json_response({'ok':True})


from .models import Order

def orders(rq):
    qs = Order.objects.all().values('id','product_name','price','status','contact_id')

    if contact_id := rq.GET.get('contact_id'):
        qs = qs.filter(contact_id=contact_id)
    if status := rq.GET.get('status'):
        qs = qs.filter(status=status)

    qs = sort(qs,rq,['id','product_name','price','status'])# и тут не забыл сортинг по заказам

    data = paginate(qs,rq)

    return json_response(data
        )


def categories(rq):
    #корневые без родака
    docs = Category.objects.filter(parent_id_isnull = True).values('id','name')
    data = []
    for doc in docs:
        #тут уже вроде дети
        children = Category.object.filter(parent_id = doc['id']).values('id','name')
        doc['children'] = list(children)
        for child in doc['children']:
            #а тут grandcildren
            grandchildren = Category.object.filter(parent_id = child['id']).values('id','name')
            child['children'] = list(grandchildren)
        data.append(doc)
    return   json_response(data)




