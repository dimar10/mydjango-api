from .models import Order
from django.shortcuts import render
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from functools import wraps
from .models import Contact, Order, Category
from django.db.models import Q
from django.http import JsonResponse
from .utils import json_response, paginate, search_filter,sort,parse_json,,filter_params,api
from .service import OrderService

service = OrderService()

def order_list(rq):
    qs = Order.objects.all()
    """ну убрал я эту цепочку if GET.get()"""
    qs = filter_params(qs,rq.GET,{'contact_id':'contact_id','status':'status'})
    qs = sort(qs, rq, ['id', 'product_name', 'price', 'status'])
    return json_response(paginate(qs, rq))
@api
def order_get(rq, pk):
    return json_response(service.get_one(pk))

@api
def order_create(rq):
    body = json.loads(rq.body)
    return json_response(service.create(body), status=201)

@api
def order_upd(rq, pk):
    body = json.loads(rq.body)
    return json_response(service.update(pk, body))

@api
def order_del(rq, pk):
    return json_response(service.delete(pk))
