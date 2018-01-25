from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json, base64
import datetime
from django.contrib.auth.decorators import login_required
from django.db import transaction
from . import models
# Create your views here.


@login_required
def index(request):
    return HttpResponse(render(request, 'inventory/index.html'))


@login_required
def get_category_list(request):
    try:
        category = list(models.ProductCategory.objects.all().values())
        return JsonResponse(category, safe=False)
    except Exception as err:
        return HttpResponse(request, "Error while getting category list" + format(err), status=500)

@login_required
def save_category(request):
    try:
        received_json_data = json.loads(request.body)
        obj_productcategory = models.ProductCategory()
        if "CategoryID" in received_json_data and str(received_json_data["CategoryID"]).isdigit():
            obj_productcategory = models.ProductCategory.objects.get(id=received_json_data["CategoryID"])
        obj_productcategory.CategoryName = received_json_data["CategoryName"]
        obj_productcategory.Description = received_json_data["Description"]
        obj_productcategory.EnteredBy = str(request.user)
        obj_productcategory.EnteredDate = datetime.date.today()
        obj_productcategory.save()
        return HttpResponse("Product Category Saved !..")

    except Exception as err:
        return HttpResponse("Error While saving product category" + format(err), status=500)

@login_required
def save_product(request):
    try:
        recevied_json_data = json.loads(request.body)
        obj_product = models.Products()
        if "ProductID" in recevied_json_data and str(recevied_json_data["ProductID"]).isdigit():
            obj_product = models.Products.objects.get(ProductID=recevied_json_data["ProductID"])
        obj_product.ProductCode = recevied_json_data["ProductCode"]
        obj_product.ProductName = recevied_json_data["ProductName"]
        obj_product.CategoryCode = models.ProductCategory.objects.get(id=recevied_json_data["CategoryCode"])
        obj_product.Units = recevied_json_data["Units"]
        obj_product.Size = recevied_json_data["Size"]
        obj_product.MoQ = recevied_json_data["MoQ"]
        obj_product.Color = recevied_json_data["Color"]
        obj_product.HsnSacCode = recevied_json_data["HsnSacCode"]
        obj_product.Description = recevied_json_data["Description"]
        obj_product.Image = recevied_json_data["Image"]
        obj_product.EnteredDate = datetime.date.today()
        obj_product.EnteredBy = str(request.user)
        obj_product.save()
        return HttpResponse("Product Saved !..")
    except Exception as err:
        return HttpResponse("Error while saving product" + format(err), status=500)


@login_required
def get_product_list(request):
    try:
        data = list(models.Products.objects.all().values())
        return JsonResponse(data, safe=False)
    except Exception as err:
        return HttpResponse("Error While Fetching Product List" + format(err))






