from django.urls import path
from . import views

urlpatterns = [

## 회원가입/로그인 (Writer : Joe)
    path('signup', views.Signup.signup_allauth),
    path('login', views.Login.login_allauth),
    path('logout', views.Logout.logout_allauth),

    path('verification_sent', views.verification_sent_allauth),
    path('passchange', views.password_change_allauth),
    path('passreset', views.password_reset_allauth),
]
