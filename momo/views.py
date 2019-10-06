from django.shortcuts import render

# Create your views here.

def home(request):
    # return render(request, 'account/verification_sent.html')
    # return render(request, 'account/password_reset.html')
    # return render(request, 'account/password_change.html')
    # return render(request, 'account/login.html')
    return render(request, 'account/signup.html')
    # return render(request, 'account/test.html')
    # return render(request, 'home.html')
