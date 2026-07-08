from .models import Order
from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact, Order, Category
from django.db.models import Q
from django.http import JsonResponse
from .utils import json_response, paginate, search_filter,sort
from .service import OrderService

service = OrderService()

def order_list(rq):
    qs = Order.objects.all().values()
    if contact_id := rq.GET.get('contact_id'):
        qs = qs.filter(contact_id=contact_id)
    if status := rq.GET.get('status'):
        qs = qs.filter(status=status)
    qs = sort(qs, rq, ['id', 'product_name', 'price', 'status'])
    return json_response(paginate(qs, rq))

def order_get(rq, pk):
    return json_response(service.get_one(pk))

@csrf_exempt
def order_create(rq):
    body = json.loads(rq.body)
    return json_response(service.create(body), status=201)

@csrf_exempt
def order_upd(rq, pk):
    body = json.loads(rq.body)
    return json_response(service.update(pk, body))

@csrf_exempt
def order_del(rq, pk):
    return json_response(service.delete(pk))
