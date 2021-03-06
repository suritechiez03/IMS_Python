from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.decorators import login_required
from django.db import transaction
from . import models
# Create your views here.

@login_required
def index(request):
    return HttpResponse(render(request, 'customer/index.html'))

@login_required
@transaction.atomic
def save_customer_info(request):
    try:
        received_json_data = json.loads(request.body)

        obj_customer = models.CustomerDetails()
        if "CustomerID" in received_json_data and str(received_json_data["CustomerID"]).isdigit():
            obj_customer = models.CustomerDetails.objects.get(CustomerID=received_json_data["CustomerID"])
        obj_customer.CustomerName = received_json_data["CustomerName"]
        obj_customer.CustomerType = received_json_data["CustomerType"]
        if "TinNumber" in received_json_data:
            obj_customer.TinNumber = received_json_data["TinNumber"]
        if "CstNumber" in received_json_data:
            obj_customer.CstNumber = received_json_data["CstNumber"]
        if "GstNumber" in received_json_data:
            obj_customer.GstNumber = received_json_data["GstNumber"]
        if "PanNumber" in received_json_data:
            obj_customer.PanNumber = received_json_data["PanNumber"]
        if "ReferenceCustomerNumber" in received_json_data:
            obj_customer.ReferenceCustomerNumber = received_json_data["ReferenceCustomerNumber"]
        obj_customer.EnteredBy = str(request.user)
        obj_customer.EnteredDate = datetime.date.today()
        obj_customer.Status = 1
        obj_customer.save()

        obj_customer_address = models.CustomerAddress()
        if "Address_Id" in received_json_data and str(received_json_data["Address_Id"]).isdigit():
            obj_customer_address = models.CustomerAddress.objects.get(id=received_json_data["Address_Id"])
        obj_customer_address.CustomerID = obj_customer
        if "CompanyEmail" in received_json_data:
            obj_customer_address.Email = received_json_data["CompanyEmail"]
        if "PhoneNumber" in received_json_data:
            obj_customer_address.PhoneNumber = received_json_data["PhoneNumber"]
        if "CompanyAddress" in received_json_data:
            obj_customer_address.Address = received_json_data["CompanyAddress"]
        if "CompanyWebsite" in received_json_data:
            obj_customer_address.WebSite = received_json_data["CompanyWebsite"]

        obj_customer_address.EnteredBy = str(request.user)
        obj_customer_address.EnteredDate = datetime.date.today()
        obj_customer_address.save()
        # send the latest customer information
        return HttpResponse("Customer information saved !..." + obj_customer.CustomerNumber)
    except Exception as err:
        print(format(err))
        return HttpResponse("Error while Saving Customer Information" + format(err), status=500)

# get the list of customer
@login_required
def get_customer_list(request):
    try:
        data = models.CustomerDetails.objects.all().values(
            'CustomerID',
            'CustomerNumber',
            'CustomerName',
            'CustomerType',
            'TinNumber',
            'CstNumber',
            'GstNumber',
            'PanNumber',
            'ReferenceCustomerNumber',
            'customeraddress__id',
            'customeraddress__Address',
            'customeraddress__Email',
            'customeraddress__WebSite',
            'customeraddress__PhoneNumber'
        )
        return JsonResponse(list(data), safe=False)
    except Exception as err:
        print(format(err))
        return HttpResponse(request, "Error while fetching customer list"+format(err), status=500)

@login_required
def get_customer_list_byType(request):
    try:
        customer_list = models.CustomerDetails.objects.filter(CustomerType=request.body).all().values()
        if customer_list:
            for customer in customer_list:
                customer_address = models.CustomerAddress.objects.filter(id=customer.CustomerID).all().values()
                customer_list["CustomerID"]
    except Exception as err:
        return HttpResponse(request, "Error while fetching customer details" + format(err), status=500)






