# Generated by Django 4.2.7 on 2023-12-03 14:56

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('release_date', models.DateField()),
                ('lte_exist', models.BooleanField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
    ]
