from django.shortcuts import render

from allauth.account.views import SignupView
from allauth.account.views import LoginView
from allauth.account.views import LogoutView

<<<<<<< HEAD
=======

>>>>>>> bff33c34852d27f5064c67768cf281de5e11b4ae
class Signup(SignupView):
    '''
    django-allauth의 SignupView 상속
    '''
    def __init__(self, arg):
        super(self).__init__()
        self.name = "Joe"

    def signup_allauth(request):
        # add code here

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

def verification_sent_allauth(request):
    # add code here

    return render(request, 'account/verification_sent.html')

def password_change_allauth(request):
    # add code here

    return render(request, 'account/password_change.html')

def password_reset_allauth(request):
    # add code here

    return render(request, 'account/password_reset.html')



# ---------------------------------------------------------------------------------------

# def home(request):
<<<<<<< HEAD
def home(request):
    # return render(request, 'errors.html')
    return render(request, 'mypage/mypage.html')
    # return render(request, 'mypage/help.html')
    # return render(request, 'mypage/contact.html')
    # return render(request, 'mypage/user.html')
=======
>>>>>>> bff33c34852d27f5064c67768cf281de5e11b4ae
    # return render(request, 'account/verification_sent.html')
    # return render(request, 'account/password_reset.html')
    # return render(request, 'account/password_change.html')
    # return render(request, 'account/login.html')
    # return render(request, 'account/signup.html')
    # return render(request, 'account/test.html')
    # return render(request, 'home.html')
