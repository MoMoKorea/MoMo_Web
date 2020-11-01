from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from allauth.account.views import SignupView
from allauth.account.views import LoginView
from allauth.account.views import LogoutView
from rest_framework.decorators import api_view, renderer_classes
from django.shortcuts import redirect
from django.urls import reverse
from momo_web.viewname import *

from .forms import MyCustomSignupForm


class Signup(SignupView):
    '''
    django-allauth의 SignupView 상속
    '''
    def __init__(self, arg):
        super(self).__init__()
        self.name = "Joe"

    @api_view(('POST', 'GET'))
    def signup_allauth(request):
        # add code here

        if request.method == 'POST':
            form = MyCustomSignupForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                return redirect(reverse(UserViewname.VIEW_VERIFICATION_SENT))
            else:
                return render(request, 'account/signup.html', {'form': form})
        else:
            return render(request, 'account/signup.html')

class Login(LoginView):
    '''
    django-allauth의 LoginView 상속
    '''
    def __init__(self, arg):
        super(self).__init__()

    def login_allauth(request):
        # add code here
        return render(request, 'account/login.html')

class Logout(LogoutView):
    '''
    django-allauth의 LogoutView 상속
    '''
    def __init__(self, arg):
        super(self).__init__()

    def logout_allauth(request):
        # add code here
        return render(request, 'account/logout.html')

def password_change_allauth(request):

    return render(request, 'accounts/password/change/')

def verification_sent_allauth(request):
    # add code here

    return render(request, 'account/verification_sent.html')

def password_reset_allauth(request):
    # add code here

    return render(request, 'account/password_reset.html')
