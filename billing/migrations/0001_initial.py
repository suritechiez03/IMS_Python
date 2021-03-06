# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-31 07:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceDetails',
            fields=[
                ('InvoiceIdentifier', models.BigAutoField(primary_key=True, serialize=False)),
                ('InvoiceNumber', models.CharField(max_length=50, unique=True)),
                ('CustomerNumber', models.CharField(max_length=50)),
                ('GeneratedOrderNumber', models.CharField(max_length=100)),
                ('InvoiceDate', models.DateTimeField(default=None)),
                ('InvoiceType', models.IntegerField()),
                ('PaymentDueDate', models.DateTimeField(null=True)),
                ('StateCode', models.CharField(max_length=10)),
                ('BranchCode', models.CharField(max_length=10)),
                ('RepName', models.CharField(max_length=255)),
                ('PaymentTerms', models.CharField(max_length=100)),
                ('FrieghtTerms', models.CharField(max_length=100)),
                ('DeliveryTerms', models.CharField(max_length=100)),
                ('Transporter', models.CharField(max_length=100)),
                ('TransportMode', models.CharField(max_length=100)),
                ('EsugamaNo', models.CharField(max_length=100)),
                ('Destination', models.CharField(max_length=100)),
                ('LRNoAndDate', models.CharField(max_length=100)),
                ('ExpectedDelivery', models.DateTimeField(default=None)),
                ('NoOfPacks', models.IntegerField()),
                ('GrossWeight', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
                ('TaxAmount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('TotalAmount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('TransactionDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('BalanceAmount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('EnteredBy', models.CharField(max_length=100)),
                ('EnteredDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('TransactionID', models.BigAutoField(primary_key=True, serialize=False)),
                ('InvoiceNumber', models.CharField(max_length=50)),
                ('BranchCode', models.CharField(max_length=10)),
                ('TransactionAmount', models.DecimalField(decimal_places=4, max_digits=10)),
                ('LedgerCode', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=500)),
                ('TransactionType', models.IntegerField()),
                ('CustomerNumber', models.CharField(max_length=50)),
                ('ChequeNo', models.CharField(max_length=50)),
                ('EnteredBy', models.CharField(max_length=100)),
                ('EnteredDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
