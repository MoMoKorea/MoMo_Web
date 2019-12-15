from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    ## 회원가입/로그인 (Writer : Joe)
    path('user/signup', views.Signup.signup_allauth),
    path('user/login', views.Login.login_allauth),
    path('user/logout', views.Logout.logout_allauth),

    path('user/verification_sent', views.verification_sent_allauth),
    path('user/passchange', views.password_change_allauth),
    path('user/passreset', views.password_reset_allauth),


]
