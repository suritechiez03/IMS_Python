from django.db import models
from django.utils import timezone
from inventory.models import Products

# Create your models here.
class ManageOrder(models.Model):
    OrderNumber = models.BigAutoField(primary_key = "True")
    GeneratedOrderNumber = models.CharField(max_length=100,unique= "True",default=self.increment_generated_ordernumber)
    OrderRaisedDate = models.DateTimeField()
    OrderFor = models.CharField(max_length = 50)
    CustomerNumber = models.CharField(max_length = 50)
    OrderStatus = models.CharField(max_length = 50)
    Comments = models.CharField(max_length=250)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateField(default=timezone.now())

    def increment_generated_ordernumber():
        last_order = ManageOrder.objects.all().order_by('OrderNumber').last()
        if not last_order:
            return str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '00000000'
        generated_ordernumber = int(last_order.GeneratedOrderNumber[6:14])
        new_generated_ordernumber_int = int(generated_ordernumber) + 1
        new_generated_ordernumber = str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(new_generated_ordernumber_int).zfill(8)
        return new_generated_ordernumber

class ShippingDetails(models.Model):
    ShippingID = models.BigAutoField(primary_key = "True")
    Address = models.CharField(max_length = 500)
    PinCode = models.IntegerField()
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateField(default=timezone.now())

class OrderDetails(models.Model):
    OrderNumber = models.ForeignKey(ManageOrder, on_delete=models.CASCADE)
    ProductCode = models.ForeignKey(Products,on_delete=models.CASCADE)
    OrderQty = models.BigIntegerField()
    DispatchQty = models.BigIntegerField()
    UnitPrice = models.DecimalField(max_digits=15,decimal_places=4)
    Discount = models.DecimalField(max_digits=5,decimal_places=2)
    TaxPerProduct = models.DecimalField(max_digits=15,decimal_places=4)
    TotalAmount = models.DecimalField(max_digits=15,decimal_places=4)
    Comments = models.CharField(max_length=250)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateField(default=timezone.now())
