from django.contrib import admin
from .models import CustomerDetails,CustomerAddress

# Register your models here.

admin.site.register(CustomerDetails)
admin.site.register(CustomerAddress)
