import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            item = Phone(name=phone['name'], image=phone['image'], price=phone['price'], release_date=phone['release_date'], lte_exist=phone['lte_exists'])
            item.save()
        #     # TODO: Добавьте сохранение модели

# name = models.CharField(max_length=50)
#     price = models.FloatField()
#     image = models.ImageField()
#     release_date = models.DateField()
#     lte_exist = models.BooleanField()
#     slug = models.SlugField(m