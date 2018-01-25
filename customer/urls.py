from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/save_customer_info$', views.save_customer_info, name='save_customer_info'),
    url(r'^api/get_customer_list', views.get_customer_list, name='get_customer_list')

]