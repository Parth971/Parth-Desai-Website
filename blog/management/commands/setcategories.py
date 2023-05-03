import json

from django.conf import settings
from django.core.management import BaseCommand

from blog.models import Category


class Command(BaseCommand):
    help = "Add/Update Categories"

    def handle(self, *args, **options):
        action_map = {
            'create': self.create,
            'delete': self.delete,
            'update': self.update,
        }

        with open(settings.BASE_DIR / 'blog/fixtures/categories.json') as f:
            data = json.load(f)

            assert isinstance(data, dict), "Json data is not valid"

            for action, values in data.items():
                func = action_map.get(action)
                if callable(func):
                    func(values)

    @staticmethod
    def create(values):
        Category.objects.bulk_create([Category(name=val) for val in values])

    @staticmethod
    def update(values):
        for old_val, new_val in values.items():
            cat = Category.objects.get(name=old_val)
            cat.name = new_val
            cat.save()

    @staticmethod
    def delete(values):
        Category.objects.filter(name__in=values).delete()
