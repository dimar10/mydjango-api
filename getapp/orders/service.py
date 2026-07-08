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