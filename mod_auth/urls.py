from django.conf.urls import url, include
from . import views

#Add Django site authentication urls (for login, logout, password management)
urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/api/getSettings', views.get_AppSettings),
    url('accounts/logout', views.logout)
]
