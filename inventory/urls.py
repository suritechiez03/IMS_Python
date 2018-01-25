from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/get_category_list', views.get_category_list, name='get_category_list'),
    url(r'^api/save_category', views.save_category, name='save_category'),
    url(r'^api/save_product', views.save_product, name='save_product'),
    url(r'^api/get_product_list', views.get_product_list, name='get_product_list')
]