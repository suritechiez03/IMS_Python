# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-08 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetails',
            name='ExpectedDelivery',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
