# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-28 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ordermanagement.models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermanagement', '0003_auto_20180204_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='Tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manageorder',
            name=b'EnteredDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='manageorder',
            name=b'GeneratedOrderNumber',
            field=models.CharField(default=ordermanagement.models.increment_generated_ordernumber, max_length=100, unique=b'True'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name=b'EnteredDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='shippingdetails',
            name=b'EnteredDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]