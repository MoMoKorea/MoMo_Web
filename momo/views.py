from django.shortcuts import render

# Create your views here.

def home(request):
    # return render(request, 'account/signup.html')
    # return render(request, 'account/test.html')
    return render(request, 'home.html')
