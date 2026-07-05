from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact
from django.db.models import Q

def get_all(rq):
    data = list(Contact.objects.all().values())
    if search := rq.GET.get('search'):
        data  = data.filter(
            Q(name_icontains = search) or Q(phone_icontains = search) or Q(email_icontains = search)
        )

        limit = int(rq.GET.get('limit',10))
        page = int(rq.GET.get('page',1))
        s = ((page -1) * limit)
        total = data.count()

        date = list(data[s:s + limit])


    return JsonResponse({'total': total,'page':page,'limit':limit,'pages': (total + limit-1)//limit,'res':date
    }, safe=False,json_dumps_params={'ensure_ascii': False,'indent':2})

def get_one(rq,one):
    c = Contact.objects.get(id = one)
    return JsonResponse({'id': c.id,'name': c.name,'phone':c.phone, 'email':c.email},json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def create(rq):
    a = json.loads(rq.body)
    c = Contact.objects.create(name = a['name'],phone = a['phone'],email = a['email'])
    return JsonResponse({'id': c.id,'name': c.name,'phone':c.phone, 'email':c.email},json_dumps_params={'ensure_ascii': False})
@csrf_exempt
def upd(rq,one):
    c = Contact.objects.get(id = one)
    a = json.loads(rq.body)
    c.name = a.get('name',c.name)
    c.phone =a.get('phone',c.phone)
    c.email = a.get('email',c.email)
    c.save()
    return JsonResponse({'id': c.id,'name': c.name,'phone':c.phone, 'email':c.email},json_dumps_params={'ensure_ascii': False})
@csrf_exempt
def delete(rq,one):
    Contact.objects.get(id=one).delete()
    return JsonResponse({'ok':True})


from .models import Order

def orders(rq):
    qs = Order.objects.all().values('id','product_name','price','status','contact_id')

    if contact_id := rq.GET.get('contact_id'):
        qs = qs.filter(contact_id=contact_id)
    if status := rq.GET.get('status'):
        qs = qs.filter(status=status)

    limit = int(rq.GET.get('limit', 10))
    page = int(rq.GET.get('page', 1))
    s = ((page - 1) * limit)
    total = qs.count()



    order = rq.GET.get('order','id')
    qs =  qs.order_by(order)
    date = list(qs[s:s + limit])

    return JsonResponse({'total': total,'page':page,'limit':limit,'pages': (total + limit-1)//limit,'res':date}
        ,safe=False,json_dumps_params={'ensure_ascii': False, 'indent': 2})



