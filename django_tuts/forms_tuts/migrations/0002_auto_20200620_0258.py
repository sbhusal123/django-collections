# Generated by Django 3.0.7 on 2020-06-20 02:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_tuts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
