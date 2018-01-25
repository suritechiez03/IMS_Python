from django.db import models

# Create your models here.


class AppSetting(models.Model):
    AppSettingName = models.CharField(max_length=100, unique=True, primary_key=True)
    AppSettingValue = models.CharField(max_length=100)
