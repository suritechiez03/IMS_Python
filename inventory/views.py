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
@transaction.atomic
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
@transaction.atomic
def save_product(request):
    try:
        recevied_json_data = json.loads(request.body)
        obj_product = models.Products()
        if "ProductID" in recevied_json_data and str(recevied_json_data["ProductID"]).isdigit():
            obj_product = models.Products.objects.get(ProductID=recevied_json_data["ProductID"])
        obj_product.ProductCode = recevied_json_data["ProductCode"]
        obj_product.ProductName = recevied_json_data["ProductName"]
        obj_product.CategoryCode = models.ProductCategory.objects.get(id=recevied_json_data["CategoryID"])
        if "Units" in recevied_json_data:
            obj_product.Units = recevied_json_data["Units"]
        if "Size" in recevied_json_data:
            obj_product.Size = recevied_json_data["Size"]
        if "MoQ" in recevied_json_data:
            obj_product.MoQ = recevied_json_data["MoQ"]
        if "Color" in recevied_json_data:
            obj_product.Color = recevied_json_data["Color"]
        if "HsnSacCode" in recevied_json_data:
            obj_product.HsnSacCode = recevied_json_data["HsnSacCode"]
        if "Description" in recevied_json_data:
            obj_product.Description = recevied_json_data["Description"]
        if "Image" in recevied_json_data:
            obj_product.Image = recevied_json_data["Image"]
        obj_product.EnteredDate = datetime.date.today()
        obj_product.EnteredBy = str(request.user)
        obj_product.save()
        create_stock_details(request, obj_product, recevied_json_data)
        # if "ProductID" not in recevied_json_data:
        #    create_stock_details(request, obj_product, recevied_json_data)

        return HttpResponse("Product Saved !..")
    except Exception as err:
        return HttpResponse("Error while saving product" + format(err), status=500)


@transaction.atomic
def create_stock_details(request, product, json_data):
    try:
        obj_stockdetails = models.StockDetails()
        if "ProductID" in json_data:
            obj_stockdetails = models.StockDetails.objects.get(ProductID_id=product.ProductID)
        obj_stockdetails.ProductID = product
        obj_stockdetails.ProductCode = product.ProductCode
        if "StockQty" in json_data:
            if "ProductID" not in json_data:
               obj_stockdetails.AvailableQty = int(json_data["StockQty"])
            else:
                obj_stockdetails.AvailableQty = int(obj_stockdetails.AvailableQty) + int(json_data["StockQty"])
        obj_stockdetails.EnteredBy = str(request.user)
        obj_stockdetails.save()
    except Exception as err:
        return HttpResponse("Error while saving product" + format(err), status=500)



@login_required
def get_product_list(request):
    try:
        data = list(models.Products.objects.all().values())
        return JsonResponse(data, safe=False)
    except Exception as err:
        return HttpResponse("Error While Fetching Product List" + format(err))






