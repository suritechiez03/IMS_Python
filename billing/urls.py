from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/get_invoice_number$', views.get_invoice_number, name='get_invoice_number'),
    url(r'^api/process_invoice', views.process_invoice, name='process_invoice'),
    url(r'^api/get_invoice_list', views.get_invoice_list, name='get_invoice_list'),
    url(r'^api/fetch_invoice_list_all', views.fetch_invoice_list_all, name='fetch_invoice_list_all'),
    url(r'^api/process_payment', views.process_payment, name='process_payment'),
    url(r'^api/get_invoice_pdf', views.get_invoice_pdf, name='get_invoice_pdf')

]