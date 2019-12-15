from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

## user내의 form에 있는 함수를 불러오는 라인을 짜보시오
from .forms import MyCustomSignupForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def signUpMomo(request):
    context = {}
    return render(request, 'accounts/signup', context = None)
