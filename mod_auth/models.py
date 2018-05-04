from django.db import models
from django.utils import timezone
# Create your models here.


class AppSetting(models.Model):
    AppSettingName = models.CharField(max_length=100, unique=True, primary_key=True)
    AppSettingValue = models.CharField(max_length=100)

class BranchDetails(models.Model):
    BranchID = models.BigAutoField(primary_key=True)
    BranchCode = models.CharField(max_length=10)
    BranchName = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    IsMainBranch = models.IntegerField()
    OpenDate = models.DateTimeField(default=None)
    SalesGL = models.CharField(max_length=50)
    PurchaseGL = models.CharField(max_length=50)
    MiscGL = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=100,default=None)
    Email = models.CharField(max_length=100,default=None)
    GSTNo = models.CharField(max_length=100,default=None)

class BrachUserDetails(models.Model):
    BrachCode = models.CharField(max_length=50, null=True)
    UserName = models.CharField(max_length=500)



