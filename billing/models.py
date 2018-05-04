# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes import fields
from django.db import models
from django.utils import timezone

# Create your models here.

class InvoiceDetails(models.Model):
    InvoiceIdentifier = models.BigAutoField(primary_key=True)
    InvoiceNumber = models.CharField(max_length=50, unique=True)
    CustomerNumber = models.CharField(max_length=50)
    GeneratedOrderNumber = models.CharField(max_length=100)
    InvoiceDate = models.DateTimeField(default=None)
    InvoiceType = models.IntegerField(blank=True, null=True)  # 1. Sales 2. Purchase Invoice
    PaymentDueDate = models.DateTimeField(null=True)
    StateCode = models.CharField(max_length=10, blank=True, null=True)
    BranchCode = models.CharField(max_length=10, blank=True, null=True)
    RepName = models.CharField(max_length=255, blank=True, null=True)
    PaymentTerms = models.CharField(max_length=100, blank=True, null=True)
    FrieghtTerms = models.CharField(max_length=100, blank=True, null=True)
    DeliveryTerms = models.CharField(max_length=100, blank=True, null=True)
    Transporter = models.CharField(max_length=100, blank=True, null=True)
    TransportMode = models.CharField(max_length=100, blank=True, null=True)
    EsugamaNo = models.CharField(max_length=100, blank=True, null=True)
    Destination = models.CharField(max_length=100, blank=True, null=True)
    LRNoAndDate = models.CharField(max_length=100, blank=True, null=True)
    ExpectedDelivery = models.DateTimeField(default=None, blank=True, null=True)
    NoOfPacks = models.CharField(max_length=50, blank=True, null=True)
    GrossWeight = models.CharField(max_length=50, blank=True, null=True)
    Status = models.CharField(max_length=50, blank=True)
    RoundOff = models.DecimalField(max_digits=30, decimal_places=4, blank=True, null=True)
    TaxAmount = models.DecimalField(max_digits=30, decimal_places=4, blank=True, null=True)
    TotalAmount = models.DecimalField(max_digits=30, decimal_places=4, blank=True, null=True)
    TransactionDate = models.DateTimeField(default=timezone.now, blank=True, null=True)
    BalanceAmount = models.DecimalField(max_digits=30, decimal_places=4, blank=True, null=True)
    CrDrNote = models.DecimalField(max_digits=30, decimal_places=4, blank=True, null=True)
    CashDisc = models.DecimalField(max_digits=30, decimal_places=4, blank=True, null=True)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=timezone.now)


class Transaction(models.Model):
    TransactionID = models.BigAutoField(primary_key=True)
    InvoiceNumber = models.CharField(max_length=50, blank=True, null=True)
    BranchCode = models.CharField(max_length=10)
    TransactionAmount = models.DecimalField(max_digits=10, decimal_places=4)
    LedgerCode = models.CharField(max_length=50)
    Description = models.CharField(max_length=500)
    TransactionBy = models.CharField(max_length=50)
    TransactionType = models.IntegerField()  # 1. Credit 2. Debit
    CustomerNumber = models.CharField(max_length=50)
    ChequeNo = models.CharField(max_length=50)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=timezone.now)





