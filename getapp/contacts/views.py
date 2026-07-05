
# TODO ДОДЕЛАЙ VIEWS.PY ЧТОБЫ ЗАРАБОТАЛО
#  (СЕРВИС ГОТОВЫЙ, НАДО ЛИШЬ ПРАВИЛЬНО ВЫЗВАТЬ)
def get_all(rq):
    data = list(Contact.objects.all().values())
    return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii': False,'indent':2})

def get_one(rq,one):
    c = Contact.objects.get(id = one)
    return JsonResponse({'id': c.id,'name': c.name,'phone':c.phone, 'email':c.email},json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def create(rq):
    a = json.loads(rq.body)
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