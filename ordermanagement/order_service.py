from . import models
import json
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .Serializers import ManageOrderSerializers
import datetime
from django.utils import timezone


class OrderService:
    @transaction.atomic
    def save_order(self, order_data, user):
        try:
            json_data = json.loads(order_data)
            obj_order = models.ManageOrder()
            obj_order.CustomerNumber = json_data["CustomerNumber"]
            if "Comments" in json_data:
                obj_order.Comments = json_data["Comments"]
            if "OrderDate" in json_data:
                obj_order.OrderRaisedDate = json_data["OrderDate"]
            else:
                obj_order.OrderRaisedDate = datetime.date.today()
            obj_order.OrderStatus = 'Order Raised'
            obj_order.EnteredBy = str(user)
            obj_order.save()

            for json_orderdetails in list(json_data["OrderDetails"]):
                obj_orderdetails = models.OrderDetails()
                obj_orderdetails.OrderNumber = obj_order
                if "ProductID" in json_orderdetails:
                    obj_orderdetails.ProductCode = models.Products.objects.get(ProductID=json_orderdetails["ProductID"])
                else:
                    obj_orderdetails.ProductCode = models.Products.objects.get(ProductID=json_orderdetails["ProductCode_id"])
                obj_orderdetails.OrderQty = json_orderdetails["orderQuantity"]
                obj_orderdetails.DispatchQty = 0
                if "UnitPrice" in json_orderdetails:
                    obj_orderdetails.UnitPrice = json_orderdetails["UnitPrice"]
                else:
                    obj_orderdetails.UnitPrice = 0
                if "Discount" in json_orderdetails:
                    obj_orderdetails.Discount = json_orderdetails["Discount"]
                else:
                    obj_orderdetails.Discount = 0
                if "Tax" in json_orderdetails:
                    obj_orderdetails.TaxPerProduct = json_orderdetails["Tax"]
                else:
                    obj_orderdetails.TaxPerProduct = 0
                if "TotalAmount" in json_orderdetails:
                    obj_orderdetails.TotalAmount = json_orderdetails["TotalAmount"]
                else:
                    obj_orderdetails.TotalAmount = 0
                obj_orderdetails.EnteredBy = str(user)
                obj_orderdetails.save()
            return obj_order.GeneratedOrderNumber
        except Exception as err:
            return err

    @login_required
    def get_order_details(self):
        try:
            order_list = []
            for index, item in enumerate(models.ManageOrder.objects.all().values()):
                order_data = item
                order_details_list = []
                #order_data["OrderDetails"] = list(models.OrderDetails.objects.filter(OrderNumber_id=item['OrderNumber']).all().values())
                for orderitem in models.OrderDetails.objects.filter(OrderNumber_id=item['OrderNumber']).all().values():
                    order_item = orderitem
                    order_item["ProductDetails"] = list(models.Products.objects.filter(ProductID=orderitem["ProductCode_id"]).all().values('ProductCode', 'ProductName'))
                    order_details_list.append(order_item)
                order_data["OrderDetails"] = order_details_list
                order_list.append(order_data)
            return order_list
        except Exception as err:
            return err

    @login_required
    def get_order_by_customer(self, CustomerNumber):
        try:
            order_list = []
            orderobj = models.ManageOrder.objects.filter(CustomerNumber=CustomerNumber, OrderStatus="Order Raised").all().values()
            for index, item in enumerate(orderobj):
                order_data = item
                order_details_list = []
                #order_data["OrderDetails"] = list(models.OrderDetails.objects.filter(OrderNumber_id=item['OrderNumber']).all().values())
                for orderitem in models.OrderDetails.objects.filter(OrderNumber_id=item['OrderNumber']).all().values():
                    order_item = orderitem
                    order_item["ProductDetails"] = list(models.Products.objects.filter(ProductID=orderitem["ProductCode_id"]).all().values('ProductCode', 'ProductName'))
                    order_details_list.append(order_item)
                order_data["OrderDetails"] = order_details_list
                order_list.append(order_data)
            return order_list
        except Exception as err:
            return err

    @login_required
    def remove_product(self, product):
        try:
            product = json.loads(product)
            productobj = models.Products.objects.get(ProductCode=product["ProductCode"])
            orderdetails = models.OrderDetails.objects\
                           .get(OrderNumber_id=product["OrderNumber"],
                                   ProductCode_id=productobj)
            orderdetails.delete()
        except Exception as err:
            return err
