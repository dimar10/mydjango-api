from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from functools import wraps
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Contact, Order, Category
from django.db.models import Q
from django.http import JsonResponse
from .utils import json_response, paginate, search_filter,sort,parse_json,,filter_params,api

service = ContactService()

@api
def get_all(rq):
    qs = Contact.objects.all().values('id', 'name', 'phone', 'email')
    qs = search_filter(qs, rq, ['name', 'phone', 'email'])
    qs = sort(qs, rq, ['id', 'name', 'phone', 'email'])
    return json_response(paginate(qs, rq))

@api
def get_one(rq, one):
    return json_response(service.get_one(one))


@api
def create(rq):
    body = parse_json(rq)
    return json_response(service.create(body), status=201)


@api
def upd(rq, one):
    body = parse_json(rq)
    return json_response(service.update(one, body))


@api
def delete(rq, one):
    return json_response(service.delete(one))