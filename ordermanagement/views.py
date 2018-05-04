from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
from .order_service import OrderService


# Create your views here.


@login_required
def index(request):
    return HttpResponse(render(request, 'manageorder/index.html'))


@login_required
def save_order(request):
    try:
        OrderService.save_order(request, request.body, request.user)
        return HttpResponse("Order Saved!..")
    except Exception as err:
        return HttpResponse("Order Processing Failed " + str(err), status=500)


@login_required
def get_order_list(request):
    try:
        return JsonResponse(list(OrderService.get_order_details(request)), safe=False)
    except Exception as err:
        return HttpResponse("Order Processing Failed " + str(err), status=500)


@login_required
def get_order_by_customer(request):
    try:
        json_data = json.loads(request.body)
        return JsonResponse(list(OrderService.get_order_by_customer(request, json_data["CustomerNumber"])), safe=False)
    except Exception as err:
        return HttpResponse("Order Processing Failed " + str(err), status=500)


@login_required
def get_order_list_by_number(request, order_number):
    try:
        return JsonResponse(list(OrderService.get_order_details_by_number(request, order_number)), safe=False)
    except Exception as err:
        return HttpResponse("Order Processing Failed " + str(err), status=500)


@login_required
def remove_product(request):
    try:
        OrderService.remove_product(request, request.body)
        return JsonResponse("Product has been removed", safe=False)
    except Exception as err:
        return HttpResponse("Unable to remove Product" + str(err), status=500)




