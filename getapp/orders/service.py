from typing import Dict
from getapp.models import Order


class OrderService:
    def get_all(self):
        return list(Order.objects.all().values())

    def get_one(self, id: int):
        o = Order.objects.get(id=id)
        return {
            'id': o.id,
            'product_name': o.product_name,
            'price': str(o.price),
            'status': o.status,
            'contact_id': o.contact_id
        }

    def create(self, create_info: Dict[str]):
        o = Order.objects.create(**create_info)
        return {
            'id': o.id,
            'product_name': o.product_name,
            'price': str(o.price),
            'status': o.status,
            'contact_id': o.contact_id
        }

    def update(self, id: int, new_model_data: dict) -> Dict[str, str]:
        Order.objects.filter(id=id).update(**new_model_data)
        return self.get_one(id)

    def delete(self, id: int):
        Order.objects.get(id=id).delete()
        return {'ok': True}

    from django.db import transaction

    @transaction.atomic()
    def pay(self,order_id,cash):
        """если бабосиков нет - откатик(exception)"""
        order = Order.objects.select_for_update().get(pk = order_id)#блокнет строку

        if cash>order.price:
            raise ValueError('иди работай')

        order.paid = cash
        order.status = 'paid'
        order.save()


        return {
            'order_id':order.pk,
            'price':order.price,
            'paid':order.paid,
            'change':order.change,


        }
