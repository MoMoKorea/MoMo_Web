from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
