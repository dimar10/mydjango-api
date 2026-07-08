from typing import Dict

from getapp.models import Contact


class ContactService:
    def get_all(self):
        return list(Contact.objects.all().values())

    def get_one(self, id: int):
        c = Contact.objects.get(id=id)
        return {'id': c.id, 'name': c.name, 'phone': c.phone, 'email': c.email}


    def create(self, create_info: Dict[str]):
        c = Contact.objects.create(**create_info)
        return {'id': c.id, 'name': c.name, 'phone': c.phone, 'email': c.email}

    def update(self, id: int, new_model_data: dict) -> Dict[str, str]:
        Contact.objects.filter(id=id).update(**new_model_data)

        return self.get_one(id)

    def delete(self, one):
        Contact.objects.get(id=one).delete()
        return {'ok': True}