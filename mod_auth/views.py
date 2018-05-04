from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from . import models
# Create your views here.


def get_AppSettings(request):

        for item in models.AppSetting.objects.all().values():
            request.session[item["AppSettingName"]] = item["AppSettingValue"]

        settings = list(models.AppSetting.objects.all().values())
        return JsonResponse(settings, safe=False)


# log out the user
def logout(request):
    logout(request)
