from django.db import models
from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
    # TODO: Добавьте требуемые поля


