import datetime
import json
import os
from pyjasper.jasperpy import JasperPy
from . import models
from django.db import transaction
from ordermanagement.order_service import OrderService

class Transaction_Service:

    def generate_invoicenumber(self):
        last_invoice = models.InvoiceDetails.objects.filter(InvoiceType=1).all().order_by('InvoiceNumber').last()
        if not last_invoice:
            return str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '00000000'
        generated_invoicenumber = int(last_invoice.InvoiceNumber[6:14])
        new_generated_invoicenumber_int = int(generated_invoicenumber) + 1
        new_generated_invoicenumber = str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(
            2) + str(new_generated_invoicenumber_int).zfill(8)
        return new_generated_invoicenumber

    @transaction.atomic
    def process_invoice(self, invoice_data, request):
        invoice_obj = models.InvoiceDetails()
        if invoice_data["InvoiceType"] == "Sales Invoice":
            invoice_obj.InvoiceType = 1
            invoice_obj.InvoiceNumber = self.generate_invoicenumber()
        else:
            invoice_obj.InvoiceType = 2
            invoice_obj.InvoiceNumber = invoice_data["InvoiceNo"]
        invoice_obj.CustomerNumber = invoice_data["Customer"]["CustomerNumber"]
        if "PaymentTerms" in invoice_data:
            invoice_obj.PaymentTerms = invoice_data["PaymentTerms"]
        if "FreightTerms" in invoice_data:
            invoice_obj.FrieghtTerms = invoice_data["FreightTerms"]
        if "DeliveryTerms" in invoice_data:
            invoice_obj.DeliveryTerms = invoice_data["DeliveryTerms"]
        if "Transporter" in invoice_data:
            invoice_obj.Transporter = invoice_data["Transporter"]
        if "TransporterMode" in invoice_data:
            invoice_obj.TransportMode = invoice_data["TransporterMode"]
        if "ESugamaNo" in invoice_data:
            invoice_obj.EsugamaNo = invoice_data["ESugamaNo"]
        if "Destination" in invoice_data:
            invoice_obj.Destination = invoice_data["Destination"]
        if "RepName" in invoice_data:
            invoice_obj.RepName = invoice_data["RepName"]
        if "NoOfPacks" in invoice_data:
            invoice_obj.NoOfPacks = invoice_data["NoOfPacks"]
        if "StateCode" in invoice_data:
            invoice_obj.StateCode = invoice_data["StateCode"]
        if "CrDrNote" in invoice_data:
            invoice_obj.CrDrNote = invoice_data["CrDrNote"]
        if "lrnoAndDate" in invoice_data:
            invoice_obj.LRNoAndDate = invoice_data["lrnoAndDate"]
        if "Grossweight" in invoice_data:
            invoice_obj.GrossWeight = invoice_data["Grossweight"]
        invoice_obj.InvoiceDate = invoice_data["Invoicedate"]
        if "ExpDeliveryDate" in invoice_data:
            invoice_obj.ExpectedDelivery = invoice_data["ExpDeliveryDate"]
        #    if not invoice_data["SelectedOrder"]:
        invoice_obj.GeneratedOrderNumber = str(self.process_order(invoice_data))
        if "TaxAmount" in invoice_data:
            invoice_obj.TaxAmount = invoice_data["TaxAmount"]
        if "RoundOff" in invoice_data:
            invoice_obj.RoundOff = invoice_data["RoundOff"]
        if "FinalAmount" in invoice_data:
            invoice_obj.TotalAmount = invoice_data["FinalAmount"]
            invoice_obj.BalanceAmount = invoice_obj.TotalAmount
        invoice_obj.Status = "Invoice Raised"
        invoice_obj.EnteredBy = str(request.user)
        invoice_obj.save()
        return invoice_obj.InvoiceNumber

    # prepare order data and send to order service
    def process_order(self, invoice_data):
        order_data = invoice_data["ManageOrder"]
        order_data["CustomerNumber"] = invoice_data["Customer"]["CustomerNumber"]
        return OrderService.save_order(self, json.dumps(order_data), "")

    @transaction.atomic
    def process_payment(self, payment_data):
        trans_obj = models.Transaction();
        trans_obj = payment_data[""]
        trans_obj.save()


    def get_invoice_details(self, invoice_no):
        invoice = models.InvoiceDetails.objects.filter(InvoiceNumber=invoice_no).all().values()
        return invoice


    def get_invoice_list(self):
        invoice = models.InvoiceDetails.objects.filter(Status="Invoice Raised").all().values()
        return invoice


    def get_invoice_list_all(self):
        invoice = models.InvoiceDetails.objects.all().values()
        return invoice

    @transaction.atomic
    def process_payment(self, payment_data, request):
        tran_details = models.Transaction()
        tran_details.InvoiceNumber = payment_data["InvoiceNumber"]
        tran_details.TransactionBy = payment_data["PaymentMethod"]
        tran_details.TransactionAmount = payment_data["TransactionAmount"]
        tran_details.TransactionType = payment_data["TransactionType"]
        tran_details.EnteredBy = request.user
        tran_details.CustomerNumber = payment_data["Invoice"][0]["CustomerNumber"]
        if "Description" in payment_data:
            tran_details.Description = payment_data["Description"]
        if "ChequeNo" in payment_data:
            tran_details.ChequeNo = payment_data["ChequeNo"]
        tran_details.save()
        self.update_invoice(payment_data["InvoiceNumber"], payment_data["TransactionAmount"])
        return tran_details


    def update_invoice(self, InvoiceNumber, TransactionAmount):
        invoice_obj = models.InvoiceDetails.objects.get(InvoiceNumber=InvoiceNumber)
        invoice_obj.BalanceAmount = float(invoice_obj.BalanceAmount)-float(TransactionAmount)
        if float(invoice_obj.BalanceAmount) == 0:
            invoice_obj.Status = "Cleared"
        if float(invoice_obj.BalanceAmount) > 0:
            invoice_obj.Status = "Partial Payment"
        invoice_obj.save()
        return

    def get_inoive_pdf(self,InvoiceNumber):
        input_file = os.path.dirname(os.path.abspath(__file__)) + '/Reports/RptFiles/RptInvoicePrint.jrxml'
        output = os.path.dirname(os.path.abspath(__file__)) + '/Reports/OutPutFiles/'+InvoiceNumber
        con = {
            'driver': 'mysql',
            'username': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'imsapp',
            'port': '3306'
        }
        jasper = JasperPy()
        jasper.process(
                input_file,
                output_file=output,
                format_list=["pdf"],
                db_connection=con,
                locale='en_US',
                parameters={'InvoiceNO': str(InvoiceNumber)})
        return output




























