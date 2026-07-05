from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact

# todo я наебнул тебе въюху, теперь её тут вообще не будет
# todo надо разнести всё как в folder /contacts


from .models import Order

def orders(rq):
    qs = Order.objects.all().values('id','product_name','price','status','contact_id')

    if contact_id := rq.GET.get('contact_id'):
        qs = qs.filter(contact_id=contact_id)
    if status := rq.GET.get('status'):
        qs = qs.filter(status=status)

    order = rq.GET.get('order','id')
    qs =  qs.order_by(order)

    return JsonResponse(list(qs),safe=False,json_dumps_params={'ensure_ascii': False, 'indent': 2})



