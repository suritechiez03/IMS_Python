from django.db import models
import datetime

# Create your models here.
def increment_customernumber():
    last_customernumber = CustomerDetails.objects.all().order_by('CustomerID').last()
    if not last_customernumber:
        return 'CUST' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
    customernumber = int(last_customernumber.CustomerNumber[10:14])
    new_customernumber_int = int(customernumber) + 1
    new_customernumber = 'CUST' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(new_customernumber_int).zfill(4)
    return new_customernumber


class CustomerDetails(models.Model):
    CustomerID = models.BigAutoField(primary_key=True)
    CustomerNumber = models.CharField(max_length=50, default=increment_customernumber, editable=False)
    CustomerName = models.CharField(max_length=500)
    CustomerType = models.CharField(max_length=50)
    TinNumber = models.CharField(max_length=100)
    CstNumber = models.CharField(max_length=100)
    GstNumber = models.CharField(max_length=100)
    PanNumber = models.CharField(max_length=50)
    ReferenceCustomerNumber = models.CharField(max_length=50, default="NULL")
    Status = models.IntegerField(1)
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=True)


class CustomerAddress(models.Model):
    CustomerID = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    Address = models.CharField(max_length=1000)
    WebSite = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    PhoneNumber = models.CharField(max_length=50, default="NULL")
    EnteredBy = models.CharField(max_length=100)
    EnteredDate = models.DateTimeField(default=True)




