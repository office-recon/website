from django.shortcuts import render
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.

def index(request):
    return render(request, "homepage/index.html")