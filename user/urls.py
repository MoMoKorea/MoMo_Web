from django.urls import path
from . import views
from momo_web.viewname import *

urlpatterns = [

## 회원가입/로그인 (Writer : Joe)
    path('signup', views.Signup.signup_allauth, name="user_signup"),
    path('login', views.Login.login_allauth, name=UserViewname.VIEW_USER_LOGIN),
    path('logout', views.Logout.logout_allauth, name=UserViewname.VIEW_USER_LOGOUT),

    path('verification_sent', views.verification_sent_allauth, name=UserViewname.VIEW_VERIFICATION_SENT),
    path('passchange', views.password_change_allauth),
    path('passreset', views.password_reset_allauth),
]
