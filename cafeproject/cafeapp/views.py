import re
from urllib import request
from django.shortcuts import render

# Create your views here.
def home(reqeust):
    return render(reqeust, 'index.html')


def detail(request):
    return render(request, 'portfolio-details.html')