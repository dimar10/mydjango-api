import json

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

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

def parse_json(rq):
    """ запарсим тело запроса или выкинем 400
    пропустит пустышки"""
    try:
        return json.loads(rq.body) if rq.body else {}
    except json.JSONDecodeError('error  json')

def json_response(data=None, status=200, errors=None):
    '''так чисто для единообразного вывода как для errors так и для data'''
    payload = {"data": data} if errors is None else {"errors": errors}
    return JsonResponse(payload, status=status, safe=False)
#ocoбого смысла в нем нем встроенный тоже норм

def filter_params(qs,params,mapping:dict):
    """ мапинг на query params : model field"""
    for query_key,field_path in mapping.items():
        value = params.get(query_key)
        if value not in (None,'',[]):
            qs = qs.filter(**{field_path : value})
    return qs

def api(fn):
    """обертка на все это csrf  + json errors и exceptions"""
    @wraps(fn)
    @csrf_exempt
    def wrapper(rq,*args,**kwargs):
        try:
            return fn(rq,*args,**kwargs)
        except ObjectDoesNotExist as e:
            return json_response(errors=str(e),status=404)
        except ValidationError as e:
            return json_response(errors=str(e),status=400)
        except Exception as e:
            #лог e
            return json_response(errors='error',status=500)
    return wrapper








