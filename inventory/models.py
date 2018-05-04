from django.db import models
from django.utils import timezone
# Create your models here.

class ProductCategory(models.Model):
    CategoryID = models.BigAutoField(primary_key=True),
    CategoryName = models.CharField(max_length=250, unique=True)
    Description = models.CharField(max_length=500)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=timezone.now)

class Products(models.Model):
    ProductID = models.BigAutoField(primary_key=True)
    ProductCode = models.CharField(max_length=50, unique=True)
    ProductName = models.CharField(max_length=250, unique=True)
    CategoryCode = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    Description = models.CharField(max_length=1000)
    HsnSacCode = models.CharField(max_length=50, unique=True)
    Units = models.CharField(max_length=50)
    Size = models.CharField(max_length=50)
    MoQ = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Image = models.TextField(blank=True)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=timezone.now)

class StockDetails(models.Model):
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    ProductCode = models.CharField(max_length=50)
    AvailableQty = models.BigIntegerField()
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=timezone.now)


class ProductPrice(models.Model):
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    ProductCode = models.CharField(max_length=50)
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=4)
    Discount = models.DecimalField(max_digits=10, decimal_places=4)
    MarginAllowed = models.DecimalField(max_digits=10, decimal_places=4)
    FinalPrice = models.DecimalField(max_digits=10, decimal_places=4)
    EffectiveDate = models.DateTimeField(default=timezone.now)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=timezone.now)


