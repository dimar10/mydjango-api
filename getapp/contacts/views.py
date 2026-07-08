from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact, Order, Category
from django.db.models import Q
from django.http import JsonResponse
from .utils import json_response, paginate, search_filter,sort

service = ContactService()


def get_all(rq):
    qs = Contact.objects.all().values('id', 'name', 'phone', 'email')
    qs = search_filter(qs, rq, ['name', 'phone', 'email'])
    qs = sort(qs, rq, ['id', 'name', 'phone', 'email'])
    return json_response(paginate(qs, rq))


def get_one(rq, one):
    return json_response(service.get_one(one))


@csrf_exempt
def create(rq):
    body = json.loads(rq.body)
    return json_response(service.create(body), status=201)


@csrf_exempt
def upd(rq, one):
    body = json.loads(rq.body)
    return json_response(service.update(one, body))


@csrf_exempt
def delete(rq, one):
    return json_response(service.delete(one))