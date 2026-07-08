from typing import Dict
from getapp.models import Category


class CategoryService:
    def get_all(self):
        docs = Category.objects.filter(parent_id__isnull=True).values('id', 'name')
        data = []
        for doc in docs:
            children = Category.objects.filter(parent_id=doc['id']).values('id', 'name')
            doc['children'] = list(children)
            for child in doc['children']:
                grandchildren = Category.objects.filter(parent_id=child['id']).values('id', 'name')
                child['children'] = list(grandchildren)
            data.append(doc)
        return data

    def get_one(self, id: int):
        c = Category.objects.get(id=id)
        return {'id': c.id, 'name': c.name, 'parent_id': c.parent_id}

    def create(self, create_info: Dict[str]):
        c = Category.objects.create(**create_info)
        return {'id': c.id, 'name': c.name, 'parent_id': c.parent_id}

    def update(self, id: int, new_model_data: dict) -> Dict[str, str]:
        Category.objects.filter(id=id).update(**new_model_data)
        return self.get_one(id)

    def delete(self, id: int):
        Category.objects.get(id=id).delete()
        return {'ok': True}