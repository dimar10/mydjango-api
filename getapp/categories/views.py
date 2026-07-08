from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact, Order, Category
from django.db.models import Q
from django.http import JsonResponse
from .utils import json_response, paginate, search_filter,sort
from .service import CategoryService

service = CategoryService()

def cat_list(rq):
    return json_response(service.get_all())

def cat_get(rq, pk):
    return json_response(service.get_one(pk))

@csrf_exempt
def cat_create(rq):
    body = json.loads(rq.body)
    return json_response(service.create(body), status=201)

@csrf_exempt
def cat_upd(rq, pk):
    body = json.loads(rq.body)
    return json_response(service.update(pk, body))

@csrf_exempt
def cat_del(rq, pk):
    return json_response(service.delete(pk))