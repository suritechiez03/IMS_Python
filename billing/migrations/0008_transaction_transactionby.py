# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-24 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_auto_20180411_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='TransactionBy',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
