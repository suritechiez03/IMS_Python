from django.http import HttpResponse
from django.shortcuts import render
from mod_auth import models

def index(request):
    # load application settings
    return HttpResponse(render(request, 'base.html'))
