# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-25 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_transaction_transactionby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetails',
            name='NoOfPacks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
