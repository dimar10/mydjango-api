from django.shortcuts import render
from functools import wraps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Contact, Order, Category
from django.db.models import Q
from django.http import JsonResponse
from .utils import json_response, paginate, search_filter,sort,parse_json,,filter_params,api
from .service import CategoryService

service = CategoryService()
@api
def cat_list(rq):
    return json_response(service.get_all())
@api
def cat_get(rq, pk):
    return json_response(service.get_one(pk))

@api
def cat_create(rq):
    body = parse_json(rq)
    return json_response(service.create(body), status=201)

@api
def cat_upd(rq, pk):
    body = parse_json(rq)
    return json_response(service.update(pk, body))

@api
def cat_del(rq, pk):
    return json_response(service.delete(pk))