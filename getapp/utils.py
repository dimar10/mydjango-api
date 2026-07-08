import json
from django.http import JsonResponse
from django.db.models import Q

from getapp.views import orders


def json_resp(data,status = 200):
    return JsonResponse(
        data,
        safe = False,
        status=status,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
    )

def paginate(qs,rq):

    limit = int(rq.GET.get('limit', 10))
    page = int(rq.GET.get('page', 1))
    s = ((page - 1) * limit)
    total = qs.count()

    return {
    'total': total,
    'page': page,
    'limit': limit,
    'pages': (total + limit - 1) // limit,
    'res': list(qs[s:s + limit])
}


def search_filter(qs,rq,fields):
    if search := rq.GET.get('search'):
        q_objects = Q()
        for field in fields:
            q_objects |= Q(**{f'{field}__icontains':search})
        qs = qs.filter(q_objects)
    return qs

def sort(qs,rq,allow_fields):
    #сортинг по полям с разрешенными филдами
    order = rq.GET.get('order','id')
    field = order.lstrip('-')#убираем минус для проверки
    if field in allow_fields:
        return qs.order_by(order)
    return qs.order_by('id')#по дефолту