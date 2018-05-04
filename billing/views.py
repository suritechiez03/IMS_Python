from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import FileResponse
import json, base64
import datetime
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .transaction_service import Transaction_Service

from . import models
from . import transaction_service
# Create your views here.


@login_required
def index(request):
    return HttpResponse(render(request, 'billing/index.html'))


@login_required
def get_invoice_number(request):
    return JsonResponse(Transaction_Service.generate_invoicenumber(request))


@login_required
def process_invoice(request):
    try:
        tranobj = Transaction_Service()
        invoiceno = tranobj.process_invoice(json.loads(request.body), request)
        return HttpResponse(str(invoiceno), status=200)
    except Exception as err:
        return HttpResponse("Order Processing Failed " + str(err), status=500)

@login_required
def get_invoice_by_number(request):
    try:
        tranobj = Transaction_Service()
        invoice = tranobj.get_invoice_details(json.loads(request.body))
        if not invoice:
            return JsonResponse(invoice)
        else:
            return HttpResponse("Invoice not fount", status=500)
    except Exception as err:
        return HttpResponse("Invoice details not found " + str(err), status=500)


@login_required
def get_invoice_list(request):
    try:
        invoice_list = Transaction_Service.get_invoice_list(request)
        if invoice_list:
            return JsonResponse(list(invoice_list), safe=False)
        else:
            return HttpResponse("No Data ",status=500)
    except Exception as err:
        return HttpResponse("Unable to get invoice details " + str(err), status=500)


@login_required
def fetch_invoice_list_all(request):
    try:
        invoice_list = Transaction_Service.get_invoice_list_all(request)
        if invoice_list:
            return JsonResponse(list(invoice_list), safe=False)
        else:
            return HttpResponse("No Data ",status=500)
    except Exception as err:
        return HttpResponse("Unable to get invoice details " + str(err), status=500)

@login_required
def process_payment(request):
    try:
        tranobj = Transaction_Service()
        invoice = tranobj.process_payment(json.loads(request.body), request)
        if invoice:
            return HttpResponse(" Transaction Successful...!" + str(invoice.TransactionID))
    except Exception as err:
        return HttpResponse("Unable to process payment " + str(err), status=500)

@login_required
def get_invoice_pdf(request):
    try:
        tranobj = Transaction_Service()
        invoice = tranobj.get_inoive_pdf(request.GET.get('InvoiceNumber'))
        if invoice:
            return FileResponse(open(invoice +".pdf", 'rb'), content_type='application/pdf')
    except Exception as err:
        return HttpResponse("Unable to Generate Report " + str(err), status=500)
