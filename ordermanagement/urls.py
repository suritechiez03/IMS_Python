from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/save_order$',views.save_order, name="save_order"),
    url(r'^api/get_order_list$', views.get_order_list, name="get_order_list"),
    url(r'^api/get_order_details/(?P<order_number>[0-9]+)/$', views.get_order_list_by_number, name="get_order_details"),
    url(r'^api/remove_product', views.remove_product, name="remove_product"),
    url(r'^api/get_order_by_customer$', views.get_order_by_customer, name="get_order_by_customer"),

]